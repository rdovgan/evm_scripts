from web3 import Web3
import json

from wallet import wallets as w
from wallet import rpc

web3 = Web3(Web3.HTTPProvider(rpc.provider['linea']))
with open('DMail.json', 'r') as f:
    contract_abi = json.load(f)

# Contract address
contract_address = '0xd1a3abf42f9e66be86cfdea8c5c2c74f041c5e14'

mail_libra = 'libraxxx@dmail.ai'

# Create contract instance
contract = web3.eth.contract(address=Web3.to_checksum_address(contract_address), abi=contract_abi)


# Function to send email via the DMail contract
def send_mail(to, subject):
    hex_email = to.encode('utf-8').hex()
    hex_subject = subject.encode('utf-8').hex()

    tx = {"from": sender_address, "nonce": web3.eth.get_transaction_count(sender_address),
          'maxPriorityFeePerGas': web3.eth.max_priority_fee,
          'maxFeePerGas': int(web3.eth.max_priority_fee * 1.1)}

    built_transaction = contract.functions.send_mail(hex_email, hex_subject).build_transaction(tx)

    signed_txn = web3.eth.account.sign_transaction(built_transaction, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return web3.eth.wait_for_transaction_receipt(tx_hash)


wallets_list = w.not_animals | w.wallets_game
addresses = list(w.load_wallets(wallets_list).values())

for current_wallet in addresses:
    # Sender's Ethereum account address and private key
    sender_address = current_wallet[0]
    private_key = current_wallet[1]

    # Example usage
    to = mail_libra
    subject = 'It\'s alive!'

    tx_receipt = send_mail(to, subject)
    print('Email sent successfully:', tx_receipt)
