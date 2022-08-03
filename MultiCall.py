from collections import namedtuple
from typing import List, Dict
from web3 import Web3
from FunctionCall import FunctionCall
import Constants
import ABI

# IMPORTS
Call = namedtuple("Call", ["target", "calldata"])
Result = namedtuple("Result", ["success", "returnData"])

ABI = ABI.ABI
MultiChain = Constants.MultiChain
CHAIN_SEPARATED_ADDRESS = Constants.CHAIN_SEPARATED_ADDRESS


# List[FunctionCall]
class MultiCall(list):

    MULTI_CALL_ABI = ABI.MARKER_MULTI_CALL
    ADDRESSES = CHAIN_SEPARATED_ADDRESS

    def __add__(self, v):
        if isinstance(v, FunctionCall):
            super().__add__(v)
        raise TypeError("Must be of type FunctionCall ")

    def _call(
        self, w3: Web3, params: List[Call], multi_call_address: str
    ) -> List[Result]:
        # Chunked call must be placed
        params = tuple([tuple(param) for param in params])
        return (
            w3.eth.contract(multi_call_address, abi=self.MULTI_CALL_ABI)
            .functions.aggregate(params)
            .call()[1]
        )

    def _map_indices(
        self, reqs: List[FunctionCall], indices, w3: Web3, final_result: list, chain_id
    ) -> list:
        params = [_.parse_call() for _ in reqs]
        multi_call_address = self.ADDRESSES.get(chain_id)
        for i, _temp_res in enumerate(self._call(w3, params, multi_call_address)):
            final_result[indices[i]] = reqs[i].parse_result(_temp_res)

    def _separate_by_chain(self) -> tuple:
        _req: Dict[int, List[FunctionCall]] = {}
        _indices: Dict[int, List[int]] = {}
        _web3_instances = []
        for i, _ in enumerate(self):
            _chain_id = _.chain_id
            if _chain_id not in _req:
                _req[_chain_id] = []
                _indices[_chain_id] = []
                _web3_instances.append(_.w3)
            _req[_chain_id].append(_)
            _indices[_chain_id].append(i)
        return _req, _indices, _web3_instances

    def result(self, chain_id) -> List[list]:
        _result = [None for i in self]
        _req, _indices, _web3_instances = self._separate_by_chain()
        for w3 in _web3_instances:
            self._map_indices(
                _req[chain_id],
                _indices[chain_id],
                w3,
                _result,
                chain_id,
            )

        return _result
