# MY Version
# ? Compile Fucntion First
# ! List as arg/kwarg
# ! List as targets
# ? Caller uses a tuple
from functools import partial

from eth_abi import decode
from custome_types import CallFunction, Call, Web3, Address


def parse_call(w3: Web3, address, abi, fn_name, *arg, **kwarg) -> str:
    return getattr(w3.eth.contract(address=address, abi=abi).functions, fn_name)(
        *arg, **kwarg
    )._encode_transaction_data()


def fn_abi(abi, fn_name):
    # TODO add named dict response
    for fn_abi in abi:
        if (
            fn_abi.get("name") == fn_name
            and fn_abi.get("type", "function") == "function"
        ):
            return fn_abi


def fn_abi_res_types(fn_abi):
    return [_.get("type") for _ in fn_abi.get("outputs")]


def result_decoder(fn_abi):
    """ """
    decoder = partial(decode, fn_abi)
    # def lazy_parser(decoder=decoder)
    return decoder


def compile(w3: Web3, address: Address, abi: list, fn_name: str, *arg, **kwarg):
    _fn_abi = fn_abi(abi, fn_name)
    call_data = parse_call(w3, address, abi, fn_name, *arg, **kwarg)
    _result_decoder = result_decoder(fn_abi_res_types(_fn_abi))
    return CallFunction(Call(address, True, call_data), _result_decoder)
