provider = {
    "mainnet": "https://ethereum.publicnode.com",
    "arbitrum": "https://arbitrum.llamarpc.com",
    "arb_nova": "https://arbitrum-nova.public.blastapi.io",
    "optimism": "https://optimism-rpc.publicnode.com",
    "base": "https://base-rpc.publicnode.com",
    "moonbeam": "https://rpc.api.moonbeam.network",
    "moonriver": "https://moonriver.public.blastapi.io",
    "zksync": "https://mainnet.era.zksync.io",
    "polygon": "https://polygon-bor.publicnode.com",
    "smart_chain": "https://bsc.publicnode.com",
    "avax": "https://avalanche-c-chain.publicnode.com",
    "evmos": "https://evmos-evm.publicnode.com",
    "aurora": "https://mainnet.aurora.dev",
    "zk_evm": "https://zkevm-rpc.com",
    "linea": "https://rpc.linea.build",
    "scroll": "https://rpc.scroll.io"
}

test_provider = {
    "sepolia": "https://endpoints.omniatech.io/v1/eth/sepolia/public",
    "arb_sep": "https://sepolia-rollup.arbitrum.io/rpc",
    "stylus": "https://stylus-testnet.arbitrum.io/rpc",
    "op_bnb": "https://opbnb-testnet-rpc.bnbchain.org",
    "scroll_alpha": "https://scroll-alphanet.public.blastapi.io",
    "scroll_sep": "https://1rpc.io/scroll/sepolia",
    "base": "https://base-goerli.public.blastapi.io",
    "zkatana": "https://rpc.zkatana.gelato.digital",
    "linea_goerli": "https://rpc.goerli.linea.build",
    "frame_test": "https://rpc.testnet.frame.xyz/http",
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
        1101: "ETH",
        51144: "ETH",
    }
    return coin_names.get(chain_id, "Unknown Coin")
