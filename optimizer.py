import itertools

def calculate_total_mitigation(armor_set):
    """Apply diminishing returns across all mitigation stats"""
    stat_keys = armor_set[0].mitigation.keys()
    cumulative = {stat: 1.0 for stat in stat_keys}

    for piece in armor_set:
        for stat in stat_keys:
            cumulative[stat] *= (1 - piece.mitigation[stat] / 100)

    return {stat: 1 - cumulative[stat] for stat in stat_keys}  # Final effective mitigation

def calculate_total_resistance(armor_set, base_stat):
    """Sum all resistances linearly and apply to baseline stat"""
    stat_keys = armor_set[0].resistances.keys()
    total_resist = {stat: 0 for stat in stat_keys}

    for piece in armor_set:
        for stat in stat_keys:
            total_resist[stat] += piece.resistances[stat]

    return {stat: base_stat * (1 + total_resist[stat]/100) for stat in stat_keys}

def score_armor_set(armor_set, weights, base_resistance_stat):
    """Score gear combination based on mitigation/resistance and weights"""
    mitigation = calculate_total_mitigation(armor_set)
    resistance = calculate_total_resistance(armor_set, base_resistance_stat)

    score = 0
    for stat, weight in weights.get("mitigation", {}).items():
        score += weight * mitigation.get(stat, 0)

    for stat, weight in weights.get("resistance", {}).items():
        # Normalize resistance values (optional scaling)
        score += (weight * resistance.get(stat, 0) / base_resistance_stat) * 0.5

    return score
