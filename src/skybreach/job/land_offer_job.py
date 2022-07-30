from src.skybreach.service.offer_service import define_land_price
from src.skybreach.db_connection import read_all_land_to_owner_without_offer
from src.skybreach.db_connection import insert_all_land_to_owner


def process_job_to_make_offers():
    land_to_owners_without_offers = read_all_land_to_owner_without_offer()
    land_to_owners_to_update = []
    try:
        for land_to_owner in land_to_owners_without_offers:
            land_to_owner['price'] = define_land_price(land_to_owner['land_id'])
            # make offer
            land_to_owners_to_update.append(land_to_owner)
    finally:
        insert_all_land_to_owner(land_to_owners_to_update)


process_job_to_make_offers()
