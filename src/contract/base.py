from web3 import Web3

import resources.variables
import src.contract.contract_service as service

provider_rpc = {
    "testnet": "https://base-goerli.public.blastapi.io",
}
web3 = Web3(Web3.HTTPProvider(provider_rpc["testnet"]))

wallet_address = resources.variables.ADDRESS_MERCURY
private_key = resources.variables.PRIVATE_KEY_MERCURY

contract_name = "GoldOwner"

gold_owner_contract = service.define_contract(web3, wallet_address, contract_name)
contract_address = service.deploy_contract(gold_owner_contract, web3, wallet_address, private_key, contract_name)

service.call_make_gold(gold_owner_contract, web3, wallet_address, private_key, contract_address)
