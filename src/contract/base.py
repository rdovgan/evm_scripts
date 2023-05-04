import json
from web3 import Web3
from solcx import compile_standard, install_solc

import resources.variables

provider_rpc = {
    "testnet": "https://base-goerli.public.blastapi.io",
}
web3 = Web3(Web3.HTTPProvider(provider_rpc["testnet"]))

wallet_address = resources.variables.ADDRESS_GINGER
private_key = resources.variables.PRIVATE_KEY_GINGER


def define_contract():
    contract_name = "GoldOwner"
    contract_filename = "GoldOwner.sol"
    balance_ginger = web3.from_wei(web3.eth.get_balance(wallet_address), "ether")
    print(f"The balance of {wallet_address} is: {balance_ginger} ETH")
    install_solc('0.8.0')
    with open(contract_filename, "r") as file:
        gold_owner_file = file.read()
    compiled_sol = compile_standard(
        {
            "language": "Solidity",
            "sources": {contract_filename: {"content": gold_owner_file}},
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
    compiled_contract_file = wallet_address[0:5] + "()" + wallet_address[-3:] + "-" + "compiled_code.json"
    print(compiled_sol)
    with open(compiled_contract_file, "w") as file:
        json.dump(compiled_sol, file)
    # get bytecode
    bytecode = compiled_sol["contracts"][contract_filename][contract_name]["evm"]["bytecode"]["object"]
    # get abi
    abi = json.loads(compiled_sol["contracts"][contract_filename][contract_name]["metadata"])["output"]["abi"]
    # Create the contract in Python
    return web3.eth.contract(abi=abi, bytecode=bytecode)


GoldOwnerContract = define_contract()
# Get the number of the latest transaction
nonce = web3.eth.get_transaction_count(wallet_address)

# build transaction
transaction = GoldOwnerContract.constructor().build_transaction(
    {
        "gasPrice": web3.eth.gas_price,
        "from": wallet_address,
        "nonce": nonce,
    }
)
# Sign the transaction
sign_transaction = web3.eth.account.sign_transaction(transaction, private_key=private_key)

# Send the transaction
print("Deploying Contract!")
transaction_hash = web3.eth.send_raw_transaction(sign_transaction.rawTransaction)

# Wait for the transaction to be mined, and get the transaction receipt
print("Waiting for transaction to finish...")
transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction_hash)
print(f"Done! Contract deployed to {transaction_receipt.contractAddress}")

