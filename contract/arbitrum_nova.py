import random

import contract_service as service

from time import sleep
from web3 import Web3
from datetime import datetime

from wallet import wallets as w
from logger import log
from wallet import rpc

log_name = 'arb_nova.log'

# wait up to 20 minutes
delay = random.randint(1, 20) * random.randint(5, 30) * random.randint(1, 2)
sleep(delay)
print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} Started Arbitrum Nova job')

web3 = Web3(Web3.HTTPProvider(rpc.provider['arb_nova']))

if web3.eth.gas_price > 100000000:
    raise "Gas price is too high"

wallets_list = w.not_animals | w.wallets_game
addresses = list(w.load_wallets(wallets_list).values())

contract_name = "GoldCounter"

random_wallet = random.choice(addresses)

wallet_address = random_wallet[0]
private_key = random_wallet[1]

balance = web3.from_wei(web3.eth.get_balance(wallet_address), "ether")
log(log_name, f"The balance of {wallet_address} is: {balance} ETH")

gold_counter_contract = service.define_contract(web3, wallet_address, contract_name)
contract_address = service.deploy_contract(gold_counter_contract, web3, wallet_address, private_key, contract_name, log_name)

times = random.randint(0, 2) + random.randint(0, 2)

log(log_name, f"Prepare to make {times} transactions")
for x in range(times):
    sleep(random.randint(2, 7) * random.randint(7, 11) - random.randint(13, 19))
    service.call_make_gold(gold_counter_contract, web3, wallet_address, private_key, contract_address, log_name)
