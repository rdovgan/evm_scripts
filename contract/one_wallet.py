import random

from web3 import Web3

from wallet import wallets as w
import contract.contract_service as service


provider_rpc = {
    "mainnet": "https://ethereum.publicnode.com",
    "arbitrum": "https://arb1.croswap.com/rpc",
    "arb_nova": "https://arbitrum-nova.public.blastapi.io",
    "optimism": "https://optimism-mainnet.public.blastapi.io",
    "moonbeam": "https://rpc.api.moonbeam.network",
    "moonriver": "https://moonriver.public.blastapi.io",
    "zksync": "https://mainnet.era.zksync.io",
    "polygon": "https://polygon-bor.publicnode.com",
    "smart_chain": "https://bsc.publicnode.com",
    "avax": "https://avalanche-c-chain.publicnode.com",
    "evmos": "https://evmos-evm.publicnode.com",
    "aurora": "https://mainnet.aurora.dev"
}

web3 = Web3(Web3.HTTPProvider(provider_rpc["arb_nova"]))

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
    # service.call_make_gold(gold_owner_contract, web3, wallet_address, private_key, db.read_contract(resources.variables.ADDRESS_GINGER)[2])
