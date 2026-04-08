class Special:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return self.name

Perk = None
SurvivalSense = Special("Survival Sense","Higher chance to find food and drink.")

CombatInsight = Special("Combat Insight","50% chance to deal a successful strike against basic enemies.")

TrapSense = Special("Trap Sense","Detect and avoid traps.")

WeirdLuck = Special("Weird Luck", "Unpredictable effects may occur.")