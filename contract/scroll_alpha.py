import random

import contract_service as service

from time import sleep
from web3 import Web3
from web3.middleware import geth_poa_middleware

from wallet import wallets as w

# wait up to 15 minutes
delay = random.randint(1, 15) * 60
sleep(delay)

provider_rpc = {
    "mainnet": "https://scroll-alphanet.public.blastapi.io",
}
web3 = Web3(Web3.HTTPProvider(provider_rpc["mainnet"]))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

wallets_list = w.wallets_with_keys
addresses = list(w.load_wallets(wallets_list).values())


contract_name = "GoldScroll"

random_wallet = random.choice(addresses)

wallet_address = random_wallet[0]
private_key = random_wallet[1]

balance = web3.from_wei(web3.eth.get_balance(wallet_address), "ether")
print(f"The balance of {wallet_address} is: {balance} ETH")

gold_counter_contract = service.define_contract(web3, wallet_address, contract_name)
contract_address = service.deploy_contract(gold_counter_contract, web3, wallet_address, private_key, contract_name)


times = random.randint(4, 10) + random.randint(0, 10)
print(f"Prepare to make {times} transactions")
for x in range(times):
    sleep(random.randint(1, 5) * 7)
    service.call_make_gold(gold_counter_contract, web3, wallet_address, private_key, contract_address, web3.eth.gas_price)
