import enum


class Rarity(enum.Enum):
    NONE = 0
    Common = 1  # 16000
    Rare = 2  # 5000
    Epic = 3  # 1000
    Harb = 4  # 2500
    Premium = 5  # 500


class Entropy(enum.Enum):
    NONE = 0
    Seldom = 1  # 7962
    Infrequent = 2  # 6891
    Uncommon = 3  # 4511
    Common = 4  # 2201
    Frequent = 5  # 2201
    Constant = 6  # 2500


class AttributeType(enum.Enum):
    Othala = 'Othala',
    Gift = 'Gift'


class LandInfo:

    def __init__(self, land_id, *land_data):
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

    def to_array(self):
        return self.land_id, self.x, self.y, self.cyber, self.steampunk, self.wind, self.volcano, self.fire, self.water, self.necro, self.mecha, self.dragon, \
               self.meadow, self.isShore, self.isIsland, self.isMountainFoot, self.rarity, self.entropy
