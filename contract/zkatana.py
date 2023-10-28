import random

import contract_service as service

from time import sleep
from web3 import Web3
from datetime import datetime
from web3.middleware import geth_poa_middleware

from wallet import wallets as w
from wallet import rpc
from logger import log


log_name = 'zkatana.log'

# wait up to 15 minutes
delay = random.randint(1, 15) * 60
# sleep(delay)
print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} Started zKatana job')

web3 = Web3(Web3.HTTPProvider(rpc.test_provider["zkatana"]))

wallets_list = w.wallets_with_keys
addresses = list(w.load_wallets(wallets_list).values())


contract_name = "zKatanaCounter"

random_wallet = random.choice(addresses)

wallet_address = random_wallet[0]
private_key = random_wallet[1]

balance = web3.from_wei(web3.eth.get_balance(wallet_address), "ether")
log(log_name, f"The balance of {wallet_address} is: {balance} ETH")

gold_counter_contract = service.define_contract(web3, wallet_address, contract_name)
contract_address = service.deploy_contract(gold_counter_contract, web3, wallet_address, private_key, contract_name, log_name)


times = random.randint(4, 10) + random.randint(0, 10)
log(log_name, f"Prepare to make {times} transactions")
for x in range(times):
    # sleep(random.randint(1, 5))
    service.call_make_gold(gold_counter_contract, web3, wallet_address, private_key, contract_address, log_name, web3.eth.gas_price)
