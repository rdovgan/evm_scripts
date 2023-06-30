from web3 import Web3
import decimal

from src.wallet import wallets as w

provider_rpc = {
    "mainnet": "https://ethereum.publicnode.com",
    "arbitrum": "https://arb1.croswap.com/rpc",
    "arb_nova": "https://arbitrum-nova.public.blastapi.io",
    "optimism": "https://optimism-mainnet.public.blastapi.io",
    # "moonbeam": "https://rpc.api.moonbeam.network",
    # "moonriver": "https://moonriver.public.blastapi.io",
    "zksync": "https://mainnet.era.zksync.io",
    # "polygon": "https://polygon-bor.publicnode.com",
    # "smart_chain": "https://bsc.publicnode.com",
    # "avax": "https://avalanche-c-chain.publicnode.com",
    # "evmos": "https://evmos-evm.publicnode.com",
    "aurora": "https://mainnet.aurora.dev"
}

wallets_list = w.all_wallets
all_wallets = list(w.load_wallets(wallets_list).values())

total_eth = decimal.Decimal(0.0)
balance_by_network = {}

for network in provider_rpc.keys():
    print(f"\nStart scanning {network} network")
    network_eth = decimal.Decimal(0.0)
    web3 = Web3(Web3.HTTPProvider(provider_rpc[network]))
    for wallet_data in all_wallets:
        wallet = wallet_data[0]
        balance = web3.from_wei(web3.eth.get_balance(wallet), "ether")
        network_eth += balance
        print(f"The balance of {wallet} is: {balance} ETH")
    balance_by_network[network] = network_eth
    total_eth += network_eth

print("\n---\n")
for network in balance_by_network.keys():
    print(f"Total balance for {network} network: {balance_by_network[network]} ETH")

print("\n---\n")
print(f"Total balance for all networks: {total_eth} ETH")
