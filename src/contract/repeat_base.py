import random

import contract_service as service
import db_connection as db

from time import sleep
from web3 import Web3

from wallet import wallets as w

# wait up to 20 minutes
delay = random.randint(1, 20) * 60
sleep(delay)

provider_rpc = {
    "testnet": "https://base-goerli.public.blastapi.io",
}
web3 = Web3(Web3.HTTPProvider(provider_rpc["testnet"]))

addresses = [(w.ADDRESS_BANANA, w.PRIVATE_KEY_BANANA), (w.ADDRESS_MANGO, w.PRIVATE_KEY_MANGO), (w.ADDRESS_GUAVA, w.PRIVATE_KEY_GUAVA),
             (w.ADDRESS_GINGER, w.PRIVATE_KEY_GINGER),
             (w.ADDRESS_MERCURY, w.PRIVATE_KEY_MERCURY), (w.ADDRESS_VENUS, w.PRIVATE_KEY_VENUS), (w.ADDRESS_MARS, w.PRIVATE_KEY_MARS),
             (w.ADDRESS_JUPITER, w.PRIVATE_KEY_JUPITER), (w.ADDRESS_SATURN, w.PRIVATE_KEY_SATURN), (w.ADDRESS_URANUS, w.PRIVATE_KEY_URANUS),
             (w.ADDRESS_NEPTUNE, w.PRIVATE_KEY_NEPTUNE),
             (w.ADDRESS_SIRIUS, w.PRIVATE_KEY_SIRIUS), (w.ADDRESS_POLARIS, w.PRIVATE_KEY_POLARIS), (w.ADDRESS_ANTARES, w.PRIVATE_KEY_ANTARES),
             (w.ADDRESS_LIBRA, w.PRIVATE_KEY_LIBRA), (w.ADDRESS_AQUARIUS, w.PRIVATE_KEY_AQUARIUS),
             (w.ADDRESS_WOLF, w.PRIVATE_KEY_WOLF), (w.ADDRESS_FOX, w.PRIVATE_KEY_FOX), (w.ADDRESS_DEER, w.PRIVATE_KEY_DEER),
             (w.ADDRESS_BEAVER, w.PRIVATE_KEY_BEAVER), (w.ADDRESS_EAGLE, w.PRIVATE_KEY_EAGLE), (w.ADDRESS_SPARROW, w.PRIVATE_KEY_SPARROW),
             (w.ADDRESS_CROW, w.PRIVATE_KEY_CROW), (w.ADDRESS_RABBIT, w.PRIVATE_KEY_RABBIT), (w.ADDRESS_TURTLE, w.PRIVATE_KEY_TURTLE)]

random_wallet = random.choice(addresses)

wallet_address = random_wallet[0]
private_key = random_wallet[1]

contract_name = "GoldOwner"

gold_owner_contract = service.define_contract(web3, wallet_address, contract_name)
contract_address = service.deploy_contract(gold_owner_contract, web3, wallet_address, private_key, contract_name)

times = random.randint(0, 4) + random.randint(0, 5)
for x in range(times):
    sleep(random.randint(1, 5) * 17 - 10)
    service.call_make_gold(gold_owner_contract, web3, wallet_address, private_key, contract_address)
    # service.call_make_gold(gold_owner_contract, web3, wallet_address, private_key, db.read_contract(resources.variables.ADDRESS_GINGER)[2])
