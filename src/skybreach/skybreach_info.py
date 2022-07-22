from web3 import Web3

import resources.config
import coordinates
import rmrk_token

providerRpc = {
    "development": "https://rpc.api.moonriver.moonbeam.network/",
    "alphanet": "https://rpc.api.moonbase.moonbeam.network",
}
web3 = Web3(Web3.HTTPProvider(providerRpc["development"]))  # Change to correct network

contract_skybreach = resources.config.CONTRACT_ADDRESS_SKYBREACH

with open('../abi/skybreach-abi.json', 'r') as file:
    abi_skybreach = file.read().replace('\n', '')

address_moon = resources.config.ADDRESS_MOON
address_main = resources.config.ADDRESS_MAIN


def print_balance():
    balance_moon_movr = web3.fromWei(web3.eth.getBalance(address_moon), "ether")
    balance_moon_rmrk = rmrk_token.get_balance(address_moon)
    print(f"The balance of {address_moon} is: {balance_moon_movr} MOVR")
    print(f"The balance of {address_moon} is: {balance_moon_rmrk} {rmrk_token.get_symbol()}")


def call_contract():
    print(f'Making a call to contract at address: {contract_skybreach}')
    contract_skybreach_component = web3.eth.contract(address=Web3.toChecksumAddress(contract_skybreach), abi=abi_skybreach)
    dutch_duration = contract_skybreach_component.functions.getCreatorFee().call()
    print(f'Dutch Duration: {dutch_duration} ')


def get_land_info(land_id: int):
    print(f'Making a call to get land info: {coordinates.convert_to_coordinates(land_id)}')
    contract_skybreach_component = web3.eth.contract(address=Web3.toChecksumAddress(contract_skybreach), abi=abi_skybreach)
    land_info = contract_skybreach_component.functions.getPlotData(land_id).call()
    print(f'Land info: {land_info} ')


get_land_info(coordinates.convert_to_id(143, 133))
get_land_info(coordinates.convert_to_id(144, 133))
get_land_info(coordinates.convert_to_id(145, 133))

