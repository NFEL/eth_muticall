from web3 import Web3
from collections import namedtuple
from typing import List, Dict, Optional, Union, MutableSet, TypedDict, NewType, Any

from eth_typing import ChecksumAddress

# struct Call3 {
#     address target;
#     bool allowFailure;
#     bytes callData;
# }
# struct Result {
#     bool success;
#     bytes returnData;
# }


CallFunction = namedtuple("CallFunction", ["Call", "result_decoder"])
Call = namedtuple("Call", ["target", "allowFailure", "callData"])
Result = namedtuple("Result", ["success", "returnData"])

Symbol = NewType("Symbol", str)
Decimals = NewType("Symbol", int)
Address = NewType("Symbol", ChecksumAddress)
CallData = NewType("CallData", str)


class Token(TypedDict):
    decimals: Decimals
    address: ChecksumAddress
    name: str
    symbol: Symbol
