from class_type_stats import ClassStats, ClassType

class Player():
    def __init__(self, name: str, class_type: ClassType, stats: ClassStats):
        self.name = name
        self.class_type = ClassType
        self.stats = stats
    
    def get_stats(self):
        attack_damage = self.stats.attack_damage
        accuracy = self.stats.accuracy
        hp = self.stats.health
        speed = self.stats.speed
        defense = self.stats.defense
        
        stats = f"Attack Damage: {attack_damage}\nAccuracy: {accuracy}\nHP: {hp}\nSpeed: {speed}\nDefence: {defense}"
        return stats
    
    
    
