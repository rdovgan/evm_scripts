from web3 import Web3
import decimal

from wallet import wallets as w

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


def get_coin_name(chain_id):
    coin_names = {
        1: "ETH",
        42161: "ETH",
        42170: "ETH",
        10: "ETH",
        324: "ETH",
        137: "MATIC",
        1313161554: "ETH",
        1284: "GLMR",
        1285: "MOVR",
        56: "BNB",
        43114: "AVAX",
        9001: "EVMOS",
    }
    return coin_names.get(chain_id, "Unknown Coin")


wallets_list = w.all_wallets
all_wallets = w.load_wallets(wallets_list)

total_eth = decimal.Decimal(0.0)
balance_by_network = {}

for network in provider_rpc.keys():
    print(f"\nStart scanning {network} network")
    network_balance = decimal.Decimal(0.0)
    web3 = Web3(Web3.HTTPProvider(provider_rpc[network]))
    coin_name = get_coin_name(web3.eth.chain_id)
    for wallet_name in all_wallets:
        wallet_data = all_wallets[wallet_name]
        wallet_address = wallet_data[0]
        balance = web3.from_wei(web3.eth.get_balance(wallet_address), "ether")
        nonce = web3.eth.get_transaction_count(wallet_address)
        network_balance += balance
        print(f"{wallet_name} : {wallet_address} : {balance} {coin_name}: {nonce} nonce")
    balance_by_network[network] = network_balance
    if coin_name == "ETH":
        total_eth += network_balance

print("\n---\n")
for network in balance_by_network.keys():
    print(f"Total balance for {network} network: {balance_by_network[network]}")

print("\n---\n")
print(f"Total balance for all networks: {total_eth}")
