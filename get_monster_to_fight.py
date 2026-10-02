import random
from player import Player
from monster_creation import monster_rank


def get_monster(user: Player) -> Monster:
    stage = user.stage + 1
    if stage == 1:
        monster = stage_1_monster()
    elif stage == 2:
        monster = stage_2_monster()
    elif stage == 3:
        monster = stage_3_monster()
    elif stage == 4:
        monster = stage_4_monster()
    else:
        raise Exception("How are you higher than 4?")
    return monster


def stage_1_monster() -> Monster:
    monster_gen_number = random.randint(1, 100)
    if monster_gen_number <= 60:
        return random.choice(monster_rank["common"])
    elif monster_gen_number <= 85:
        return random.choice(monster_rank["uncommon"])
    elif monster_gen_number < 96:
        return random.choice(monster_rank["rare"])
    else:
        return random(monster_rank["epic"])
    

def stage_2_monster():
    if monster_gen_number <= 35:
        return random.choice(monster_rank["common"])
    elif monster_gen_number <= 65:
        return random.choice(monster_rank["uncommon"])
    elif monster_gen_number <= 85:
        return random.choice(monster_rank["rare"])
    elif monster_gen_number <= 99:
        return random.choice(monster_rank["epic"])
    else:
        return random.choice(monster_rank["legendary"])

def stage_3_monster():
    if monster_gen_number <= 10:
        return random.choice(monster_rank["common"])
    elif monster_gen_number <= 25:
        return random.choice(monster_rank["uncommon"])
    elif monster_gen_number <= 45:
        return random.choice(monster_rank["rare"])
    elif monster_gen_number <= 89:
        return random.choice(monster_rank["epic"])
    elif monster_gen_number <= 99:
        return random.choice(monster_rank["legendary"])
    else:
        return random.choice(monster_rank["s"])


def stage_4_monster():
    if monster_gen_number <= 2:
        return random.choice(monster_rank["common"])
    elif monster_gen_number <= 4:
        return random.choice(monster_rank["uncommon"])
    elif monster_gen_number <= 15:
        return random.choice(monster_rank["rare"])
    elif monster_gen_number <= 30:
        return random.choice(monster_rank["epic"])
    elif monster_gen_number <= 85:
        return random.choice(monster_rank["legendary"])
    else:
        return random.choice(monster_rank["s"])