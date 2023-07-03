import random

import contract_service as service

from time import sleep
from web3 import Web3
from datetime import datetime
from web3.middleware import geth_poa_middleware

from wallet import wallets as w
from logger import log


log_name = 'optimism_bnb.log'

# wait up to 10 minutes
delay = random.randint(1, 20) * random.randint(1, 30)
sleep(delay)
print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} Started Optimism BNB job')

provider_rpc = {
    "testnet": "https://data-seed-prebsc-1-s1.binance.org:8545",
}
web3 = Web3(Web3.HTTPProvider(provider_rpc["testnet"]))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

wallets_list = {w.Banana, w.Mango, w.Guava, w.Ginger, w.Mercury, w.Venus, w.Mars, w.Jupiter, w.Sirius, w.Libra, w.Aquarius}
addresses = list(w.load_wallets(wallets_list).values())

contract_name = "OptimismBnb"

random_wallet = random.choice(addresses)

wallet_address = random_wallet[0]
private_key = random_wallet[1]

balance = web3.from_wei(web3.eth.get_balance(wallet_address), "ether")
log(log_name, f"The balance of {wallet_address} is: {balance} ETH")

gold_counter_contract = service.define_contract(web3, wallet_address, contract_name)
contract_address = service.deploy_contract(gold_counter_contract, web3, wallet_address, private_key, contract_name, log_name)

times = random.randint(0, 4) + random.randint(0, 5)
log(log_name, f"Prepare to make {times} transactions")
for x in range(times):
    sleep(random.randint(1, 5) * random.randint(11, 13) - random.randint(7, 10))
    service.call_make_gold(gold_counter_contract, web3, wallet_address, private_key, contract_address, web3.eth.gas_price, log_name)
