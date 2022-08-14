from eth_multicall import MultiChain, MultiCaller, Function
import json
import pytest
from pathlib import Path
from tests.ABI import ABI


with open(Path(__file__).parent.joinpath("tokens.json")) as f:
    TOKEN_LIST = json.load(f)
    # TODO - Check if file is in correct format


def get_all_balance(wallet_address, chain, tokens):
    x = MultiCaller(
        [
            Function(chain.w3, token, ABI.TOKEN, "balanceOf", wallet_address)
            for token in tokens
        ]
    ).call(chain)
    return x


def get_all_balance_via_web3(wallet_address, chain: MultiChain, tokens):
    return [
        chain.w3.eth.contract(token, abi=ABI.TOKEN)
        .functions.balanceOf(wallet_address)
        .call()
        for token in tokens
    ]


@pytest.mark.parametrize("chain", [MultiChain.FTM, MultiChain.BSC, MultiChain.AVAX])
def test_balance(chain, tokens: list = None):
    # chain = MultiChain.BSC
    if tokens is None:
        tokens = TOKEN_LIST.get(str(chain.value))
    assert tokens, "Please Provide Token For Given Chain"
    # with open("tokens_balances.json", "w") as f:
    #     json.dump(
    tokens = tokens[:10]
    # print(tokens[1])
    # logging.info(tokens[11])

    multi_call_response_normal = get_all_balance_via_web3(
        "0xB49F17514D6F340d7bcdFfC47526C9A3713697e0",
        chain,
        [_.get("address") for _ in tokens],
    )
    multi_call_response = get_all_balance(
        "0xB49F17514D6F340d7bcdFfC47526C9A3713697e0",
        chain,
        [_.get("address") for _ in tokens],
    )

    assert (
        multi_call_response == multi_call_response_normal
    ), "W3 response is different from Multicall"
