from web3 import Web3

import resources.config

provider_rpc = {
    "development": "https://rpc.api.moonriver.moonbeam.network/",
    "alphanet": "https://rpc.api.moonbase.moonbeam.network",
}
web3 = Web3(Web3.HTTPProvider(provider_rpc["development"]))  # Change to correct network

address_moon = resources.config.ADDRESS_MOON
address_figa = resources.config.ADDRESS_MAIN

balance_from = web3.fromWei(web3.eth.getBalance(address_moon), "ether")
balance_to = web3.fromWei(web3.eth.getBalance(address_figa), "ether")

print(f"The balance of {address_moon} is: {balance_from} MOVR")
print(f"The balance of {address_figa} is: {balance_to} MOVR")
