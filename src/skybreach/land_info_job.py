from web3 import Web3

import requests
import resources.variables
import coordinates
import db_connection
from src.skybreach.land_info_dto import LandInfo

providerRpc = {
    "development": "https://rpc.api.moonriver.moonbeam.network/",
    "alphanet": "https://rpc.api.moonbase.moonbeam.network",
}
web3 = Web3(Web3.HTTPProvider(providerRpc["development"]))

contract_skybreach = resources.variables.CONTRACT_ADDRESS_SKYBREACH

with open('../abi/skybreach-abi.json', 'r') as file:
    abi_skybreach = file.read().replace('\n', '')


def get_land_info(land_id: int):
    contract_skybreach_component = web3.eth.contract(address=Web3.toChecksumAddress(contract_skybreach), abi=abi_skybreach)
    land_info = contract_skybreach_component.functions.getPlotData(land_id).call()
    return land_info


def process_job():
    land_ids_from_db = [land_from_db[0] for land_from_db in db_connection.read_all()]
    for x in range(50, 256):
        lands_to_insert = []
        for y in range(1, 256):
            try:
                land_id = coordinates.convert_to_id(x, y)
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
            db_connection.insert_records(lands_to_insert)


def process_othala_job():
    link = "https://skybreach.app/api/oth"
    othala_data_response = requests.get(link)
    print(othala_data_response.text)



process_othala_job()
