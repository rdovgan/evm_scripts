provider = {
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