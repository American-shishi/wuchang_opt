import streamlit as st
from gear_data import headgear, chestgear, armgear, leggear, ArmorPiece
from optimizer import score_armor_set, calculate_total_mitigation, calculate_total_resistance
import itertools

st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 350px !important;  /* wider sidebar */
        }
        section[data-testid="stSidebar"] > div {
            width: 350px !important;
        }
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

st.set_page_config(page_title="Gear Optimizer", layout="centered")

st.title("🛡️ Gear Optimizer")

# Build selector for each slot
available_gear = {}
gear_sources = {
    "head": headgear,
    "chest": chestgear,
    "arms": armgear,
    "legs": leggear
}

high_madness = st.sidebar.checkbox("High Madness?", value=True)  # default checked
base_resistance_stat = 130 if high_madness else 100
st.sidebar.caption(f"Base Resistance Stat = {base_resistance_stat}")

# Sidebar for gear selection
st.sidebar.subheader("🎒 Available Gear Selection")

available_gear = {}
for slot, gear_dict in gear_sources.items():
    with st.sidebar.expander(f"{slot.capitalize()} Gear", expanded=False):
        selected_items = []
        for name, piece in gear_dict.items():
            if st.checkbox(f"{name}", value=True, key=f"{slot}_{name}"):
                selected_items.append(piece)
        available_gear[slot] = selected_items


left, right = st.columns([3, 2])  # 60% | 40% split

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
        armor_by_slot = available_gear
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
