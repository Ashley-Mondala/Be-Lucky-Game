
# {ranks: [attack_buff_amt, accuracy_buff_amt, health_restor_amt, defense_buff_amt]}
monster_rank_buffs: dict[str: [int]] = {"common":[5, 3, 10, 5],
                                        "uncommon": [10, 6, 15, 10],
                                        "rare": [15, 8, 20, 15],
                                        "epic": [25, 12, 40, 30]
                                        "legendary": [40, 16, 50, 40],
                                        "s": [60, 20, 80, 80]
                                        }