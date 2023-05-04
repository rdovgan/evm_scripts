from web3 import Web3

import resources.variables

provider_rpc = {
    "development": "https://rpc.api.moonriver.moonbeam.network/",
    "alphanet": "https://rpc.api.moonbase.moonbeam.network",
}
web3 = Web3(Web3.HTTPProvider(provider_rpc["development"]))  # Change to correct network

address_moon = resources.variables.ADDRESS_MOON
address_main = resources.variables.ADDRESS_FIGA

balance_moon = web3.fromWei(web3.eth.getBalance(address_moon), "ether")
balance_main = web3.fromWei(web3.eth.getBalance(address_main), "ether")

print(f"The balance of {address_moon} is: {balance_moon} MOVR")
print(f"The balance of {address_main} is: {balance_main} MOVR")
