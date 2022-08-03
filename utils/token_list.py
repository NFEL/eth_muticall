import requests
from web3 import Web3
from string import Template
from enum import Enum
from dataclasses import dataclass, asdict
from Constants import MultiChain


@dataclass(init=True)
class Token:
    address: str
    symbol: str
    decimals: int
    name: str
    chain_id: int
    logo: str = None

    def __hash__(self) -> int:
        return hash(f"{self.chain_id}{self.address}")

    # def __dict__(self) -> dict:
    #     return self.__dict__


blocked_address = ["0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"]


def get_one_inch_tokens(chain_id) -> dict:
    r = set()
    for token in (
        requests.get(
            Template("https://tokens.1inch.io/v1.1/${chain_id}").substitute(
                chain_id=chain_id
            )
        )
        .json()
        .values()
    ):
        token["logo"] = token.pop("logoURI")
        token["address"] = Web3.toChecksumAddress(token["address"])
        if token["address"] in blocked_address:
            continue
        for key in set(token.keys()).difference(
            {"address", "symbol", "decimals", "name", "chain_id", "logo"}
        ):
            token.pop(key)
        token["chain_id"] = chain_id
        r.add(Token(**token))
    return r


_PROVIDERS_MAP = {
    "1inch": {
        "func": get_one_inch_tokens,
        "supported_chains": [
            1,
            4,
            5,
            10,
            42,
            56,
            100,
            128,
            137,
            250,
            42161,
            42220,
            43114,
            31337,
        ],
    },
}


# class TokensList(Enum):


def all_tokens(chain: MultiChain):
    r = set()
    for provider in _PROVIDERS_MAP.values():
        try:
            _r = provider.get("func")(chain.value)
            r = r.union(_r)
        except Exception as e:

            print(chain, e)
    return list(r)


def all_chain_token():
    r = {}
    for chain in MultiChain:
        r[chain.value] = all_tokens(chain)
    return r


def all_chain_token_dict():
    r = {}
    for chain in MultiChain:
        r[chain.value] = [asdict(_) for _ in all_tokens(chain)]
    return r
