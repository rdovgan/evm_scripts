from web3 import Web3

import resources.variables

providerRpc = {
    "development": "https://rpc.api.moonriver.moonbeam.network/",
    "alphanet": "https://rpc.api.moonbase.moonbeam.network",
}
# Connect to RPC
web3 = Web3(Web3.HTTPProvider(providerRpc["development"]))

contract_skybreach = resources.variables.CONTRACT_ADDRESS_SKYBREACH

# Read ABI structure to understand smart contract
with open('../abi/skybreach-abi.json', 'r') as file:
    abi_skybreach = file.read().replace('\n', '')

# Initialise Smart contract component
contract_skybreach_component = web3.eth.contract(address=Web3.toChecksumAddress(contract_skybreach), abi=abi_skybreach)


# Call smart contract to retrieve land data
def get_land_info(land_id: int):
    land_info = contract_skybreach_component.functions.getPlotData(land_id).call()
    return land_info


# Call smart contract to retrieve owners of provided lands
def get_plots_owners(land_ids):
    land_owners = contract_skybreach_component.functions.getPlotOwners(land_ids).call()
    return land_owners


# Splits provided array to chunks with provided size
def split_array(array, size: int):
    chunks = []
    for i in range(0, len(array), size):
        chunks.append(array[i:i + size])
    return chunks


# Combine two arrays with lands and owners into one array
def define_land_to_owner_list(lands, owners):
    land_to_owner_list = []
    # define size of result array by defining min length of two arrays
    size = min(len(lands), len(owners))
    for i in range(0, size):
        land_to_owner_list.append((lands[i], owners[i], None))
    return land_to_owner_list
