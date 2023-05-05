from web3 import Web3

import resources.variables
import src.contract.contract_service as service

provider_rpc = {
    "testnet": "https://base-goerli.public.blastapi.io",
}
web3 = Web3(Web3.HTTPProvider(provider_rpc["testnet"]))

wallet_address = resources.variables.ADDRESS_GINGER
private_key = resources.variables.PRIVATE_KEY_GINGER

contract_name = "GoldOwner"

GoldOwnerContract = service.define_contract(web3, wallet_address, contract_name)
contract_address = service.deploy_contract(GoldOwnerContract, web3, wallet_address, private_key, contract_name)

service.call_make_gold(GoldOwnerContract, web3, wallet_address, private_key, contract_address)
