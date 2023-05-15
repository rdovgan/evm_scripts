import random

import contract_service as service
import db_connection as db

from time import sleep
from web3 import Web3

from wallet import wallets as w

# wait up to 20 minutes
delay = random.randint(1, 20) * 60
sleep(delay)

provider_rpc = {
    "mainnet": "https://arbitrum-nova.public.blastapi.io",
}
web3 = Web3(Web3.HTTPProvider(provider_rpc["mainnet"]))

if web3.eth.gas_price > 100000000:
    raise "Gas price is too high"

addresses = [(w.ADDRESS_BANANA, w.PRIVATE_KEY_BANANA), (w.ADDRESS_MANGO, w.PRIVATE_KEY_MANGO), (w.ADDRESS_GUAVA, w.PRIVATE_KEY_GUAVA),
             (w.ADDRESS_GINGER, w.PRIVATE_KEY_GINGER),
             (w.ADDRESS_MERCURY, w.PRIVATE_KEY_MERCURY), (w.ADDRESS_VENUS, w.PRIVATE_KEY_VENUS), (w.ADDRESS_MARS, w.PRIVATE_KEY_MARS),
             (w.ADDRESS_JUPITER, w.PRIVATE_KEY_JUPITER), (w.ADDRESS_SATURN, w.PRIVATE_KEY_SATURN), (w.ADDRESS_URANUS, w.PRIVATE_KEY_URANUS)]

contract_name = "GoldCounter"

random_wallet = random.choice(addresses)

wallet_address = random_wallet[0]
private_key = random_wallet[1]

balance = web3.from_wei(web3.eth.get_balance(wallet_address), "ether")
print(f"The balance of {wallet_address} is: {balance} ETH")

gold_counter_contract = service.define_contract(web3, wallet_address, contract_name)
contract_address = service.deploy_contract(gold_counter_contract, web3, wallet_address, private_key, contract_name)

times = random.randint(0, 4) + random.randint(0, 5)
for x in range(times):
    sleep(random.randint(1, 5) * 17 - 10)
    service.call_make_gold(gold_counter_contract, web3, wallet_address, private_key, contract_address)
