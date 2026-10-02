from class_type_stats import ClassStats, ClassType

class Player():
    def __init__(self, name: str, class_type: ClassType, stats: ClassStats, stage: int):
        self.name = name
        self.class_type = ClassType
        self.stats = stats
        self.stage = stage
        self.block = False
        self.turn = False
    
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
    
    def take_damage(self, monster_attack: int):
        damage_taken = monster_attack * (self.get_defense // 100)
        self.stats.health -= damage_taken
    
    def buff(self, attack_buff: int, accuracy_buff: int, hp_restore: int, defense_buff: int):
        self.stats.attack_damage  += attack_buff
        self.stats.accuracy_buff += accuracy_buff
        self.stats.health += hp_restore
        self.stats.defense += defense_buff
    
    def can_use_move(self, roll, accepted_num):
        if roll <= accepted_num:
            return True
        return False
    
    def is_dead(self):
        if self.stats.health <= 0:
            return True
        return False