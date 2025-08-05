class ArmorPiece:
    mitigation_order = [
        "Slash", "Blunt", "Stab", "Feathering",
        "Magic", "Lightning", "Fire", "Tenacity"
    ]
    resistance_order = [
        "Blight", "PoiseBreak", "Burn", "Frostbite",
        "Corruption", "Despair", "Paralysis"
    ]

    def __init__(self, name, mitigation, resistances, chapter, slot=None):
        self.name = name
        self.slot = slot
        self.chapter = chapter

        self.mitigation = dict(zip(self.mitigation_order, mitigation))
        self.resistances = dict(zip(self.resistance_order, resistances))

        # Also assign each stat as an object attribute for convenience
        for stat, val in self.mitigation.items():
            setattr(self, stat, val)
        for stat, val in self.resistances.items():
            setattr(self, stat, val)

    def __repr__(self):
        return f"{self.name}"