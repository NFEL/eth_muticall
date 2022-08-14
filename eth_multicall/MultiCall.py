import logging
from eth_multicall.MultiChain import MultiChain
from eth_multicall.custome_types import List, CallFunction, Result, Dict
from eth_abi.exceptions import DecodingError

logger = logging.getLogger(__name__)

class MultiCaller(list):
    def call(calls: List[CallFunction], chain: MultiChain):
        r = chain.multicall([call.Call for call in calls]).call()
        _res = []
        for i, response in enumerate(r):
            response = Result(*response)
            if response.success:
                try:
                    logger.info(calls[i])
                    logger.info(calls[i].result_decoder)
                    _tmp = calls[i].result_decoder(response.returnData)
                    if len(_tmp) == 1:
                        _res.append(_tmp[0])
                    else:
                        _res.append(_tmp)
                except DecodingError as e:
                    logger.warn(e)
                    _res.append(str(e))
            else:
                _res.append(None)
        return _res


# class MultiCaller(dict):
#     def call(chain_separated_calls: Dict[CallFunction]):
#         _chain_res = {}
#         for chain, calls in chain_separated_calls.items():
#             r = chain.multicall([call.Call for call in calls]).call()
#             _res = []
#             for i, response in enumerate(r):
#                 response = Result(*response)
#                 _res.append(calls[i].result_decoder(response.returnData))
#             _chain_res[chain] = _res
#         return _chain_res
