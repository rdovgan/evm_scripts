import src.skybreach.utils.offer_service as service
import src.skybreach.db_connection as db
import time
from src.skybreach.utils import coordinates_utils


def process_job_to_make_offers():
    land_to_owners_filtered_land_types = service.define_land_to_owners_to_buy()

    land_to_owners_to_update = []
    try:
        for land_to_owner in land_to_owners_filtered_land_types:
            price = service.define_land_price(land_to_owner[0])
            try:
                if not service.is_active_order(land_to_owner[0]):
                    print(f'Offer for {land_to_owner[0]} {coordinates_utils.convert_to_coordinates(land_to_owner[0])}')
                    service.make_buy_offer(land_to_owner[0])
                land_to_owners_to_update.append((land_to_owner[0], land_to_owner[1], price))
            except Exception as exception:
                print(f'{exception} Timeout for land {land_to_owner[0]}')
                time.sleep(60)

    finally:
        print(len(land_to_owners_to_update))
        db.insert_all_land_to_owner(land_to_owners_to_update)
