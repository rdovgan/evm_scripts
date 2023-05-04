import json
from web3 import Web3
from solcx import compile_standard, install_solc

import resources.variables

provider_rpc = {
    "testnet": "https://base-goerli.public.blastapi.io",
}
web3 = Web3(Web3.HTTPProvider(provider_rpc["testnet"]))

filename = "GoldOwner.sol"

address_ginger = resources.variables.ADDRESS_MOON
private_ginger = resources.variables.PRIVATE_KEY_GINGER

balance_ginger = web3.from_wei(web3.eth.get_balance(address_ginger), "ether")

print(f"The balance of {address_ginger} is: {balance_ginger} ETH")

install_solc('0.8.0')

with open(filename, "r") as file:
    gold_owner_file = file.read()

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {filename: {"content": gold_owner_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version="0.8.0",
)
print(compiled_sol)
with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)