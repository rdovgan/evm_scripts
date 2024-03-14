from wallet import wallets as w
from utils import generate_random_email_subject, define_random_words


def send_mail_for_each_wallet(web3, contract, contract_address, chain_name):
    wallets_list = w.get_wallets_by_chain(chain_name)
    addresses = list(w.load_wallets(wallets_list).values())

    for current_wallet in addresses:
        # Sender's Ethereum account address and private key
        sender_address = current_wallet[0]
        private_key = current_wallet[1]

        email, subject = generate_random_email_subject(define_random_words())

        tx_receipt = "None"
        if chain_name == 'zksync':
            tx_receipt = send_mail_zksync(web3, contract, contract_address, sender_address, private_key, email, subject)
        print('Email sent successfully:', tx_receipt)


# Function to send email via the DMail contract
def send_mail_zksync(web3, contract, contract_address, sender_address, private_key, email, subject):
    data = contract.encodeABI("send_mail", args=(email, subject))
    tx = {"from": sender_address, "to": contract_address, "data": data, "nonce": web3.eth.get_transaction_count(sender_address), "gasPrice": web3.eth.gas_price}
    tx["gas"] = int(web3.eth.estimate_gas(tx))
    signed_tx = web3.eth.account.sign_transaction(tx, private_key=private_key)
    return web3.eth.wait_for_transaction_receipt(web3.eth.send_raw_transaction(signed_tx.rawTransaction))
