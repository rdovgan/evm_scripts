import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet
from src.contract import db_connection as db

load_dotenv()

Address = 'ADDRESS_'
PrivateKey = 'PRIVATE_KEY_'

key_to_decrypt = db.read_setting('wallet_key')

# List of all wallet abbreviation
Figa = 'FIGA'
Ledger_E4 = 'LEDGER_E4'
Ledger_D9 = 'LEDGER_D9'
Ledger_8C = 'LEDGER_8C'
Ledger_77 = 'LEDGER_77'
Papaya = 'PAPAYA'
Banana = 'BANANA'
Mango = 'MANGO'
Ginger = 'GINGER'
Guava = 'GUAVA'
Moon = 'MOON'
Mercury = 'MERCURY'
Venus = 'VENUS'
Mars = 'MARS'
Jupiter = 'JUPITER'
Saturn = 'SATURN'
Uranus = 'URANUS'
Neptune = 'NEPTUNE'
MoBox = 'MOBOX'
Sirius = 'SIRIUS'
Polaris = 'POLARIS'
Antares = 'ANTARES'
Libra = 'LIBRA'
Aquarius = 'AQUARIUS'
Fox = 'FOX'
Wolf = 'WOLF'
Deer = 'DEER'
Beaver = 'BEAVER'
Eagle = 'EAGLE'
Sparrow = 'SPARROW'
Crow = 'CROW'
Rabbit = 'RABBIT'
Turtle = 'TURTLE'

all_wallets = {Figa, Ledger_E4, Ledger_D9, Ledger_8C, Ledger_77, Papaya, Banana, Mango, Ginger, Guava, Moon, Mercury, Venus, Mars, Jupiter, Saturn, Uranus,
               Neptune, MoBox, Sirius, Polaris, Antares, Libra, Aquarius, Fox, Wolf, Deer, Beaver, Eagle, Sparrow, Crow, Rabbit, Turtle}

test = {Aquarius}


def get_wallet_data(wallet_name):
    return os.getenv(Address + wallet_name),  os.getenv(PrivateKey + wallet_name)


def load_wallets(wallets_to_load):
    fernet = Fernet(key_to_decrypt)
    wallets = {}
    for wallet_name in wallets_to_load:
        wallet_data = get_wallet_data(wallet_name)
        wallets[wallet_name] = wallet_data[0], decrypt_value(fernet, wallet_data)
    return wallets


def decrypt_value(fernet, wallet_data):
    if wallet_data[1] is None:
        return None
    return str(fernet.decrypt(bytes(wallet_data[1], 'UTF-8')), 'UTF-8')

