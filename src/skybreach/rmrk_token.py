from web3 import Web3

import resources.variables

providerRpc = {
    "development": "https://rpc.api.moonriver.moonbeam.network/",
    "alphanet": "https://rpc.api.moonbase.moonbeam.network",
}
web3 = Web3(Web3.HTTPProvider(providerRpc["development"]))  # Change to correct network

with open('../abi/rmrk-abi.json', 'r') as file:
    abiRmrk = file.read().replace('\n', '')

contract_address = resources.variables.CONTRACT_ADDRESS_RMRK

contract_rmrk_component = web3.eth.contract(address=Web3.toChecksumAddress(contract_address), abi=abiRmrk)

token_symbol = contract_rmrk_component.functions.symbol().call()
token_decimals = contract_rmrk_component.functions.decimals().call()


def get_balance(address):
    balance = contract_rmrk_component.functions.balanceOf(address).call()
    return balance / pow(10, token_decimals)


def get_symbol():
    return token_symbol
