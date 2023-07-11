import os
import requests
from web3 import Web3
from dotenv import load_dotenv
from web3.middleware import geth_poa_middleware

from wallet import rpc

from wallet import wallets as w

# w3.middleware_onion.inject(geth_poa_middleware, layer=0)

wallets_list = w.all_wallets
addresses = w.load_wallets(wallets_list)

load_dotenv()

supported_chains = ['mainnet', 'optimism', 'arbitrum', 'polygon', 'smart_chain']

contract_dict = {
    'mm_mainnet_swap': ['0x881D40237659C251811CEC9c364ef91dC08D300C', '0x9dDA6Ef3D919c9bC8885D5560999A3640431e8e6'],
    'mm_mainnet_bridge': ['0x82E0b8cDD80Af5930c4452c684E71c861148Ec8A'],

    'mm_optimism_swap': ['0x881D40237659C251811CEC9c364ef91dC08D300C', '0x9dDA6Ef3D919c9bC8885D5560999A3640431e8e6'],
    'mm_optimism_bridge': ['0x82E0b8cDD80Af5930c4452c684E71c861148Ec8A'],

    'mm_arbitrum_swap': ['0x881D40237659C251811CEC9c364ef91dC08D300C', '0x9dDA6Ef3D919c9bC8885D5560999A3640431e8e6'],
    'mm_arbitrum_bridge': ['0x82E0b8cDD80Af5930c4452c684E71c861148Ec8A'],

    'mm_polygon_swap': ['0x1a1ec25DC08e98e5E93F1104B5e5cdD298707d31', '0x881D40237659C251811CEC9c364ef91dC08D300C'],
    'mm_polygon_bridge': ['0x82E0b8cDD80Af5930c4452c684E71c861148Ec8A'],

    'mm_smart_chain_swap': ['0x881D40237659C251811CEC9c364ef91dC08D300C', '0x9dDA6Ef3D919c9bC8885D5560999A3640431e8e6'],
    'mm_smart_chain_bridge': ['0x82E0b8cDD80Af5930c4452c684E71c861148Ec8A'],
}


def define_contracts_to_check(service, chain, action):
    return contract_dict[f'{service}_{chain}_{action}']


# Define the API endpoint
def define_api_endpoint(chain, address, block_number):
    api = ''
    api_key = ''
    if chain == 'mainnet':
        api = 'https://api.etherscan.io/api'
        api_key = os.getenv('ETHERSCAN_API_KEY')
    elif chain == 'optimism':
        api = 'https://api-optimistic.etherscan.io/api'
        api_key = os.getenv('OPTIMISMSCAN_API_KEY')
    elif chain == 'arbitrum':
        api = 'https://api.arbiscan.io/api'
        api_key = os.getenv('ARBITRUMSCAN_API_KEY')
    elif chain == 'polygon':
        api = 'https://api.polygonscan.com/api'
        api_key = os.getenv('POLYGONSCAN_API_KEY')
    elif chain == 'smart_chain':
        api = 'https://api.bscscan.com/api'
        api_key = os.getenv('BSCSCAN_API_KEY')
    return f"{api}?module=account&action=txlist&address={address}&startblock=0&endblock={block_number}&sort=desc&apikey={api_key}"


def define_transaction_list(chain, address, block_number):
    url = define_api_endpoint(chain, address, block_number)
    try:
        # Send a GET request to the API endpoint
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the response JSON
            data = response.json()

            # Check if the API returned a successful response
            if data['status'] == '1':
                # Retrieve the list of transactions
                transactions = data['result']

                # Process the transactions
                # print_transaction_info(transactions)
                return transactions
            # else:
            #     print(f"API Error: {data['message']}")
        else:
            print(f"Request Error: {response.status_code} - {response.reason}")
    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {e}")
    return None


def print_transaction_info(transactions):
    for tx in transactions:
        print(f"Transaction Hash: {tx['hash']}")
        print(f"From: {tx['from']}")
        print(f"To: {tx['to']}")
        print(f"Timestamp: {tx['timeStamp']}")
        print("")


def has_interacted_with_contract(transactions, contract_address):
    counter = 0
    if transactions is None:
        return counter
    for transaction in transactions:
        if str(transaction['to']).lower() == contract_address.lower():
            counter += 1
    return counter


def check_meta_mask_contract_usage():
    wallet_rating = {}
    for chain in supported_chains:
        print('-' * (10 + len(chain)))
        print('-' * 5 + f'{chain}' + '-' * 5)
        print('-' * (10 + len(chain)))
        w3 = Web3(Web3.HTTPProvider(rpc.provider[chain]))
        block_number = w3.eth.block_number
        for wallet in addresses:
            transactions = define_transaction_list(chain, addresses[wallet][0], block_number)
            if transactions is None or len(transactions) == 0:
                continue
            print(f"{wallet} total Transactions: {len(transactions)}")
            rating = 0
            rating += check_contract_usage(transactions, chain, 'mm', 'swap', (wallet, addresses[wallet]))
            rating += check_contract_usage(transactions, chain, 'mm', 'bridge', (wallet, addresses[wallet]))
            # put rating into wallet_rating by wallet
            wallet_rating[wallet] = wallet_rating.get(wallet, 0) + rating
            print(f'{wallet} {rating} point(s)\n')
    print(wallet_rating)


def check_contract_usage(transactions, chain, service, method, wallet):
    # print(f"Checking {wallet[0]} on {chain} network")
    contracts = define_contracts_to_check(service, chain, method)
    counter = 0
    for contract_address in contracts:
        counter += has_interacted_with_contract(transactions, contract_address)
    if counter > 0:
        print(f"{wallet[0]} has interacted with {service}.{method} {counter} time(s)")
    return counter


check_meta_mask_contract_usage()
