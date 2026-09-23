from stats_upgrade import StatsUpgrades

upgrades_rarity: dict[str: [StatsUpgrades]] = {"common": [
                                            StatsUpgrades(rank = Rank.COMMON, stat_type = "Attack Damage Boost", buff_amount = 5),
                                            StatsUpgrades(rank = Rank.COMMON, stat_type = "Accuracy Boost", buff_amount = 2),
                                            StatsUpgrades(rank = Rank.COMMON, stat_type = "HP Boost", buff_amount = 15)
                                            StatsUpgrades(rank = Rank.COMMON, stat_type = "Speed Boost", buff_amount = 2),
                                            StatsUpgrades(rank = Rank.COMMON, stat_type = "Defense Boost", buff_amount = 10)
                                        ],
                                        "uncommon": [
                                            StatsUpgrades(rank = Rank.UNCOMMON, stat_type = "Attack Damage Boost", buff_amount = 10),
                                            StatsUpgrades(rank = Rank.UNCOMMON, stat_type = "Accuracy Boost", buff_amount = 5),
                                            StatsUpgrades(rank = Rank.UNCOMMON, stat_type = "HP Boost", buff_amount = 20),
                                            StatsUpgrades(rank = Rank.UNCOMMON, stat_type = "Speed Boost", buff_amount = 10),
                                            StatsUpgrades(rank = Rank.UNCOMMON, stat_type = "Defense Boost", buff_amount = 15)
                                        ],
                                        "rare": [
                                            StatsUpgrades(rank = Rank.RARE, stat_type = "Attack Damage Boost", buff_amount = 15),
                                            StatsUpgrades(rank = Rank.RARE, stat_type = "Accuracy Boost", buff_amount = 10),
                                            StatsUpgrades(rank = Rank.RARE, stat_type = "HP Boost", buff_amount = 25),
                                            StatsUpgrades(rank = Rank.RARE, stat_type = "Speed Boost", buff_amount = 20),
                                            StatsUpgrades(rank = Rank.RARE, stat_type = "Defense Boost", buff_amount = 25)
                                        ],
                                        "epic": [
                                            StatsUpgrades(rank = Rank.EPIC, stat_type = "Attack Damage Boost", buff_amount = 25),
                                            StatsUpgrades(rank = Rank.EPIC, stat_type = "Accuracy Boost", buff_amount = 15),
                                            StatsUpgrades(rank = Rank.EPIC, stat_type = "HP Boost", buff_amount = 50),
                                            StatsUpgrades(rank = Rank.EPIC, stat_type = "Speed Boost", buff_amount = 40),
                                            StatsUpgrades(rank = Rank.EPIC, stat_type = "Defense Boost", buff_amount = 50)
                                        ],
                                        "legendary": [
                                            StatsUpgrades(rank = Rank.LEGENDARY, stat_type = "Attack Damage Boost", buff_amount = 50),
                                            StatsUpgrades(rank = Rank.LEGENDARY, stat_type = "Accuracy Boost", buff_amount = 25),
                                            StatsUpgrades(rank = Rank.LEGENDARY, stat_type = "HP Boost", buff_amount = 75),
                                            StatsUpgrades(rank = Rank.LEGENDARY, stat_type = "Defense Boost", buff_amount = 100)
                                        ],
                                        "s": [
                                            StatsUpgrades(rank = Rank.LEGENDARY, stat_type = "Attack Damage Boost", buff_amount = 150),
                                            StatsUpgrades(rank = Rank.LEGENDARY, stat_type = "HP Boost", buff_amount = 180),
                                            StatsUpgrades(rank = Rank.LEGENDARY, stat_type = "Defense Boost", buff_amount = 200)
                                        ]
                                        }