import random

import contract_service as service

from time import sleep
from web3 import Web3

from src.wallet import wallets as w

# wait up to 20 minutes
delay = random.randint(1, 20) * 60
sleep(delay)

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
print(f"The balance of {wallet_address} is: {balance} ETH")

contract_name = "GoldOwner"

gold_owner_contract = service.define_contract(web3, wallet_address, contract_name)
contract_address = service.deploy_contract(gold_owner_contract, web3, wallet_address, private_key, contract_name)

times = random.randint(0, 4) + random.randint(0, 5)
print(f"Prepare to make {times} transactions")
for x in range(times):
    sleep(random.randint(1, 5) * 17 - 10)
    service.call_make_gold(gold_owner_contract, web3, wallet_address, private_key, contract_address)
    # service.call_make_gold(gold_owner_contract, web3, wallet_address, private_key, db.read_contract(resources.variables.ADDRESS_GINGER)[2])
