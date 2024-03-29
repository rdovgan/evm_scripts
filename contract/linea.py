import random

import contract_service as service

from time import sleep
from web3 import Web3
from datetime import datetime

from wallet import wallets as w
from logger import log
from wallet import rpc

log_name = 'linea.log'

# wait up to 120 minutes
delay = random.randint(10, 120) * random.randint(5, 60)
sleep(delay)
print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} Started Linea job')

web3 = Web3(Web3.HTTPProvider(rpc.provider['linea']))

if web3.eth.gas_price > 10000000000:
    raise "Gas price is too high"

wallets_list = {w.Banana, w.Mango, w.Ginger, w.Guava, w.Mercury, w.Venus, w.Mars, w.Jupiter, w.Saturn, w.Neptune, w.MoBox, w.Sirius, w.Libra, w.Aquarius}
addresses = list(w.load_wallets(wallets_list).values())

contract_name = "Storage"

random_wallet = random.choice(addresses)

wallet_address = random_wallet[0]
private_key = random_wallet[1]

balance = web3.from_wei(web3.eth.get_balance(wallet_address), "ether")
log(log_name, f"The balance of {wallet_address} is: {balance} ETH")

gold_counter_contract = service.define_contract(web3, wallet_address, contract_name)
contract_address = service.deploy_contract(gold_counter_contract, web3, wallet_address, private_key, contract_name, log_name)

# times = random.randint(0, 4) + random.randint(0, 4)
times = 1

log(log_name, f"Prepare to make {times} transactions")
for x in range(times):
    service.store(gold_counter_contract, web3, wallet_address, private_key, contract_address, log_name, web3.eth.gas_price, random.randint(1, 1000))
