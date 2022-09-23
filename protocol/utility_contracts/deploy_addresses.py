from enum import Enum
from eth_typing import HexStr


class ZkSyncAddresses(Enum):
    ETH_ADDRESS = HexStr("0x0000000000000000000000000000000000000000")
    CONTRACT_DEPLOYER_ADDRESS = HexStr("0x0000000000000000000000000000000000008006")
    NONCE_HOLDER_ADDRESS = HexStr("0x0000000000000000000000000000000000008003")
    MESSENGER_ADDRESS = HexStr("0x0000000000000000000000000000000000008008")