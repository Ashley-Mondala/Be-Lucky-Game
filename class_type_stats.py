from enum import Enum

class ClassType(Enum):
    WARRIOR = "warrior"
    RANGER = "ranger"
    ASSASSIN = "assassin"
    WIZARD = "wizard"
    DRUID = "druid"


class ClassStats:
    def __init__(self, attack_damage: int, accuracy:  int, health: int, speed: int, defense: int):
        self.attack_damage = attack_damage
        self.accuracy = accuracy
        self.health = health
        self.speed = speed
        self.defense = defense

