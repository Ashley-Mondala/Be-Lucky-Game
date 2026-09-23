from rank import Rank

class StatsUpgrades:
    def __init__(self, rank: Rank, stat_type:str, buff_amount:int):
        self.rank = rank
        self.type = stat_type
        self.buff_amount = amount
    
    def upgrade_detail(self):
        match self.rank:
            case Rank.COMMON:
                print(f"--- Good Luck ---\n~ {self.rank.title()} ~\n{self.stat_type}: +{buff_amount}")
            
            case Rank.UNCOMMON:
                print(f"--- Ok ---\n~ {self.rank.title()} ~\n{self.stat_type}: +{buff_amount}")
    
            case Rank.RARE:
                print(f"--- Not Bad ---\n~ {self.rank.title()} ~\n{self.stat_type}: +{buff_amount}")
            
            case Rank.EPIC:
                print(f"--- Nice ---\n~ {self.rank.title()} ~\n{self.stat_type}: +{buff_amount}")
            
            case Rank.LEGENDARY:
                print(f"--- YIPPEE ---\n~ {self.rank.title()} ~\n{self.stat_type}: +{buff_amount}")
            
            case Rank.SRANK:
                print(f"--- SHEEEEESHHHH ---\n~ {self.rank.title()} ~\n{self.stat_type}: +{buff_amount}")

            case _:
                raise Exception("Not a valid rank.")