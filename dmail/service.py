import random
import json
from time import sleep
from web3 import Web3

from utils import generate_random_email_subject, define_random_words

import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from wallet import wallets as w
from wallet import rpc


def send_mail_for_each_wallet(contract_address, chain_name):
    web3 = Web3(Web3.HTTPProvider(rpc.provider[chain_name]))
    script_dir = os.path.dirname(os.path.realpath(__file__))
    with open(script_dir + "/" + 'dmail_abi.json', 'r') as f:
        contract_abi = json.load(f)

    # Create contract instance
    contract = web3.eth.contract(address=Web3.to_checksum_address(contract_address), abi=contract_abi)

    wallets_list = w.get_wallets_by_chain(chain_name)
    addresses = list(w.load_wallets(wallets_list).values())

    sleep(random.randint(1, 1080))  # up to 3 hours
    for current_wallet in addresses:
        sleep(random.randint(10, 600))  # up to 10 minutes

        # Sender's Ethereum account address and private key
        sender_address = current_wallet[0]
        private_key = current_wallet[1]

        email, subject = generate_random_email_subject(define_random_words())

        tx_receipt = "None"
        if chain_name == 'zksync':
            tx_receipt = send_mail_zksync(web3, contract, contract_address, sender_address, private_key, email, subject)
        elif chain_name == 'linea':
            tx_receipt = send_mail_linea(web3, contract, contract_address, sender_address, private_key, email, subject)
        elif chain_name == 'base':
            tx_receipt = send_mail_base(web3, contract, contract_address, sender_address, private_key, email, subject)
        print('Email sent successfully:', tx_receipt)


# Function to send email via the DMail contract
def send_mail_zksync(web3, contract, contract_address, sender_address, private_key, email, subject):
    data = contract.encodeABI("send_mail", args=(email, subject))
    tx = {"from": sender_address, "to": contract_address, "data": data, "nonce": web3.eth.get_transaction_count(sender_address), "gasPrice": web3.eth.gas_price}
    tx["gas"] = int(web3.eth.estimate_gas(tx))
    signed_tx = web3.eth.account.sign_transaction(tx, private_key=private_key)

    return web3.eth.wait_for_transaction_receipt(web3.eth.send_raw_transaction(signed_tx.rawTransaction))


def send_mail_linea(web3, contract, contract_address, sender_address, private_key, email, subject):
    hex_email, hex_subject = email.encode('utf-8').hex(), subject.encode('utf-8').hex()
    tx = {"from": sender_address, "nonce": web3.eth.get_transaction_count(sender_address),
          'maxPriorityFeePerGas': web3.eth.max_priority_fee,
          'maxFeePerGas': int(web3.eth.max_priority_fee * 1.1)}

    send_mail_tx = contract.functions.send_mail(hex_email, hex_subject).build_transaction(tx)
    signed_tx = web3.eth.account.sign_transaction(send_mail_tx, private_key)

    return web3.eth.wait_for_transaction_receipt(web3.eth.send_raw_transaction(signed_tx.rawTransaction))


def send_mail_base(web3, contract, contract_address, sender_address, private_key, email, subject):
    hex_email, hex_subject = email.encode('utf-8').hex(), subject.encode('utf-8').hex()
    tx = {"from": sender_address, "nonce": web3.eth.get_transaction_count(sender_address), "gasPrice": web3.eth.gas_price}

    send_mail_tx = contract.functions.send_mail(hex_email, hex_subject).build_transaction(tx)
    signed_tx = web3.eth.account.sign_transaction(send_mail_tx, private_key=private_key)

    return web3.eth.wait_for_transaction_receipt(web3.eth.send_raw_transaction(signed_tx.rawTransaction))
