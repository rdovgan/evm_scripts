import random

from web3 import Web3

from wallet import wallets as w
from wallet import rpc
import contract.contract_service as service


web3 = Web3(Web3.HTTPProvider(rpc.provider["arb_nova"]))

wallet_data = list(w.load_wallets({w.Mars}).values())[0]
wallet_address = wallet_data[0]
private_key = wallet_data[1]

contract_name = "GoldOwner"

gold_owner_contract = service.define_contract(web3, wallet_address, contract_name)
contract_address = service.deploy_contract(gold_owner_contract, web3, wallet_address, private_key, contract_name)

times = random.randint(5, 20)
print(f"Prepare to make {times} transactions")
for x in range(times):
    service.call_make_gold(gold_owner_contract, web3, wallet_address, private_key, contract_address)