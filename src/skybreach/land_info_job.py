from web3 import Web3

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
    print(f'Making a call to get land info: {coordinates.convert_to_coordinates(land_id)}')
    contract_skybreach_component = web3.eth.contract(address=Web3.toChecksumAddress(contract_skybreach), abi=abi_skybreach)
    land_info = contract_skybreach_component.functions.getPlotData(land_id).call()
    print(f'Land info: {land_info}')
    return land_info


def process_job():
    for x in range(3, 255):
        lands_to_insert = []
        for y in range(1, 255):
            try:
                land_id = coordinates.convert_to_id(x, y)
                land_info = get_land_info(land_id)
                if land_info[13] > 0:
                    lands_to_insert.append(LandInfo(land_id, *land_info).to_array())
            except Exception as error:
                print(error)
        if len(lands_to_insert) > 0:
            print(f'Lands retrieved for {x} column: {len(lands_to_insert)}')
            db_connection.insert_records(lands_to_insert)

process_job()
