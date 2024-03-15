from service import send_mail_for_each_wallet

chain_name = 'zksync'

contract_address = '0x981F198286E40F9979274E0876636E9144B8FB8E'

send_mail_for_each_wallet(contract_address, chain_name)
