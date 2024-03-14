from web3 import Web3
import json

from wallet import wallets as w
from wallet import rpc

web3 = Web3(Web3.HTTPProvider(rpc.provider['zksync']))
with open('dmail_abi.json', 'r') as f:
    contract_abi = json.load(f)

# Contract address
contract_address = '0x981F198286E40F9979274E0876636E9144B8FB8E'

mail_libra = 'libraxxx@dmail.ai'

# Create contract instance
contract = web3.eth.contract(address=Web3.to_checksum_address(contract_address), abi=contract_abi)


# Function to send email via the DMail contract
def send_mail(to, subject):
    data = contract.encodeABI("send_mail", args=(to, subject))
    tx = {"from": sender_address, "to": contract_address, "data": data, "nonce": web3.eth.get_transaction_count(sender_address), "gasPrice": web3.eth.gas_price}

    tx["gas"] = int(web3.eth.estimate_gas(tx))

    signed_tx = web3.eth.account.sign_transaction(tx, private_key=private_key)

    send_store_contact = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return web3.eth.wait_for_transaction_receipt(send_store_contact)


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
