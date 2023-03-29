from dataclasses import dataclass

from jsonconstants import JSONConstants


@dataclass
class Attributes:
    intelligence: int
    strength: int
    endurance: int
    spicyFoodTolerance: int

    def __init__(self, json):
        self.strength = json[JSONConstants.strength]
        self.intelligence = json[JSONConstants.intelligence]
        self.spicyFoodTolerance = json[JSONConstants.spicy_food_tolerance]
        self.endurance = json[JSONConstants.endurance]



