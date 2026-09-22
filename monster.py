from rank import Rank
from class_type_stats import ClassStats

class MonsterStats(ClassStats):
    def __init__(attack_damage:int, accuracy:int, health:int, speed: int, defense: int):
        super().__init__(attack_damage=attack_damage, accuracy=accuracy,health=health, speed=speed, defense=defense)

class Monster():
    def __init__(self, name:str, rank: Rank, stats: MonsterStats):
        self.name = name
        self.rank = rank
        self.stats = MonsterStats
    
    def get_stats(self):
        attack_damage = self.stats.attack_damage
        accuracy = self.stats.accuracy
        hp = self.stats.health
        speed = self.stats.speed
        defense = self.stats.defense
        
        stats = f"Attack Damage: {attack_damage}\nAccuracy: {accuracy}\nHP: {hp}\nSpeed: {speed}\nDefence: {defense}"
        return stats