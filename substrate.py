from substrateinterface.base import SubstrateInterface
# TODO need to refactor this
import resources.variables

substrate = SubstrateInterface(
    url="wss://kusama-rpc.polkadot.io/",
    ss58_format=2,
    type_registry_preset='kusama'
)

# Set block_hash to None for chaintip
block_hash = resources.variables.SUBSTRATE_BLOCH_HASH


def check_block():
    # Retrieve extrinsics in block
    result = substrate.get_block(block_hash=block_hash)

    for extrinsic in result['extrinsics']:

        if 'address' in extrinsic.value:
            signed_by_address = extrinsic.value['address']
        else:
            signed_by_address = None

        print('\nPallet: {}\nCall: {}\nSigned by: {}'.format(
            extrinsic.value["call"]["call_module"],
            extrinsic.value["call"]["call_function"],
            signed_by_address
        ))

        # Loop through call params
        for param in extrinsic.value["call"]['call_args']:

            if param['type'] == 'Balance':
                param['value'] = '{} {}'.format(param['value'] / 10 ** substrate.token_decimals, substrate.token_symbol)

            print("Param '{}': {}".format(param['name'], param['value']))


check_block()