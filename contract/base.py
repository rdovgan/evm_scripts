import random

import contract_service as service

from time import sleep
from web3 import Web3
from datetime import datetime

from wallet import wallets as w
from logger import LoggerService


def log(message):
    with LoggerService('../logs/base.log') as logger:
        logger.info(message)


# wait up to 30 minutes
delay = random.randint(1, 30) * random.randint(3, 10) * random.randint(1, 6)
sleep(delay)
print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} Started Base job')

provider_rpc = {
    "testnet": "https://base-goerli.public.blastapi.io",
}
web3 = Web3(Web3.HTTPProvider(provider_rpc["testnet"]))

wallets_list = w.wallets_with_keys
addresses = list(w.load_wallets(wallets_list).values())

random_wallet = random.choice(addresses)

wallet_address = random_wallet[0]
private_key = random_wallet[1]

balance = web3.from_wei(web3.eth.get_balance(wallet_address), "ether")
log(f"The balance of {wallet_address} is: {balance} ETH")

contract_name = "GoldOwner"

gold_owner_contract = service.define_contract(web3, wallet_address, contract_name)
contract_address = service.deploy_contract(gold_owner_contract, web3, wallet_address, private_key, contract_name)

times = random.randint(0, 10) + random.randint(0, 10)
log(f"Prepare to make {times} transactions")
for x in range(times):
    sleep(random.randint(1, 5) * random.randint(8, 17) - random.randint(1, 10))
    service.call_make_gold(gold_owner_contract, web3, wallet_address, private_key, contract_address)
