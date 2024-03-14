from web3 import Web3
import json

from wallet import wallets as w
from wallet import rpc

web3 = Web3(Web3.HTTPProvider(rpc.provider['base']))
with open('DMail.json', 'r') as f:
    contract_abi = json.load(f)

# Contract address
contract_address = '0x47fbe95e981C0Df9737B6971B451fB15fdC989d9'


# Create contract instance
contract = web3.eth.contract(address=Web3.to_checksum_address(contract_address), abi=contract_abi)


# Function to send email via the DMail contract
def send_mail(to, path):
    tx = {"from": sender_address, "nonce": web3.eth.get_transaction_count(sender_address), "gasPrice": web3.eth.gas_price}

    send_mail_tx = contract.functions.send_mail(to, path).build_transaction(tx)
    signed_tx = web3.eth.account.sign_transaction(send_mail_tx, private_key=private_key)

    send_store_contact = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return web3.eth.wait_for_transaction_receipt(send_store_contact)


wallets_list = w.not_animals | w.wallets_game
addresses = list(w.load_wallets(wallets_list).values())

for current_wallet in addresses:
    # Sender's Ethereum account address and private key
    sender_address = current_wallet[0]
    private_key = current_wallet[1]

    # Example usage
    to = "00da28989ed049cea9855e52b9720d2b7557e829656a2204618dd0581b2bf340"
    path = "05b05178c6500578ffaf67f5b9bf81c1e5ed91943fb7e3df18ccf40d4a1a6ee5"

    tx_receipt = send_mail(to, path)
    print('Email sent successfully:', tx_receipt)