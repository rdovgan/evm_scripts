from pathlib import Path

from web3 import Web3
from web3.gas_strategies.rpc import rpc_gas_price_strategy
# TODO need to refactor this
import resources.variables as variables
import skybreach.db_connection as db
from skybreach.land_info_dto import Rarity
from skybreach.rmrk_token import token_decimals

providerRpc = {
    "development": "https://rpc.api.moonriver.moonbeam.network/",
    "alphanet": "https://rpc.api.moonbase.moonbeam.network",
}
# Connect to RPC
web3 = Web3(Web3.HTTPProvider(providerRpc["development"]))

account_executor = {
    "private_key": variables.PRIVATE_KEY_GINGER,
    "address": variables.ADDRESS_GINGER,
}

web3.eth.set_gas_price_strategy(rpc_gas_price_strategy)

contract_skybreach = variables.CONTRACT_ADDRESS_SKYBREACH

# Read ABI structure to understand smart contract
with open(Path(__file__).parent / '../../abi/skybreach-abi.json', 'r') as file:
    abi_skybreach = file.read().replace('\n', '')

# Initialise Smart contract component
contract_skybreach_component = web3.eth.contract(address=Web3.toChecksumAddress(contract_skybreach), abi=abi_skybreach)


def define_land_price(land_id: int):
    price = pow(10, token_decimals - 5) * 22
    return int(price)


def make_buy_offer(land_id: int):
    buy_offer = contract_skybreach_component.functions.makeOffer(land_id, define_land_price(land_id)).buildTransaction(
        {
            'from': account_executor['address'],
            'nonce': web3.eth.get_transaction_count(account_executor['address']),
        }
    )
    tx_buy_offer = web3.eth.account.sign_transaction(buy_offer, account_executor['private_key'])
    tx_hash = web3.eth.send_raw_transaction(tx_buy_offer.rawTransaction)
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_receipt


def skip_lands_in_wallets(land_to_owners):
    return [land_to_owner for land_to_owner in land_to_owners if
            land_to_owner[1] not in [variables.ADDRESS_MOON, variables.ADDRESS_FIGA, variables.ADDRESS_PAPAYA, variables.ADDRESS_GINGER]]


def skip_land_types(land_to_owners, land_info_records):
    correct_lands = [land_info for land_info in land_info_records if land_info[13] not in [Rarity.Harb.value, Rarity.Premium.value]]
    correct_land_ids = list(map(lambda correct_land: correct_land[0], correct_lands))
    return [land_to_owner for land_to_owner in land_to_owners if
            land_to_owner[0] in correct_land_ids]


def convert_land_to_owner_to_land_ids(land_to_owners):
    return list(map(lambda land_to_owner: land_to_owner[0], land_to_owners))


def define_land_to_owners_to_buy():
    land_to_owners_without_offers = db.read_all_land_to_owner_without_offer()
    land_to_owners_skipped_wallets = skip_lands_in_wallets(land_to_owners_without_offers)
    land_info_records = db.read_all_land_info_by_ids(convert_land_to_owner_to_land_ids(land_to_owners_skipped_wallets))
    land_to_owners_filtered_land_types = skip_land_types(land_to_owners_skipped_wallets, land_info_records)
    return land_to_owners_filtered_land_types


def define_land_offers(land_id: int):
    return contract_skybreach_component.functions.getOffers(land_id).call()


def is_active_order(land_id):
    return variables.ADDRESS_GINGER in list(map(lambda offer:  offer[0], define_land_offers(land_id)))
