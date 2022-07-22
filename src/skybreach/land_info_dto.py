import coordinates
import enum


class Rarity(enum.Enum):
    NONE = 0
    Common = 1
    Rare = 2
    Epic = 3
    Harb = 4
    Premium = 5


class Entropy(enum.Enum):
    NONE = 0
    Seldom = 1
    Infrequent = 2
    Uncommon = 3
    Common = 4
    Frequent = 5
    Constant = 6


class LandInfo:

    def __init__(self, land_id, land_data):
        self.land_id = land_id
        self.x = coordinates.convert_to_coordinates(land_id)[0]
        self.y = coordinates.convert_to_coordinates(land_id)[1]
        self.cyber = land_data[0]
        self.steampunk = land_data[1]
        self.wind = land_data[2]
        self.volcano = land_data[3]
        self.fire = land_data[4]
        self.water = land_data[5]
        self.necro = land_data[6]
        self.mecha = land_data[7]
        self.dragon = land_data[8]
        self.meadow = land_data[9]
        self.isShore = land_data[10]
        self.isIsland = land_data[11]
        self.isMountainFoot = land_data[12]
        self.rarity = land_data[13]
        self.entropy = land_data[14]
