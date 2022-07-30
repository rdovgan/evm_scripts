import src.skybreach.utils.offer_service as service
import src.skybreach.db_connection as db


def process_job_to_make_offers():
    land_to_owners_without_offers = db.read_all_land_to_owner_without_offer()
    land_to_owners_skipped_wallets = service.skip_lands_in_wallets(land_to_owners_without_offers)
    land_info_records = db.read_all_land_info_by_ids(service.convert_land_to_owner_to_land_ids(land_to_owners_skipped_wallets))
    land_to_owners_filtered_land_types = service.skip_land_types(land_to_owners_skipped_wallets, land_info_records)

    land_to_owners_to_update = []
    try:
        for land_to_owner in land_to_owners_filtered_land_types:
            price = service.define_land_price(land_to_owner[1])
            # make offer
            land_to_owners_to_update.append((land_to_owner[0], land_to_owner[1], land_to_owner[2], price, land_to_owner[4]))
    finally:
        print(len(land_to_owners_to_update))
        # insert_all_land_to_owner(land_to_owners_to_update)


process_job_to_make_offers()
