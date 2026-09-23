from monster import Monster

monster_rank: dict[str: [Monster]] = {"common": [
                                            Monster(name="goblin", rank=Rank.COMMON, stats=MonsterStats(attack_damage=45, accuracy=65, hp=65, speed=54, defense=40)),
                                            Monster(name="goblin archer", rank=Rank.COMMON, stats=MonsterStats(attack_damage=45, accuracy=65, hp=65, speed=54, defense=40)),
                                            Monster(name="goblin theif", rank=Rank.COMMON, stats=MonsterStats(attack_damage=50, accuracy=65, hp=50, speed=75, defense=40)),
                                            Monster(name="goblin mage", rank=Rank.COMMON, stats=MonsterStats(attack_damage=55, accuracy=65, hp=65, speed=40, defense=40)),
                                            Monster(name="wolf", rank=Rank.COMMON, stats=MonsterStats(attack_damage=60, accuracy=65, hp=60, speed=75, defense=40)),
                                            Monster(name="rabbit", rank=Rank.COMMON, stats=MonsterStats(attack_damage=5, accuracy=100, hp=50, speed=100, defense=25)),
                                        ],
                                        "uncommon": [
                                            Monster(name="giant slime", rank=Rank.UNCOMMON, stats=MonsterStats(attack_damage=55, accuracy=70, hp=75, speed=50, defense=50)),
                                            Monster(name="goblin warrior", rank=Rank.UNCOMMON, stats=MonsterStats(attack_damage=55, accuracy=70, hp=70, speed=55, defense=50)),
                                            Monster(name="goblin assassin", rank=Rank.UNCOMMON, stats=MonsterStats(attack_damage=60, accuracy=70, hp=50, speed=75, defense=50)),
                                            Monster(name="goblin summoner", rank=Rank.UNCOMMON, stats=MonsterStats(attack_damage=65, accuracy=700, hp=65, speed=40, defense=50)),
                                            Monster(name="dire wolf", rank=Rank.UNCOMMON, stats=MonsterStats(attack_damage=65, accuracy=70, hp=60, speed=75, defense=50)),
                                        ],
                                        "rare": [
                                            Monster(name="Mimic", rank=Rank.RARE, stats=MonsterStats(attack_damage=58, accuracy=75, hp=85, speed=54, defense=60)),
                                            Monster(name="goblin king", rank=Rank.RARE, stats=MonsterStats(attack_damage=65, accuracy=75, hp=90, speed=63, defense=80)),
                                            Monster(name="gargoyle", rank=Rank.RARE, stats=MonsterStats(attack_damage=60, accuracy=75, hp=95, speed=40, defense=70)),
                                            Monster(name="pixie", rank=Rank.RARE, stats=MonsterStats(attack_damage=56, accuracy=75, hp=65, speed=68, defense=57)),
                                            Monster(name="giant wolf", rank=Rank.RARE, stats=MonsterStats(attack_damage=60, accuracy=75, hp=80, speed=75, defense=60)),
                                        ],
                                        "epic": [
                                            Monster(name="Imp", rank=Rank.EPIC, stats=MonsterStats(attack_damage=65, accuracy=90, hp=65, speed=80, defense=65)),
                                            Monster(name="Harpy", rank=Rank.EPIC, stats=MonsterStats(attack_damage=80, accuracy=80, hp=65, speed=80, defense=65)),
                                            Monster(name="Fae Quen", rank=Rank.EPIC, stats=MonsterStats(attack_damage=80, accuracy=80, hp=50, speed=80, defense=65)),
                                            Monster(name="Emperor slime", rank=Rank.EPIC, stats=MonsterStats(attack_damage=65, accuracy=80, hp=120, speed=60, defense=80)),
                                            Monster(name="Shadow Wolf", rank=Rank.EPIC, stats=MonsterStats(attack_damage=72, accuracy=80, hp=90, speed=75, defense=70)),
                                        ],
                                        "legendary": [
                                            Monster(name="Peonix", rank=Rank.LEGENDARY, stats=MonsterStats(attack_damage=95, accuracy=90, hp=150, speed=95, defense=90)),
                                            Monster(name="Succubus", rank=Rank.LEGENDARY, stats=MonsterStats(attack_damage=100, accuracy=90, hp=100, speed=90, defense=90)),
                                            Monster(name="Wyvern", rank=Rank.LEGENDARY, stats=MonsterStats(attack_damage=90, accuracy=90, hp=200, speed=85, defense=90)),
                                        ],
                                        "s": [
                                            Monster(name="Dragon", rank=Rank.SRANK, stats=MonsterStats(attack_damage=130, accuracy=95, hp=250, speed=100, defense=110)),
                                            Monster(name="Fenrir", rank=Rank.SRANK, stats=MonsterStats(attack_damage=135, accuracy=95, hp=180, speed=150, defense=100)),
                                            Monster(name="Demon King", rank=Rank.SRANK, stats=MonsterStats(attack_damage=150, accuracy=95, hp=100, speed=125, defense=100)),
                                        ]
                                        }