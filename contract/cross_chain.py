from web3 import Web3
import decimal

from wallet import wallets as w
from wallet import rpc


def get_balance_for_wallets(wallets):
    all_wallets = w.load_wallets(wallets)
    total_eth = decimal.Decimal(0.0)
    balance_by_network = {}
    for network in rpc.provider.keys():
        print(f"\nStart scanning {network} network")
        network_balance = decimal.Decimal(0.0)
        web3 = Web3(Web3.HTTPProvider(rpc.provider[network]))
        coin_name = rpc.get_coin_name(web3.eth.chain_id)
        for wallet_name in all_wallets:
            wallet_data = all_wallets[wallet_name]
            wallet_address = wallet_data[0]
            balance = web3.from_wei(web3.eth.get_balance(wallet_address), "ether")
            nonce = web3.eth.get_transaction_count(wallet_address)
            network_balance += balance
            if balance > 0:
                print(f"{wallet_name} : {wallet_address} : {balance} {coin_name}: {nonce} nonce")
        balance_by_network[network] = network_balance
        if coin_name == "ETH":
            total_eth += network_balance
    print("\n---\n")
    for network in balance_by_network.keys():
        print(f"Total balance for {network} network: {balance_by_network[network]}")
    print("\n---\n")
    print(f"Total balance for all networks: {total_eth}")


# get_balance_for_wallets(w.all_wallets)
get_balance_for_wallets({w.Figa})
