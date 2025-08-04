class ArmorPiece:
    mitigation_order = [
        "Slash", "Blunt", "Stab", "Feathering",
        "Magic", "Lightning", "Fire", "Tenacity"
    ]
    resistance_order = [
        "Blight", "PoiseBreak", "Burn", "Frostbite",
        "Corruption", "Despair", "Paralysis"
    ]

    def __init__(self, name, mitigation, resistances, slot=None):
        self.name = name
        self.slot = slot

        self.mitigation = dict(zip(self.mitigation_order, mitigation))
        self.resistances = dict(zip(self.resistance_order, resistances))

        # Also assign each stat as an object attribute for convenience
        for stat, val in self.mitigation.items():
            setattr(self, stat, val)
        for stat, val in self.resistances.items():
            setattr(self, stat, val)

    def __repr__(self):
        return f"{self.name}"

headgear = {
    "Embroidered Headband": ArmorPiece(
        "Embroidered Headband",
        [7.0, 5.9, 7.0, 7.4, 7.2, 8.7, 8.9, 1.0],  # mitigation: Slash → Tenacity (8 items)
        [23, 23, 23, 23, 23, 23, 23]     # resistances: Blight → Paralysis (7 items)
    ),
    "Night Spectre - High Crown": ArmorPiece(
        "Night Spectre - High Crown",
        [5.2, 4.0, 4.9, 14.7, 15.1, 5.6, 5.2, 1.5],
        [29.9, -2.38, -1.78, -2.75, 24.98, 24.72, -1.69]
    ),
    "White Spectre - High Crown": ArmorPiece(
        "White Spectre - High Crown",
        [4.0, 4.3, 5.1, 5.7, 5.5, 12.4, 13.9, 1.7],
        [-1.61, -3.61, 23.64, 29.43, 10.88, 28.85, 27.17]
    ),
    "Soul Ritual Robe - Crown": ArmorPiece(
        "Soul Ritual Robe - Crown",
        [11.3, 16.0, 16.7, 8.6, 8.9, 8.2, 6.6, 1.1],
        [10.09, -8.35, 15.25, -5.62, 16.63, 2.97, -7.49]
    ),
    "Draconic Resurgence - Crown": ArmorPiece(
        "Draconic Resurgence - Crown",
        [9.1, 8.2, 8.2, 2.0, 10.8, 7.7, 14.2, 1.5],
        [-9.2, -10.4, 23.2, 26.9, -10.8, 9.9, 24]
    ),
    "Overlord's Regalia - Hairpin": ArmorPiece(
        "Overlord's Regalia - Hairpin",
        [12.6, 12.6, 12.9, 8.0, 8.3, 8.1, 7.4, 1.0],
        [12.71, -4.7, 15.03, -5.19, -9.12, 2.61, -6.4]
    ),
    "Dhutanga's Mask": ArmorPiece(
        "Dhutanga's Mask",
        [2.4, 2.0, 2.2, 20.0, 8.4, 5.2, 27.4, 0.2],
        [33, 5.2, 45, 18, 36, 21, -9.54]
    ),
    "Ming Helmet": ArmorPiece(
        "Ming Helmet",
        [18.0, 5.5, 22.0, 0.6, 2.5, 0.6, 10.0, 2.3],
        [-20, -15.13, 17, 7, -30, -30, -18.72]
    ),
    "Pirate Hairpin": ArmorPiece(
        "Pirate Hairpin",
        [7.4, 6.7, 7.4, 9.5, 10.6, 8.4, 10.5, 1.1],
        [11.37, 5.63, 11.37, 9.95, 8.53, 14, 7.65]
    ),
    "Delicate Hairpin": ArmorPiece(
        "Delicate Hairpin",
        [2.2, 3.7, 3.1, 6.5, 12.3, 9.2, 10.0, 0.4],
        [30.95, 17.12, 4.1, 3.6, 23.21, 30, 18.49]
    ),
    "Zhenwu Hairpin": ArmorPiece(
        "Zhenwu Hairpin",
        [2.8, 2.5, 1.5, 10.1, 26.2, 24.2, 20.1, 0.3],
        [-14.1, 13.87, 25.11, 36.26, 22.32, -1, 28.44]
    ),
    "Beaked Hood": ArmorPiece(
        "Beaked Hood",
        [6.4, 5.8, 7.0, 19.6, 14.5, 12.3, 0.5, 1.1],
        [24.74, 4.77, -24.74, 17.32, 12.37, 29.68, 4.66]
    ),
    "Golden Bandits Cap": ArmorPiece(
        "Golden Bandits Cap",
        [10.5, 13.5, 15.6, 5.0, 9.5, 4.6, 7.1, 1.2],
        [20.5, 12.57, -7, 8.2, 6.5, -15, -15.78]
    ),
    "Palace Maid's Hairpin": ArmorPiece(
        "Palace Maid's Hairpin",
        [3.7, 5.4, 2.8, 20, 19.7, 15.7, 3.4, 0.4],
        [15, 18.85, 21.47, 15.3, 24.16, 35, 11.54]
    ),
    "Imperial Bamboo Hat": ArmorPiece(
        "Imperial Bamboo Hat",
        [6.0, 8.0, 16.0, 8.0, 8.4, 10.0, 8.0, 1.8],
        [3.32, 3.03, 18, 1.74, 1.58, 1.89, 0]
    ),
    "Clerical Mask": ArmorPiece(
        "Clerical Mask",
        [9.0, 10.7, 6.3, 9.6, 24.0, 2.4, 3.4, 0.7],
        [45, 15.6, -12, 6, 18.6, 14.6, 4.5]
    ),
    "Centipede Hood": ArmorPiece(
        "Centipede Hood",
        [20.0, 6.2, 23.5, 6.2, 0.3, 0.3, 0.3, 2.1],
        [25, -16.96, -22.4, -12.5, 22, -8, -20.12]
    ),
    "Bridal Veil": ArmorPiece(
        "Bridal Veil",
        [4.0, 4.8, 4.8, 6.7, 10, 13.2, 9.1, 0.6],
        [21.32, 27, 21, 10, 28.42, 26.05, 6.4]
    ),
}

chestgear = {
    "Embroidered Armor": ArmorPiece(
        "Embroidered Armor",
        [10.5, 11.1, 10.0, 12.5, 12.3, 14.4, 10.7, 2.4],  # mitigation: Slash → Tenacity (8 items)
        [31.4, 31.4, 31.4, 31.4, 31.4, 31.4, 31.4]     # resistances: Blight → Paralysis (7 items)
    ),
    "Night Spectre - Robes": ArmorPiece(
        "Night Spectre - Robes",
        [8.9, 8.1, 7.5, 27.4, 28.1, 7.8, 8.3, 2.8],
        [39.95, -2.91, -2.78, -5.64, 33.14, 40.86, 0]
    ),
    "White Spectre - Robes": ArmorPiece(
        "White Spectre - Robes",
        [8.4, 8.4, 8.0, 7.5, 7.7, 22.2, 28.7, 2.8],
        [-3.07, -7.12, 34.56, 44.66, 14.68, 42.21, 43.48]
    ),
    "Tiger of Fortune - Outfit": ArmorPiece(
        "Tiger of Fortune - Outfit",
        [6.2, 28.7, 7.1, 8.9, 13.7, 10.0, 1.6, 2.6],
        [29.14, 47.3, -23.09, 55.01, 35.81, 29.06, 36.01]
    ),
    "Soul Ritual Robe - Robe": ArmorPiece(
        "Soul Ritual Robe - Robe",
        [21.1, 14.7, 14.9, 13.5, 17.8, 15.2, 17.9, 1.2],
        [47.28, -16.46, 44.03, -10.82, 26.28, 4.36, -21.99]
    ),
    "Draconic Resurgence - Robe": ArmorPiece(
        "Draconic Resurgence - Robe",
        [12.2, 12.7, 13.0, 4.4, 22.2, 10.8, 18.2, 2.0],
        [-20.1, -13.9, 49.4, 50.3, -18.8, 13.1, 48.7]
    ),
    "Overlord's Regalia - Coat": ArmorPiece(
        "Overlord's Regalia - Coat",
        [17.8, 19.0, 17.9, 13.6, 15.4, 15.2, 15.9, 1.0],
        [40.11, -9.35, 45.03, -10.57, -15.86, 3.94, -21.08]
    ),
    "Dhutanga's Robes": ArmorPiece(
        "Dhutanga's Robes",
        [14.4, 14.0, 15.4, 12.5, 5.0, 2.8, 16.3, 2.7],
        [7.25, 15.4, 19.76, 3.95, 7.91, -10.64, -24.39]
    ),
    "Ming Armor": ArmorPiece(
        "Ming Armor",
        [27.3, 9.7, 26.8, 0.9, 3.6, 0.9, 8.6, 3.8],
        [-14.12, -24.95, 14.12, 6, -19.76, -18.35, -28.15]
    ),
    "Pirate Armor": ArmorPiece(
        "Pirate Armor",
        [15.2, 15.5, 16.2, 10.1, 11.3, 15.8, 10.1, 2.5],
        [8.28, 19.02, 8.28, 7.25, 17, 6, 16.4]
    ),
    "Delicate Armor": ArmorPiece(
        "Delicate Armor",
        [3.0, 5.9, 4.9, 27.1, 16.5, 24.0, 24.0, 0.8],
        [48.56, 47.5, 1.4, 4.21, 36.42, 47, 21.82]
    ),
    "Golden Bandits Robes": ArmorPiece(
        "Golden Bandits Robes",
        [17.5, 15.0, 13.2, 16.4, 12.5, 9.6, 8.1, 1.0],
        [45, 25.04, -6.7, 45, 34, 14, 5]
    ),
    "Fake Monk Robes": ArmorPiece(
        "Fake Monk Robes",
        [15.6, 14.4, 15.6, 4.5, 20.0, 18.7, 10.5, 1.3],
        [30.1, 10.39, 10, 21.7, 15, -14.4, 7.4]
    ),
    "Dazzling Fake Monk Robes": ArmorPiece(
        "Dazzling Fake Monk Robes",
        [15.6, 14.4, 15.6, 16.8, 20.4, 20.5, 2.5, 1.3],
        [30.1, 10.39, -14, 21.7, 43, -14, 11]
    ),
    "Palace Maid's Satin Dress": ArmorPiece(
        "Palace Maid's Satin Dress",
        [13, 14.3, 14.5, 26.1, 18.0, 19.0, 7, 1.1],
        [14.12, 20.82, -19.15, 12.78, 31.34, 41.5, 16]
    ),
    "Imperial Uniform": ArmorPiece(
        "Imperial Uniform",
        [14.0, 14.5, 6.0, 6.0, 14.2, 14.0, 18.0, 2.8],
        [9.88, 28.66, 20, 15.18, -14.71, -15.65, -2]
    ),
    "Clerical Robes": ArmorPiece(
        "Clerical Robes",
        [4.5, 7.0, 6.1, 30.2, 29.0, 8.4, 8.2, 1.6],
        [26, 25.64, -13, 9.5, 24.62, -13, 9.5, 24.62, 22.3, 6.7]
    ),
    "Bridal Corset": ArmorPiece(
        "Bridal Corset",
        [5.9, 7.0, 7.0, 16, 15, 22.6, 15.1, 0.9],
        [34.73, 42.5, 3, 24, 46.31, 42.45, 15.36]
    )
}

armgear = {
    "Embroidered Vambraces": ArmorPiece(
        "Embroidered Vambraces",
        [6.7, 5.6, 6.6, 4.7, 4.7, 3.6, 4.1, 1.2],  # mitigation: Slash → Tenacity (8 items)
        [3, 3, 3, 3, 3, 3, 3]     # resistances: Blight → Paralysis (7 items)
    ),
    "Night Spectre - Bracers": ArmorPiece(
        "Night Spectre - Bracers",
        [3.0, 2.9, 3.0, 7.5, 10.3, 2.9, 2.4, 0.8],
        [14.04, -1.25, -1.07, -1.66, 14.83, 14.13, 0]
    ),
    "White Spectre - Bracers": ArmorPiece(
        "White Spectre - Bracers",
        [2.5, 3.5, 3.1, 18.0, 2.7, 10.5, 8.2, 0.7],
        [-1.09, -2.14, 16.8, 13.07, 4.05, 16.85, 13.14]
    ),
    "Soul Ritual Robe - Bracers": ArmorPiece(
        "Soul Ritual Robe - Bracers",
        [7.5, 6.8, 6.5, 4.8, 4.0, 4.0, 5.1, 0.8],
        [8.99, -4.61, 15.13, -2.56, 12.62, 1.56, -6.69]
    ),
    "Draconic Resurgence - Bracers": ArmorPiece(
        "Draconic Resurgence - Bracers",
        [7.3, 7.8, 6.9, 1.1, 8.0, 5.3, 10.7, 0.5],
        [-4, -6.5, 16.4, 16.2, -3.7, 5.8, 15.8]
    ),
    "Overlord's Regalia - Bracers": ArmorPiece(
        "Overlord's Regalia - Bracers",
        [6.7, 6.6, 7.5, 4.1, 4.8, 4.1, 4.5, 0.7],
        [8.18, -3.2, 15.86, -2.99, -6.88, 1.5, -7.17]
    ),
    "Dhutanga's Prayer Beads": ArmorPiece(
        "Dhutanga's Praryer Beads",
        [4.5, 3.7, 4.1, 7.7, 3.1, 1.1, 10.1, 0.8],
        [11.8, 5.55, 17.16, 6.44, 12.87, 7.51, -7.62]
    ),
    "Ming Armguards": ArmorPiece(
        "Ming Armguards",
        [9.0, 3.6, 11.9, 0.4, 2.5, 0.4, 3.9, 1.4],
        [-4.55, -9.77, 4.55, 3, -6.36, -5.92, -9.21]
    ),
    "Pirate Bracers": ArmorPiece(
        "Pirate Bracers",
        [9.5, 8.0, 8.2, 2.9, 3.3, 2.5, 2.9, 1.2],
        [0.44, 5.68, 0.44, 0.38, 0.33, 0.65, 0.42]
    ),
    "Delicate Bracelet": ArmorPiece(
        "Delicate Bracelet",
        [3.5, 2.0, 2.9, 4.3, 7.5, 4.8, 4.2, 0.7],
        [13.75, 23, 2.3, 3.1, 10.31, 14, 4.92]
    ),
    "Golden Bandits Bracers": ArmorPiece(
        "Golden Bandits Bracers",
        [6.3, 7.5, 4.5, 7.8, 7.4, 5.7, 6.3, 0.7],
        [41, 7.07, 4.25, 3.33, 6.75, 4.25, 9.07]
    ),
    "Palace Maid's Bracelet": ArmorPiece(
        "Palace Maid's Bracelet",
        [1.3, 1.5, 1.9, 10, 11.2, 9, 1.2, 0.6],
        [13.4, 6.1, -12.07, 13.7, 13.58, 18.9, 14]
    ),
    "Imperial Bracers": ArmorPiece(
        "Imperial Bracers",
        [7.6, 5.4, 5.0, 4.0, 5.5, 6.0, 4.0, 1.1],
        [4.2, 5.27, 1, 2.2, 2, 2.4, 2]
    ),
    "Clerical Belt": ArmorPiece(
        "Clerical Belt",
        [3.0, 6.0, 4.0, 10.2, 16.0, 4.3, 2.0, 0.5],
        [24, 8.45, -8, 3, 8.6, 6.4, 3]
    ),
    "Centipede Vambraces": ArmorPiece(
        "Centipede Vambraces",
        [9.8, 4.2, 9.4, 8.5, 0.4, 0.2, 0.4, 1.4],
        [14, -11.07, -21, -14.5, 14.7, -4.25, -17.6]
    ),
    "Bridal Shackles": ArmorPiece(
        "Bridal Shackles",
        [3.0, 3.5, 3.5, 6.7, 4.5, 8.2, 3.7, 0.7],
        [10.96, 13.4, 14.5, 6.5, 14.62, 13.4, 6.47]
    ),
}

leggear = {
    "Embroidered Vambraces": ArmorPiece(
        "Embroidered Boots",
        [5.6, 5.4, 5.7, 8.2, 9.2, 7.2, 8.2, 1.0],  # mitigation: Slash → Tenacity (8 items)
        [7.8, 7.8, 7.8, 7.8, 7.8, 7.8, 7.8]     # resistances: Blight → Paralysis (7 items)
    ),
    "Night Spectre - Shin Wraps": ArmorPiece(
        "Night Spectre - Shin Wraps",
        [3.7, 3.4, 4.7, 10.9, 13.1, 3.5, 4.2, 1.4],
        [19.03, -1.55, -1.35, -1.99, 16.11, 22.76, 0]
    ),
    "White Spectre - Shin Wraps": ArmorPiece(
        "White Spectre - Shin Wraps",
        [4.6, 3.9, 3.3, 3.6, 3.5, 10.8, 13.7, 1.3],
        [-1.36, -2.7, 18.33, 19.46, 4.32, 22.95, 16.34]
    ),
    "Soul Ritual Robe - Boots": ArmorPiece(
        "Soul Ritual Robe - Boots",
        [8.6, 7.2, 6.4, 7.1, 6.1, 6.0, 8.7, 0.8],
        [11.55, -10.35, 22.85, -6.73, 12.52, 1.91, -9.09]
    ),
    "Draconic Resurgence - Long Boots": ArmorPiece(
        "Draconic Resurgence - Long Boots",
        [8.7, 9.3, 8.2, 1.4, 10.1, 6.1, 11.4, 1.0],
        [-8.1, -12.5, 14, 14.8, -7.7, 13.4, 15]
    ),
    "Overlord's Regalia - Long Boots": ArmorPiece(
        "Overlord's Regalia - Long Boots",
        [7.8, 8.4, 7.3, 6.9, 7.7, 8.0, 7.0, 1.0],
        [10.04, -5.56, 18.3, -5.97, -8.14, 1.99, -10.21]
    ),
    "Ming Greaves": ArmorPiece(
        "Ming Greaves",
        [12.5, 5.0, 13.7, 0.4, 1.6, 0.4, 3.5, 2.0],
        [-8, -13.12, 10, 7, -11.2, -10.4, -13.93]
    ),
    "Pirate Boots": ArmorPiece(
        "Pirate Boots",
        [8.3, 7.1, 6.1, 6.4, 7.2, 5.6, 6.4, 0.9],
        [10.84, 5.01, 10.84, 12.49, 8.13, 14, 9.12]
    ),
    "Delicate Leggings": ArmorPiece(
        "Delicate Leggings",
        [3.1, 3.1, 2.6, 7.1, 6.4, 8.9, 8.3, 0.4],
        [24.15, 9.48, 3, 0.5, 18.11, 24.7, 24.52]
    ),
    "Golden Bandits Leg Wraps": ArmorPiece(
        "Golden Bandits Leg Wraps",
        [10.1, 7.2, 14.5, 4.0, 4.2, 1.5, 3.1, 0.5],
        [15, 10.98, -7.12, 18, 9.22, 3.28, -11]
    ),
    "Fake Monk Sandals": ArmorPiece(
        "Fake Monk Sandals",
        [7.8, 7.2, 7.8, 2.2, 14.0, 1.5, 5.4, 0.6],
        [15.1, 3.12, 3.2, 14.9, 12.3, -3.7, -11]
    ),
    "Palace Maid's Garment": ArmorPiece(
        "Palace Maid's Garment",
        [1, 1, 1, 1, 1, 1, 1, 0.2],
        [17.6, 3.98, -14.4, 14, 21.6, 43, 13]
    ),
    "Imperial Riding Boots": ArmorPiece(
        "Imperial Riding Boots",
        [8.3, 7.7, 8.0, 5.0, 6.7, 7.0, 5.0, 1.5],
        [1.53, 3.5, 0.36, 0.8, 0.73, 0.87, 3.67]
    ),
    "Clerical Waist Cloth": ArmorPiece(
        "Clerical Waist Cloth",
        [3.5, 8.0, 5.0, 12.8, 18.0, 7.5, 3.0, 0.8],
        [30, 13.62, -18, 4.2, 3, 14.5, 6.12]
    ),
    "Centipede Leg Armor": ArmorPiece(
        "Centipede Leg Armor",
        [14.5, 4.8, 17.2, 9.2, 0.5, 0.4, 0.6, 1.8],
        [23, -15.65, -17.5, -15.6, 18.5, -6.25, -18.5]
    ),
    "Bridal Dress": ArmorPiece(
        "Bridal Dress",
        [2.6, 3.0, 3.0, 10.5, 11.2, 13.7, 9.1, 0.3],
        [18.98, 21, 4.5, 7.8, 25.31, 23.2, 21.58]
    )
}

# Automatically assign slot to each piece in its category
for piece in headgear.values():
    piece.slot = "head"

for piece in chestgear.values():
    piece.slot = "chest"

for piece in armgear.values():
    piece.slot = "arms"

for piece in leggear.values():
    piece.slot = "legs"