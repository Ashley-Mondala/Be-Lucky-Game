from class_type_stats import ClassType, ClassStats
from player import Player


def player_setter():
    name = input("Enter your name: ")
    player_class = input("Please choose one of the following class:\nWarrior\nRanger\nAssassin\nWizard\nDriud\n")

    match player_class.lower():
        case ClassType.WARRIOR:
            warrior = ClassStats(attack_damage=55, accuracy=70, health=110, speed=55, defense=100)
            user = Player(name=name, class_type=ClassType.WARRIOR, stats=warrior, stage = 0)
            return user
        
        case ClassType.RANGER:
            ranger = ClassStats(attack_damage=70, accuracy=75, health=70, speed=70, defense=40)
            user = Player(name=name, class_type=ClassType.RANGER, stats=ranger, stage = 0)
            return user
        
        case ClassType.ASSASSIN:
            assassin = ClassStats(attack_damage=75, accuracy=80, health=60, speed=80, defense=30)
            user = Player(name=name, class_type=ClassType.ASSASSIN, stats=assassin, stage = 0)
            return user
        
        case ClassType.WIZARD:
            wizard = ClassStats(attack_damage=75, accuracy=80, health=70, speed=50, defense=50)
            user = Player(name=name, class_type=ClassType.WIZARD, stats=wizard, stage = 0)
            return user
        
        case ClassType.DRUID:
            druid = ClassStats(attack_damage=60, accuracy=60, health=90, speed=60, defense=80)
            user = Player(name=name, class_type=ClassType.DRUID, stats=druid, stage = 0)
            return user
        
        case _:
            raise Exception("Not a valid class type")
    