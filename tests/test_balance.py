from MultiChain import MultiChain
from MultiCall import MultiCaller
import Function
from ABI import ABI

with open("tokens.json") as f:
    TOKEN_LIST = json.load(f)
    # TODO - Check if file is in correct format


def get_all_balance(wallet_address, chain, tokens):
    x = MultiCaller(
        [
            Function.compile(chain.w3, token, ABI.TOKEN, "balanceOf", wallet_address)
            for token in tokens
        ]
    ).call(chain)
    return x


if __name__ == "__main__":

    import json

    chain = MultiChain.BSC
    tokens = TOKEN_LIST.get(str(chain.value))
    assert tokens, "Please Provide Token For Given Chain"
    with open("tokens_balances.json", "w") as f:
        json.dump(
            dict(
                zip(
                    map(lambda x: x.get("address"), tokens),
                    get_all_balance(
                        "0xB49F17514D6F340d7bcdFfC47526C9A3713697e0",
                        chain,
                        [_.get('address') for _ in tokens],
                    ),
                )
            ),
            f,
        )
