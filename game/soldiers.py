class Soldier:
    """The base class of all the soldiers of the game"""
    soldierCount = 0

    def __init__(self, name, country):
        self.name = name
        self.country = country
        Soldier.soldierCount += 1

    def __repr__(self):
        return "Soldier()"

    def __str__(self):
        return "a specific soldier of the game"

    
        
        