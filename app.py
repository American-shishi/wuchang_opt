import streamlit as st
from gear_data import headgear, chestgear, handgear, leggear
from armor_piece import ArmorPiece
from optimizer import score_armor_set, calculate_total_mitigation, calculate_total_resistance
import itertools
from streamlit_js_eval import streamlit_js_eval


screen_width = streamlit_js_eval(js_expressions='window.innerWidth', key="SCR_WIDTH")
is_mobile = screen_width and screen_width < 768

st.markdown(
    """
    <style>
        /* Override Streamlit's max-width constraint */
        .css-1lcbmhc.e1f1d6gn3, .block-container {
            max-width: 100% !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <style>
        /* Shrink spacing around sliders */
        .stSlider {
            padding-top: 0rem;
            padding-bottom: 0rem;
            margin-top: -5px;
            margin-bottom: -10px;
        }

        /* Shrink font and spacing in labels */
        .stSlider label {
            font-size: 0.85rem;
            margin-bottom: 0px;
        }

        /* Expand slider to full width */
        .stSlider div[data-baseweb="slider"] {
            width: 100% !important;
        }

        /* Reduce spacing between widgets in columns */
        div[data-testid="column"] > div {
            padding-bottom: 0.25rem;
        }
    </style>
""", unsafe_allow_html=True)


def get_top_gear(gear_list, weights, base_stat, top_n_overall=8, top_n_per_stat=3):
    mitigation_stats = list(weights["mitigation"].keys())
    resistance_stats = list(weights["resistance"].keys())

    # 1. Top N overall by weighted score
    scored = []
    for item in gear_list:
        mit_score = sum(item.mitigation.get(stat, 0) * weights["mitigation"].get(stat, 0) for stat in mitigation_stats)
        res_score = sum(base_stat * (1 + item.resistances.get(stat, 0) / 100) * weights["resistance"].get(stat, 0) for stat in resistance_stats)
        total_score = mit_score + 0.5 * res_score
        scored.append((total_score, item))
    scored.sort(reverse=True)
    top_overall = set(item for _, item in scored[:top_n_overall])

    # 2. Top N for each individual stat
    top_per_stat = set()

    for stat in mitigation_stats:
        top_items = sorted(gear_list, key=lambda item: item.mitigation.get(stat, 0), reverse=True)[:top_n_per_stat]
        top_per_stat.update(top_items)

    for stat in resistance_stats:
        top_items = sorted(gear_list, key=lambda item: item.resistances.get(stat, 0), reverse=True)[:top_n_per_stat]
        top_per_stat.update(top_items)

    # 3. Combine all selected items
    final_items = list(top_overall.union(top_per_stat))
    return final_items


st.set_page_config(page_title="Gear Optimizer", layout="centered")

st.title("🛡️ Gear Optimizer")

# ─────────────────────────────
# TOP CONTROLS (Mobile or Desktop Layout)
# ─────────────────────────────

if is_mobile:
    high_madness = st.checkbox("High Madness?", value=True)
    dlc_enabled = st.checkbox("Include DLC Armor (Chapter 0)", value=True)
    max_chapter = st.selectbox("Max Chapter to Include", options=[1, 2, 3, 4, 5], index=4)
else:
    with st.container():
        cols = st.columns([1, 1, 1.5])
        high_madness = cols[0].checkbox("High Madness?", value=True)
        dlc_enabled = cols[1].checkbox("Include DLC Armor (Ch. 0)", value=True)
        max_chapter = cols[2].selectbox("Max Chapter", options=[1, 2, 3, 4, 5], index=4)

base_resistance_stat = 130 if high_madness else 100
st.caption(f"Base Resistance Stat = {base_resistance_stat}")

available_gear = {}

def gear_filter(item):
    if item.chapter == 0:
        return dlc_enabled
    elif item.chapter <= max_chapter:
        return True
    elif item.chapter == 6:
        return False
    return False

gear_sources = {
    "head": headgear,
    "chest": chestgear,
    "arms": handgear,
    "legs": leggear
}

# Layout for gear selection expanders
st.markdown("### 🎒 Available Gear Selection")

if is_mobile:
    for slot, gear_dict in gear_sources.items():
        selected_items = []
        with st.expander(f"{slot.capitalize()} Gear", expanded=False):
            for name, piece in gear_dict.items():
                default_checked = gear_filter(piece)
                if st.checkbox(name, value=default_checked, key=f"{slot}_{name}"):
                    selected_items.append(piece)
        available_gear[slot] = selected_items
else:
    gear_cols = st.columns(4)
    for i, (slot, gear_dict) in enumerate(gear_sources.items()):
        selected_items = []
        with gear_cols[i].expander(f"{slot.capitalize()} Gear", expanded=False):
            for name, piece in gear_dict.items():
                default_checked = gear_filter(piece)
                if st.checkbox(name, value=default_checked, key=f"{slot}_{name}"):
                    selected_items.append(piece)
        available_gear[slot] = selected_items



if is_mobile:
    left = st.container()
    right = st.container()
else:
    left, right = st.columns([3, 2])

with left:
    st.subheader("🎚️ Stat Weight Sliders")
    st.caption("Adjust how much each stat matters to you. Higher weights prioritize that stat more.")

    st.markdown("**Mitigation Weights**")
    mitigation_weights = {}
    for stat in ArmorPiece.mitigation_order:
        mitigation_weights[stat] = st.slider(
            stat, 0.1, 5.0,
            3.0 if stat in ["Slash", "Blunt", "Stab"] else (0.1 if stat == "Tenacity" else 0.5), 0.05,
            key=f"mit_{stat}"
        )

    st.markdown("**Resistance Weights**")
    resistance_weights = {}
    for stat in ArmorPiece.resistance_order:
        resistance_weights[stat] = st.slider(
            stat, 0.1, 2.0, 0.1, 0.05, key=f"res_{stat}"
        )

with right:
    st.subheader("⚙️ Run & Results")
    if st.button("🔍 Optimize Gear"):
        # Filter top 20 per slot before running optimizer
        armor_by_slot = {
            slot: get_top_gear(
                available_gear[slot],
                {"mitigation": mitigation_weights, "resistance": resistance_weights},
                base_resistance_stat,
            )
            for slot in available_gear
        }
        best_score = float('-inf')
        best_combo = None

        for combo in itertools.product(
                armor_by_slot["head"],
                armor_by_slot["chest"],
                armor_by_slot["arms"],
                armor_by_slot["legs"]
        ):
            score = score_armor_set(combo, {"mitigation": mitigation_weights, "resistance": resistance_weights}, base_resistance_stat)
            if score > best_score:
                best_score = score
                best_combo = combo

        st.markdown("### 🎯 Best Gear Set")
        for piece in best_combo:
            st.markdown(
                f"<div style='font-size:18px;'>"
                f"{piece.slot.capitalize()}: <span style='font-weight:bold; color:green;'>{piece.name}</span>"
                f"</div>",
                unsafe_allow_html=True
            )

        final_mitigation = calculate_total_mitigation(best_combo)
        final_resistance = calculate_total_resistance(best_combo, base_resistance_stat)

        st.markdown("### 🧮 Final Mitigation")
        for stat in ArmorPiece.mitigation_order:
            value = final_mitigation[stat] * 100
            if stat in ["Slash", "Blunt", "Stab"]:
                st.markdown(
                    f"<div style='font-size:16px; font-weight:bold;'>{stat:<10}: {value:.2f}%</div>",
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f"<div style='font-size:16px;'>{stat:<10}: {value:.2f}%</div>",
                    unsafe_allow_html=True
                )

        st.markdown("### 🧬 Final Resistances")
        for stat in ArmorPiece.resistance_order:
            value = final_resistance[stat]
            st.markdown(
                f"<div style='font-size:16px;'>{stat:<12}: {value:.2f}</div>",
                unsafe_allow_html=True
            )
    else:
        st.info("Set your weights and click **Optimize Gear** to begin.")
