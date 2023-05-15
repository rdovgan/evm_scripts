from web3 import Web3
import decimal

from wallet import wallets as w

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

all_wallets = [w.ADDRESS_FIGA, w.ADDRESS_LEDGER_1, w.ADDRESS_LEDGER_2, w.ADDRESS_LEDGER_3, w.ADDRESS_LEDGER_4, w.ADDRESS_PAPAYA, w.ADDRESS_BANANA,
               w.ADDRESS_MANGO, w.ADDRESS_GINGER, w.ADDRESS_GUAVA, w.ADDRESS_MOON, w.ADDRESS_MERCURY, w.ADDRESS_VENUS, w.ADDRESS_MARS, w.ADDRESS_JUPITER,
               w.ADDRESS_SATURN, w.ADDRESS_URANUS, w.ADDRESS_NEPTUNE, w.ADDRESS_MOBOX, w.ADDRESS_SIRIUS, w.ADDRESS_POLARIS, w.ADDRESS_ANTARES, w.ADDRESS_LIBRA,
               w.ADDRESS_AQUARIUS, w.ADDRESS_WOLF, w.ADDRESS_FOX, w.ADDRESS_DEER, w.ADDRESS_BEAVER, w.ADDRESS_EAGLE, w.ADDRESS_SPARROW, w.ADDRESS_CROW,
               w.ADDRESS_RABBIT, w.ADDRESS_TURTLE]

total_eth = decimal.Decimal(0.0)
balance_by_network = {}

for network in provider_rpc.keys():
    print(f"\nStart scanning {network} network")
    network_eth = decimal.Decimal(0.0)
    web3 = Web3(Web3.HTTPProvider(provider_rpc[network]))
    for wallet in all_wallets:
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
