import random

import contract_service as service
import db_connection as db

from time import sleep
from hexbytes import HexBytes
from web3 import Web3
from web3.middleware import geth_poa_middleware

from wallet import wallets as w

# wait up to 20 minutes
delay = random.randint(1, 20) * 60
sleep(delay)

provider_rpc = {
    "mainnet": "https://scroll-alphanet.public.blastapi.io",
}
web3 = Web3(Web3.HTTPProvider(provider_rpc["mainnet"]))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

addresses = [(w.ADDRESS_BANANA, w.PRIVATE_KEY_BANANA), (w.ADDRESS_MANGO, w.PRIVATE_KEY_MANGO), (w.ADDRESS_GINGER, w.PRIVATE_KEY_GINGER),
             (w.ADDRESS_GUAVA, w.PRIVATE_KEY_GUAVA),
             (w.ADDRESS_MERCURY, w.PRIVATE_KEY_MERCURY), (w.ADDRESS_VENUS, w.PRIVATE_KEY_VENUS), (w.ADDRESS_MARS, w.PRIVATE_KEY_MARS),
             (w.ADDRESS_JUPITER, w.PRIVATE_KEY_JUPITER), (w.ADDRESS_SATURN, w.PRIVATE_KEY_SATURN), (w.ADDRESS_URANUS, w.PRIVATE_KEY_URANUS),
             (w.ADDRESS_NEPTUNE, w.PRIVATE_KEY_NEPTUNE), (w.ADDRESS_SIRIUS, w.PRIVATE_KEY_SIRIUS), (w.ADDRESS_POLARIS, w.PRIVATE_KEY_POLARIS),
             (w.ADDRESS_ANTARES, w.PRIVATE_KEY_ANTARES), (w.ADDRESS_LIBRA, w.PRIVATE_KEY_LIBRA), (w.ADDRESS_AQUARIUS, w.PRIVATE_KEY_AQUARIUS)]

contract_name = "GoldScroll"

random_wallet = random.choice(addresses)

wallet_address = random_wallet[0]
private_key = random_wallet[1]

balance = web3.from_wei(web3.eth.get_balance(wallet_address), "ether")
print(f"The balance of {wallet_address} is: {balance} ETH")

gold_counter_contract = service.define_contract(web3, wallet_address, contract_name)
contract_address = service.deploy_contract(gold_counter_contract, web3, wallet_address, private_key, contract_name)


def call_make_gold(contract_object, web3, wallet_address, private_key, contract_address):
    custom_gas_price = web3.to_wei(150, "gwei")
    make_gold = contract_object.functions.makeGold().build_transaction(
        {"from": wallet_address, "to": contract_address, "nonce": web3.eth.get_transaction_count(wallet_address), "gasPrice": custom_gas_price})
    # Sign the transaction
    sign_store_contact = web3.eth.account.sign_transaction(
        make_gold, private_key=private_key
    )
    # Send the transaction
    send_store_contact = web3.eth.send_raw_transaction(sign_store_contact.rawTransaction)
    transaction_receipt = web3.eth.wait_for_transaction_receipt(send_store_contact)
    print(f"Submitted contract method execution {HexBytes.hex(transaction_receipt.transactionHash)}")


times = random.randint(1, 4) + random.randint(0, 5)
for x in range(times):
    sleep(random.randint(1, 5) * 17 - 10)
    call_make_gold(gold_counter_contract, web3, wallet_address, private_key, contract_address)
