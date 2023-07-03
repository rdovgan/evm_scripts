import json
import os

from hexbytes import HexBytes
from solcx import compile_standard, install_solc

from db import db_connection as db


def define_contract(web3, wallet_address, contract_name):
    compiled_contract_file = "result/" + wallet_address[2:7] + ":" + contract_name + ".json"
    contract_filename = contract_name + ".sol"

    script_dir = os.path.dirname(os.path.realpath(__file__))
    if os.path.isfile(compiled_contract_file):
        with open(script_dir + "/" + compiled_contract_file, "r") as file:
            compiled_sol = json.load(file)
    else:
        compiled_sol = generate_contract_compilation(contract_name)
        with open(script_dir + "/" + compiled_contract_file, "w") as file:
            json.dump(compiled_sol, file)
    # get bytecode
    bytecode = compiled_sol["contracts"][contract_filename][contract_name]["evm"]["bytecode"]["object"]
    # get abi
    abi = json.loads(compiled_sol["contracts"][contract_filename][contract_name]["metadata"])["output"]["abi"]
    # Create the contract in Python
    return web3.eth.contract(abi=abi, bytecode=bytecode)


def generate_contract_compilation(contract_name):
    contract_filename = contract_name + ".sol"
    install_solc('0.8.0')
    script_dir = os.path.dirname(os.path.realpath(__file__))
    with open(script_dir + "/solidity/" + contract_filename, "r") as file:
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
    return compiled_sol


def deploy_contract(contract_object, web3, wallet_address, private_key, contract_name):
    # check if contract was deployed before
    contract_data = db.read_contract(wallet_address, contract_name)
    if contract_data is not None:
        return contract_data[2]

    # build transaction
    transaction = contract_object.constructor().build_transaction(
        {
            "gasPrice": web3.eth.gas_price,
            "from": wallet_address,
            "nonce": web3.eth.get_transaction_count(wallet_address),
        }
    )
    # Sign the transaction
    sign_transaction = web3.eth.account.sign_transaction(transaction, private_key=private_key)
    # Send the transaction
    print("Deploying Contract!")
    transaction_hash = web3.eth.send_raw_transaction(sign_transaction.rawTransaction)
    # Wait for the transaction to be mined, and get the transaction receipt
    print("Waiting for transaction to finish...")
    transaction_contract_address = web3.eth.wait_for_transaction_receipt(transaction_hash).contractAddress
    print(f"Done! Contract deployed to {transaction_contract_address}")
    db.insert_contract((wallet_address, contract_name, transaction_contract_address))
    return db.read_contract(wallet_address, contract_name)[2]


def call_make_gold(contract_object, web3, wallet_address, private_key, contract_address, gas_price=None):
    if gas_price is None:
        transaction = {"from": wallet_address, "to": contract_address, "nonce": web3.eth.get_transaction_count(wallet_address)}
    else:
        transaction = {"from": wallet_address, "to": contract_address, "nonce": web3.eth.get_transaction_count(wallet_address), "gasPrice": gas_price}
    make_gold = contract_object.functions.makeGold().build_transaction(transaction)
    # Sign the transaction
    sign_store_contact = web3.eth.account.sign_transaction(
        make_gold, private_key=private_key
    )
    # Send the transaction
    send_store_contact = web3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
    transaction_receipt = web3.eth.wait_for_transaction_receipt(send_store_contact)
    print(f"Submitted contract method execution {HexBytes.hex(transaction_receipt.transactionHash)}")
