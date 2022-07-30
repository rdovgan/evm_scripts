from web3 import Web3
from web3.gas_strategies.rpc import rpc_gas_price_strategy
from src.skybreach.land_info_dto import Rarity
import resources.variables as variables
import src.skybreach.db_connection as db

providerRpc = {
    "development": "https://rpc.api.moonriver.moonbeam.network/",
    "alphanet": "https://rpc.api.moonbase.moonbeam.network",
}
# Connect to RPC
web3 = Web3(Web3.HTTPProvider(providerRpc["alphanet"]))

account_executor = {
    "private_key": variables.PRIVATE_KEY_GINGER,
    "address": variables.ADDRESS_GINGER,
}

web3.eth.set_gas_price_strategy(rpc_gas_price_strategy)

contract_skybreach = variables.CONTRACT_ADDRESS_SKYBREACH

# Read ABI structure to understand smart contract
with open('../../abi/skybreach-abi.json', 'r') as file:
    abi_skybreach = file.read().replace('\n', '')

# Initialise Smart contract component
contract_skybreach_component = web3.eth.contract(address=Web3.toChecksumAddress(contract_skybreach), abi=abi_skybreach)


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


def define_land_to_owners_to_buy():
    land_to_owners_without_offers = db.read_all_land_to_owner_without_offer()
    land_to_owners_skipped_wallets = skip_lands_in_wallets(land_to_owners_without_offers)
    land_info_records = db.read_all_land_info_by_ids(convert_land_to_owner_to_land_ids(land_to_owners_skipped_wallets))
    land_to_owners_filtered_land_types = skip_land_types(land_to_owners_skipped_wallets, land_info_records)
    return land_to_owners_filtered_land_types
