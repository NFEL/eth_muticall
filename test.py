import ABI
import Constants
from functools import partial
from FunctionCall import FunctionCall

MultiChain = Constants.MultiChain
ABI = ABI.ABI
# TEST
w3 = MultiChain.LOCAL.w3
chain_id = MultiChain.LOCAL.value

tokens = {
    "USDT":"0xdAC17F958D2ee523a2206206994597C13D831ec7",
    "DAI":"0x6B175474E89094C44Da98b954EedeAC495271d0F",
    "BUSD" : "0x4Fabb145d64652a948d72533023f6E7A623C7C53",
    "USDC" : "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    # "FTM": "0x21be370D5312f44cB42ce377BC9b8a0cEF1A4C83",
    # "LINK": "0xb3654dc3D10Ea7645f8319668E8F54d2574FBdC8",
    # "ETH": "0x321162Cd933E2Be498Cd2267a90534A804051b11",
}
# contracts = {k: w3.eth.contract(v, abi=ABI.TOKEN) for k, v in tokens.items()}
# balances of wallet 0xB49F17514D6F340d7bcdFfC47526C9A3713697e0
wallet_address = "0xB49F17514D6F340d7bcdFfC47526C9A3713697e0"
wallet_addresses = [
    "0xB49F17514D6F340d7bcdFfC47526C9A3713697e0",
    "0xdAC17F958D2ee523a2206206994597C13D831ec7",
    "0x6B175474E89094C44Da98b954EedeAC495271d0F",
]

# Use cases

_FunctionCall = partial(FunctionCall, w3, chain_id)
Token = partial(
    _FunctionCall,
    ABI.TOKEN,
)
TokenBalance = partial(Token, "balanceOf")
