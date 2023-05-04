from web3 import Web3

import resources.variables

provider_rpc = {
    "testnet": "https://base-goerli.public.blastapi.io",
}
web3 = Web3(Web3.HTTPProvider(provider_rpc["testnet"]))  # Change to correct network

address_moon = resources.variables.ADDRESS_MOON
address_main = resources.variables.ADDRESS_FIGA

balance_moon = web3.from_wei(web3.eth.get_balance(address_moon), "ether")
balance_main = web3.from_wei(web3.eth.get_balance(address_main), "ether")

print(f"The balance of {address_moon} is: {balance_moon} ETH")
print(f"The balance of {address_main} is: {balance_main} ETH")
