import random

from web3 import Web3

from wallet import wallets as w
import src.contract.contract_service as service
import src.contract.db_connection as db

provider_rpc = {
    "testnet": "https://base-goerli.public.blastapi.io",
}
web3 = Web3(Web3.HTTPProvider(provider_rpc["testnet"]))

wallet_address = w.ADDRESS_MARS
private_key = w.PRIVATE_KEY_MARS

contract_name = "GoldOwner"

gold_owner_contract = service.define_contract(web3, wallet_address, contract_name)
contract_address = service.deploy_contract(gold_owner_contract, web3, wallet_address, private_key, contract_name)

times = random.randint(5, 20)
print(f"Prepare to make {times} transactions")
for x in range(times):
    service.call_make_gold(gold_owner_contract, web3, wallet_address, private_key, contract_address)
    # service.call_make_gold(gold_owner_contract, web3, wallet_address, private_key, db.read_contract(resources.variables.ADDRESS_GINGER)[2])
