from web3 import Web3

import resources.variables
import coordinates_utils
from src.skybreach import rmrk_token

providerRpc = {
    "development": "https://rpc.api.moonriver.moonbeam.network/",
    "alphanet": "https://rpc.api.moonbase.moonbeam.network",
}
web3 = Web3(Web3.HTTPProvider(providerRpc["development"]))  # Change to correct network

with open('../../abi/skybreach-abi.json', 'r') as file:
    abi_skybreach = file.read().replace('\n', '')

address_moon = resources.variables.ADDRESS_MOON
address_main = resources.variables.ADDRESS_FIGA

contract_skybreach = resources.variables.CONTRACT_ADDRESS_SKYBREACH
contract_skybreach_component = web3.eth.contract(address=Web3.toChecksumAddress(contract_skybreach), abi=abi_skybreach)


def print_balance():
    balance_moon_movr = web3.fromWei(web3.eth.getBalance(address_moon), "ether")
    print(f"The balance of {address_moon} is: {balance_moon_movr} MOVR")
    balance_moon_rmrk = rmrk_token.get_balance(address_moon)
    print(f"The balance of {address_moon} is: {balance_moon_rmrk} {rmrk_token.get_symbol()}")


def call_contract_test():
    print(f'Making a call to contract at address: {contract_skybreach}')
    creator_fee = contract_skybreach_component.functions.getCreatorFee().call()
    print(f'Creator fee: {creator_fee} ')


def get_land_info(land_id: int):
    print(f'Making a call to get land info: {coordinates_utils.convert_to_coordinates(land_id)}')
    land_info = contract_skybreach_component.functions.getPlotData(land_id).call()
    print(f'Land info: {land_info} ')


def get_land_types_by_address(address: str):
    print(f'Making a call to get lands by address {address}')
    return contract_skybreach_component.functions.getOwnedPlotRarities(address).call()


def get_lands_by_address(address: str):
    print(f'Making a call to get lands by address {address}')
    return contract_skybreach_component.functions.getOwnerPlots(address).call()


def get_resources_by_id(land_id: int):
    print(f'Making a call to get resources by land {land_id}')
    return contract_skybreach_component.functions.getPlotResource(land_id).call()


def get_bought_lands():
    return []

