import Constants
from MultiBalance import MultiBalance
from MultiCall import MultiCall
from utils.token_list import all_tokens, all_chain_token, all_chain_token_dict

MultiChain = Constants.MultiChain


def get_all_balance(wallet_address, tokens):
    balances = {}
    for chain_id, tokens in tokens.items():
        chain = MultiChain(chain_id)
        _chain_balnces = MultiBalance(chain.w3)
        balances[chain_id] = MultiCall(
            [
                _chain_balnces(
                    token.get("address"),
                )
                for token in tokens
            ]
        ).result()
    return balances


if __name__ == "__main__":
    print(all_tokens(MultiChain.FTM)[0])
    import json

    tokens = all_chain_token_dict()
    with open("token.json", "w") as f:
        json.dump(tokens, f)
    print(get_all_balance("0xB49F17514D6F340d7bcdFfC47526C9A3713697e0", tokens))
