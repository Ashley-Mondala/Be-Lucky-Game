from enum import Enum

class Rank(Enum):
    COMMON = "common"
    UNCOMMON = "uncommon"
    RARE = "rare"
    EPIC = "epic"
    LEGENDARY = "legendary"
    SRANK = "s"

    def __str__(self):
        return self.value
