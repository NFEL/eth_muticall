import itertools
from collections.abc import Iterable
from collections import namedtuple
from eth_typing import AnyAddress, HexStr
from web3.contract import ContractFunction
from dataclasses import dataclass
from functools import partial
from typing import Optional, List, Any, Union, Dict, Iterable
from eth_abi.exceptions import DecodingError
from web3.contract import get_abi_output_types, BASE_RETURN_NORMALIZERS, map_abi_data
from web3 import Web3

import Constants
import ABI

## IMPORTS
# Call = namedtuple("Call", ["target", "gasLimit", "calldata"])
Call = namedtuple("Call", ["target", "calldata"])
Result = namedtuple("Result", ["success", "returnData"])

ABI = ABI.ABI
MultiChain = Constants.MultiChain
CHAIN_SEPARATED_ADDRESS = Constants.CHAIN_SEPARATED_ADDRESS




@dataclass(
    init=True,
)
class FunctionCall:
    w3: Web3
    chain_id: int
    contract_abi: List[dict]
    ## Would not consider function overloading and uses the first function name match
    fn_name: str
    target: AnyAddress
    params: Iterable = None
    func: ContractFunction = None
    abi: dict = None

    call: Call = None
    result: Result = None

    gas_limit: int = 3_000_000

    def parse_call(
        self,
        target: AnyAddress = None,
        params: Iterable = None,
        gas_limit: int = None,
        call_data=None,
    ) -> Call:
        # Calls _encode_transaction_data of function
        # cls.web3, cls.abi, cls.arguments, cls.selector
        _param = params or self.params
        if _param:
            if not isinstance(_param, Iterable):
                _param = (_param,)
            _call_data = call_data or self._func(*_param)._encode_transaction_data()
        else:
            # _func Possibly took no parameters
            _call_data = call_data or self._func()._encode_transaction_data()
        assert _call_data, f"No Way to call This {self._func}"
            
        self.call = Call(
            target or self.target,
            # gas_limit or self.gas_limit,
            _call_data
        )
        return self.call

    @property
    def _func(self):
        if self.func is None:
            self.func = self.w3.eth.contract(abi=[self.fun_abi]).get_function_by_name(
                self.fn_name
            )
        return self.func

    @property
    def fun_abi(o):
        if o.abi is None:
            for _ in o.contract_abi:
                if _.get("name") == o.fn_name:
                    o.abi = _
                    break
            assert o.abi is not None, "Couldn't Find abi"
        return o.abi

    def parse_result_dict(self, result: Result, output_types: Dict = None) -> Dict:
        _ = self.parse_result(result, list(output_types.values()))
        return dict(zip(output_types.keys(), _))

    def parse_result(self, result: bytes, output_types: List[Any] = None) -> List[Any]:
        # ['uint256']

        if output_types is None:
            output_types = get_abi_output_types(self.fun_abi)
        try:
            output_data = self.func.web3.codec.decode_abi(output_types, result)
        except DecodingError as e:
            print(e)
            raise e

        _normalizers = itertools.chain(
            BASE_RETURN_NORMALIZERS,
            self.func._return_data_normalizers,
        )
        normalized_data = map_abi_data(_normalizers, output_types, output_data)
        return normalized_data

    def make_result(self, success: bool, gas_used: int, return_data: HexStr) -> Result:
        self.result = Result(success, gas_used, return_data)
        return self.result

