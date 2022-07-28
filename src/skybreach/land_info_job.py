import requests
import json
import db_connection

from service import coordinates_utils
from land_info_job_utils import get_land_info
from land_info_job_utils import get_plots_owners
from land_info_job_utils import split_array
from land_info_job_utils import define_land_to_owner_list
from src.skybreach.land_info_dto import LandInfo
from src.skybreach.land_info_dto import AttributeType


# Job to generate coordinates from (1,1) to (255,255) and retrieve data from blockchain and store to DB
def process_land_import_job():
    land_ids_from_db = [land_from_db[0] for land_from_db in db_connection.read_all_land_info()]
    for x in range(1, 256):
        lands_to_insert = []
        for y in range(1, 256):
            try:
                land_id = coordinates_utils.convert_to_id(x, y)
                if land_id in land_ids_from_db:
                    continue
                land_info = get_land_info(land_id)
                if land_info[13] > 0:
                    print(f'Land info: {land_info}')
                    lands_to_insert.append(LandInfo(land_id, *land_info).to_array())
            except Exception as error:
                print(error)
        if len(lands_to_insert) > 0:
            print(f'Lands retrieved for {x} column: {len(lands_to_insert)}')
            db_connection.insert_all_land_info(lands_to_insert)


# Process job to retrieve lands owners and update connections in DB
def process_land_to_owner_import_job():
    land_ids_from_db = [land_from_db[0] for land_from_db in db_connection.read_all_land_info()]
    splits = split_array(land_ids_from_db, 250)
    for land_split in splits:
        owner_list = get_plots_owners(land_split)
        land_to_owner_list = define_land_to_owner_list(land_split, owner_list)
        db_connection.insert_all_land_to_owner(land_to_owner_list)


# Retrieve Othala Chunkies owners from direct endpoint and store to land_attribute table with type `Othala`
def process_othala_job():
    link = "https://skybreach.app/api/oth"
    othala_data_response = requests.get(link)
    othala_data = []
    for element in json.loads(othala_data_response.text):
        othala_data.append((element['id'], element['owner'], AttributeType.Othala, 1))
    db_connection.insert_all_land_attribute(othala_data)


# Retrieve Gift owners from direct endpoint and store to land_attribute table with type `Gift`
def process_gift_job():
    link = "https://skybreach.app/api/love"
    gift_data_response = requests.get(link)
    gift_data = []
    for element in json.loads(gift_data_response.text):
        gift_data.append((element['id'], element['owner'], AttributeType.Gift, 1))
    db_connection.insert_all_land_attribute(gift_data)

# process_land_import_job()
# process_land_to_owner_import_job()
# process_othala_job()
# process_gift_job()
