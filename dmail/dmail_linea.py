from web3 import Web3
import json

from wallet import rpc
from service import send_mail_for_each_wallet

chain_name = 'linea'

web3 = Web3(Web3.HTTPProvider(rpc.provider[chain_name]))
with open('dmail_abi.json', 'r') as f:
    contract_abi = json.load(f)

contract_address = '0xd1a3abf42f9e66be86cfdea8c5c2c74f041c5e14'

# Create contract instance
contract = web3.eth.contract(address=Web3.to_checksum_address(contract_address), abi=contract_abi)

send_mail_for_each_wallet(web3, contract, contract_address, chain_name)
