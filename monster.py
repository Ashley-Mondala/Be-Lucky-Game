import random
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
        self.block = False
    
    def get_stats(self):
        stats = f"Attack Damage: {self.get_attack_damage}\nAccuracy: {self.get_accuracy}\nHP: {self.get_health}\nSpeed: {self.get_speed}\nDefense: {self.get_defense}"
        return stats

    def get_attack_damage(self):
        return self.stats.attack_damage

    def get_accuracy(self):
        return self.stats.accuracy
         
    def get_health(self):
        return self.stats.health
    
    def get_speed(self):
        return self.stats.speed
    
    def get_defense(self):
        return self.stats.speed
    
    def take_damage(self, player_attack: int):
        damage_taken = player * (self.get_defense // 100)
        self.stats.health -= damage_taken
    
    def buff(self, attack_buff: int, accuracy_buff: int, hp_restore: int, defense_buff: int):
        self.stats.attack_damage  += attack_buff
        self.stats.accuracy_buff += accuracy_buff
        self.stats.health += hp_restore
        self.stats.defense += defense_buff
    
    def hits_attack(self):
        if_hits_num = random.randint(1, 100)
        if if_hits_num  <= self.accuracy:
            return True
        return False

    def is_dead(self):
        if self.stats.health <= 0:
            return True
        return False
    
