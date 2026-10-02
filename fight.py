import random
from player import Player
from monster import Monster
from monster_buff_by_rank import monster_rank_buffs


def player_turn(user: Player, monster: Monster):
    move = input("1. Attack\n2. Defend\n3. Buff\n4.Ultimate")
    move_passes = random.randint(1, 100)
    
    # if user inputs attack
    if move.lower() == "attack" or int(move) == 1:
        if user.can_use_move(roll=move_passes, accepted_num=user.stats.accuracy):
            if monster.block:
                monster.take_damage(user.get_attack_damage // 2)
                monster.block = False
            else:
                monster.take_damage(user.get_attack_damage)
    
    # if user inputs defend
    elif move.lower() == "defend" or int(move) == 2:
        if user.can_use_move(roll=move_passes, accepted_num=90):
            user.block = True
    
    # if user inputs buff
    elif move.lower() == "buff" or int(move) == 3:
        if user.can_use_move(roll=move_passes, accepted_num=65)::
            user.buff(attack_buff=10, accuracy_buff=5, hp_restore=15, speed_buff=2, defense_buff=10)
    
    # if user inputs ultimate
    elif move.lower() == "ultimate" or int(move) == 4:
        if user.can_use_move(roll=move_passes, accepted_num=35):
            if monster.block:
                monster.take_damage((user.get_attack_damage + 100) // 2)
                monster.block = False
            else:
                monster.take_damage(user.get_attack_damage + 100)
    user.player_turn = False

def monster_turn(monster: Monster, user: Player):
    moveset_roll = random.randint(1, 100)
    
    # buffs
    if moveset_roll <= 10:
        print(f"{monster.name.title()} buffs itself!")
        rank = monster.rank
        monster.buff(attack_buff=monster_rank_buffs[rank][0], accuracy_buff=monster_buff_by_rank[rank][1], hp_restore=monster_buff_by_rank[rank][2], defense_buff[rank][3])
   
    #defense
    elif moveset_roll <= 30:
        print(f"{monster.name.title()} uses defend!")
        monster.block = True
    
    #attack
    elif moveset_roll <= 60:
        if monster.hits_attack():
            print(f"{monster.name.title()} attacks!")
            if user.block:
                user.take_damage(monster.get_attack_damage // 2)
                user.block = False
            else:
                user.take_damage(monster.get_attack_damage)
        else:
            print(f"{monster.name.title()} missed its attack!")
    
    #ultimate
    else:
        if monster.hits_attack():
            print(f"{monster.name.title()} uses its ultimate!")
            if user.block:
                user.take_damage(monster.get_attack_damage // 2)
                user.block = False
            else:
                user.take_damage(monster.get_attack_damage)
        else:
            print(f"{monster.name.title()} missed its ultimate!")
    
    user.player_turn = True