import resources.variables as variables
from src.skybreach.land_info_dto import Rarity


def define_land_price(land_id: int):
    price = 0.00022
    return price


def skip_lands_in_wallets(land_to_owners):
    return [land_to_owner for land_to_owner in land_to_owners if
            land_to_owner[2] not in [variables.ADDRESS_MOON, variables.ADDRESS_MAIN, variables.ADDRESS_POME]]


def skip_land_types(land_to_owners, land_info_records):
    correct_lands = [land_info for land_info in land_info_records if land_info[13] not in [Rarity.Harb, Rarity.Premium]]
    correct_land_ids = list(map(lambda correct_land: correct_land[0], correct_lands))
    return [land_to_owner for land_to_owner in land_to_owners if
            land_to_owner[1] in correct_land_ids]


def convert_land_to_owner_to_land_ids(land_to_owners):
    return list(map(lambda land_to_owner: land_to_owner[1], land_to_owners))


def define_object_to_make_offer():
    print('init object')
