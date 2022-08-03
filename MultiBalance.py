from enum import Enum
from functools import partial
from MultiCall import MultiCall
from FunctionCall import FunctionCall
from ABI import ABI

# class TokensList(Enum):


MultiBalance = lambda w3: partial(
    FunctionCall, w3, w3.eth.chain_id, ABI.TOKEN, "balanceOf"
)
