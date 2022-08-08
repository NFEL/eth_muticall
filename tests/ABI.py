from dataclasses import dataclass


@dataclass
class ABI:
    ## TODO Add this
    APPROVE = []
    ALLOWANCE = []
    MULTI_CALL_V3 = [{"inputs":[{"components":[{"internalType":"address","name":"target","type":"address"},{"internalType":"bytes","name":"callData","type":"bytes"}],"internalType":"struct Multicall3.Call[]","name":"calls","type":"tuple[]"}],"name":"aggregate","outputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"},{"internalType":"bytes[]","name":"returnData","type":"bytes[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"target","type":"address"},{"internalType":"bool","name":"allowFailure","type":"bool"},{"internalType":"bytes","name":"callData","type":"bytes"}],"internalType":"struct Multicall3.Call3[]","name":"calls","type":"tuple[]"}],"name":"aggregate3","outputs":[{"components":[{"internalType":"bool","name":"success","type":"bool"},{"internalType":"bytes","name":"returnData","type":"bytes"}],"internalType":"struct Multicall3.Result[]","name":"returnData","type":"tuple[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"target","type":"address"},{"internalType":"bool","name":"allowFailure","type":"bool"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"bytes","name":"callData","type":"bytes"}],"internalType":"struct Multicall3.Call3Value[]","name":"calls","type":"tuple[]"}],"name":"aggregate3Value","outputs":[{"components":[{"internalType":"bool","name":"success","type":"bool"},{"internalType":"bytes","name":"returnData","type":"bytes"}],"internalType":"struct Multicall3.Result[]","name":"returnData","type":"tuple[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"target","type":"address"},{"internalType":"bytes","name":"callData","type":"bytes"}],"internalType":"struct Multicall3.Call[]","name":"calls","type":"tuple[]"}],"name":"blockAndAggregate","outputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"},{"internalType":"bytes32","name":"blockHash","type":"bytes32"},{"components":[{"internalType":"bool","name":"success","type":"bool"},{"internalType":"bytes","name":"returnData","type":"bytes"}],"internalType":"struct Multicall3.Result[]","name":"returnData","type":"tuple[]"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"getBasefee","outputs":[{"internalType":"uint256","name":"basefee","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"}],"name":"getBlockHash","outputs":[{"internalType":"bytes32","name":"blockHash","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getBlockNumber","outputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getChainId","outputs":[{"internalType":"uint256","name":"chainid","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getCurrentBlockCoinbase","outputs":[{"internalType":"address","name":"coinbase","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getCurrentBlockDifficulty","outputs":[{"internalType":"uint256","name":"difficulty","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getCurrentBlockGasLimit","outputs":[{"internalType":"uint256","name":"gaslimit","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getCurrentBlockTimestamp","outputs":[{"internalType":"uint256","name":"timestamp","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"addr","type":"address"}],"name":"getEthBalance","outputs":[{"internalType":"uint256","name":"balance","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLastBlockHash","outputs":[{"internalType":"bytes32","name":"blockHash","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bool","name":"requireSuccess","type":"bool"},{"components":[{"internalType":"address","name":"target","type":"address"},{"internalType":"bytes","name":"callData","type":"bytes"}],"internalType":"struct Multicall3.Call[]","name":"calls","type":"tuple[]"}],"name":"tryAggregate","outputs":[{"components":[{"internalType":"bool","name":"success","type":"bool"},{"internalType":"bytes","name":"returnData","type":"bytes"}],"internalType":"struct Multicall3.Result[]","name":"returnData","type":"tuple[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"bool","name":"requireSuccess","type":"bool"},{"components":[{"internalType":"address","name":"target","type":"address"},{"internalType":"bytes","name":"callData","type":"bytes"}],"internalType":"struct Multicall3.Call[]","name":"calls","type":"tuple[]"}],"name":"tryBlockAndAggregate","outputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"},{"internalType":"bytes32","name":"blockHash","type":"bytes32"},{"components":[{"internalType":"bool","name":"success","type":"bool"},{"internalType":"bytes","name":"returnData","type":"bytes"}],"internalType":"struct Multicall3.Result[]","name":"returnData","type":"tuple[]"}],"stateMutability":"payable","type":"function"}]
    MARKER_MULTI_CALL = [{"inputs":[{"components":[{"internalType":"address","name":"target","type":"address"},{"internalType":"bytes","name":"callData","type":"bytes"}],"internalType":"struct Multicall.Call[]","name":"calls","type":"tuple[]"}],"name":"aggregate","outputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"},{"internalType":"bytes[]","name":"returnData","type":"bytes[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"}],"name":"getBlockHash","outputs":[{"internalType":"bytes32","name":"blockHash","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getCurrentBlockCoinbase","outputs":[{"internalType":"address","name":"coinbase","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getCurrentBlockDifficulty","outputs":[{"internalType":"uint256","name":"difficulty","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getCurrentBlockGasLimit","outputs":[{"internalType":"uint256","name":"gaslimit","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getCurrentBlockTimestamp","outputs":[{"internalType":"uint256","name":"timestamp","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"addr","type":"address"}],"name":"getEthBalance","outputs":[{"internalType":"uint256","name":"balance","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getLastBlockHash","outputs":[{"internalType":"bytes32","name":"blockHash","type":"bytes32"}],"stateMutability":"view","type":"function"}]
    UNISWAP_MULTI_CALL = [{"inputs":[],"name":"getCurrentBlockTimestamp","outputs":[{"internalType":"uint256","name":"timestamp","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"addr","type":"address"}],"name":"getEthBalance","outputs":[{"internalType":"uint256","name":"balance","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"target","type":"address"},{"internalType":"uint256","name":"gasLimit","type":"uint256"},{"internalType":"bytes","name":"callData","type":"bytes"}],"internalType":"struct UniswapInterfaceMulticall.Call[]","name":"calls","type":"tuple[]"}],"name":"multicall","outputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"},{"components":[{"internalType":"bool","name":"success","type":"bool"},{"internalType":"uint256","name":"gasUsed","type":"uint256"},{"internalType":"bytes","name":"returnData","type":"bytes"}],"internalType":"struct UniswapInterfaceMulticall.Result[]","name":"returnData","type":"tuple[]"}],"stateMutability":"nonpayable","type":"function"}] 
    UNISWAP_ROUTER = [{"inputs":[{"internalType":"address","name":"_factory","type":"address"},{"internalType":"address","name":"_WETH","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"WETH","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"amountADesired","type":"uint256"},{"internalType":"uint256","name":"amountBDesired","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amountTokenDesired","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountIn","outputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountOut","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsIn","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsOut","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"reserveA","type":"uint256"},{"internalType":"uint256","name":"reserveB","type":"uint256"}],"name":"quote","outputs":[{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETHSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermit","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermitSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityWithPermit","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapETHForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETHSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]
    TOKEN = [
        {
            "constant": True,
            "inputs": [],
            "name": "name",
            "outputs": [{"name": "", "type": "string"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": False,
            "inputs": [
                {"name": "_spender", "type": "address"},
                {"name": "_value", "type": "uint256"},
            ],
            "name": "approve",
            "outputs": [{"name": "", "type": "bool"}],
            "payable": False,
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [],
            "name": "totalSupply",
            "outputs": [{"name": "", "type": "uint256"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": False,
            "inputs": [
                {"name": "_from", "type": "address"},
                {"name": "_to", "type": "address"},
                {"name": "_value", "type": "uint256"},
            ],
            "name": "transferFrom",
            "outputs": [{"name": "", "type": "bool"}],
            "payable": False,
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [],
            "name": "decimals",
            "outputs": [{"name": "", "type": "uint8"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [{"name": "_owner", "type": "address"}],
            "name": "balanceOf",
            "outputs": [{"name": "balance", "type": "uint256"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [],
            "name": "symbol",
            "outputs": [{"name": "", "type": "string"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": False,
            "inputs": [
                {"name": "_to", "type": "address"},
                {"name": "_value", "type": "uint256"},
            ],
            "name": "transfer",
            "outputs": [{"name": "", "type": "bool"}],
            "payable": False,
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [
                {"name": "_owner", "type": "address"},
                {"name": "_spender", "type": "address"},
            ],
            "name": "allowance",
            "outputs": [{"name": "", "type": "uint256"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {"payable": True, "stateMutability": "payable", "type": "fallback"},
        {
            "anonymous": False,
            "inputs": [
                {"indexed": True, "name": "owner", "type": "address"},
                {"indexed": True, "name": "spender", "type": "address"},
                {"indexed": False, "name": "value", "type": "uint256"},
            ],
            "name": "Approval",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {"indexed": True, "name": "from", "type": "address"},
                {"indexed": True, "name": "to", "type": "address"},
                {"indexed": False, "name": "value", "type": "uint256"},
            ],
            "name": "Transfer",
            "type": "event",
        },
    ]
    PAIR = [
        {"inputs": [], "stateMutability": "nonpayable", "type": "constructor"},
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "owner",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "spender",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "value",
                    "type": "uint256",
                },
            ],
            "name": "Approval",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "sender",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount0",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount1",
                    "type": "uint256",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "to",
                    "type": "address",
                },
            ],
            "name": "Burn",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "sender",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount0",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount1",
                    "type": "uint256",
                },
            ],
            "name": "Mint",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "sender",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount0In",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount1In",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount0Out",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount1Out",
                    "type": "uint256",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "to",
                    "type": "address",
                },
            ],
            "name": "Swap",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "uint112",
                    "name": "reserve0",
                    "type": "uint112",
                },
                {
                    "indexed": False,
                    "internalType": "uint112",
                    "name": "reserve1",
                    "type": "uint112",
                },
            ],
            "name": "Sync",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "from",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "to",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "value",
                    "type": "uint256",
                },
            ],
            "name": "Transfer",
            "type": "event",
        },
        {
            "inputs": [],
            "name": "DOMAIN_SEPARATOR",
            "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "MINIMUM_LIQUIDITY",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "PERMIT_TYPEHASH",
            "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "", "type": "address"},
                {"internalType": "address", "name": "", "type": "address"},
            ],
            "name": "allowance",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "spender", "type": "address"},
                {"internalType": "uint256", "name": "value", "type": "uint256"},
            ],
            "name": "approve",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "", "type": "address"}],
            "name": "balanceOf",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "to", "type": "address"}],
            "name": "burn",
            "outputs": [
                {"internalType": "uint256", "name": "amount0", "type": "uint256"},
                {"internalType": "uint256", "name": "amount1", "type": "uint256"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "decimals",
            "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "factory",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getReserves",
            "outputs": [
                {"internalType": "uint112", "name": "_reserve0", "type": "uint112"},
                {"internalType": "uint112", "name": "_reserve1", "type": "uint112"},
                {
                    "internalType": "uint32",
                    "name": "_blockTimestampLast",
                    "type": "uint32",
                },
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_token0", "type": "address"},
                {"internalType": "address", "name": "_token1", "type": "address"},
            ],
            "name": "initialize",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "kLast",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "to", "type": "address"}],
            "name": "mint",
            "outputs": [
                {"internalType": "uint256", "name": "liquidity", "type": "uint256"}
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "name",
            "outputs": [{"internalType": "string", "name": "", "type": "string"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "", "type": "address"}],
            "name": "nonces",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "owner", "type": "address"},
                {"internalType": "address", "name": "spender", "type": "address"},
                {"internalType": "uint256", "name": "value", "type": "uint256"},
                {"internalType": "uint256", "name": "deadline", "type": "uint256"},
                {"internalType": "uint8", "name": "v", "type": "uint8"},
                {"internalType": "bytes32", "name": "r", "type": "bytes32"},
                {"internalType": "bytes32", "name": "s", "type": "bytes32"},
            ],
            "name": "permit",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "price0CumulativeLast",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "price1CumulativeLast",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "to", "type": "address"}],
            "name": "skim",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "amount0Out", "type": "uint256"},
                {"internalType": "uint256", "name": "amount1Out", "type": "uint256"},
                {"internalType": "address", "name": "to", "type": "address"},
                {"internalType": "bytes", "name": "data", "type": "bytes"},
            ],
            "name": "swap",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "symbol",
            "outputs": [{"internalType": "string", "name": "", "type": "string"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "sync",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "token0",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "token1",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "totalSupply",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "to", "type": "address"},
                {"internalType": "uint256", "name": "value", "type": "uint256"},
            ],
            "name": "transfer",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "from", "type": "address"},
                {"internalType": "address", "name": "to", "type": "address"},
                {"internalType": "uint256", "name": "value", "type": "uint256"},
            ],
            "name": "transferFrom",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
    ]
    UNISWAP_FACTORY = [
        {
            "constant": True,
            "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "name": "allPairs",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [],
            "name": "allPairsLength",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [
                {"internalType": "address", "name": "", "type": "address"},
                {"internalType": "address", "name": "", "type": "address"},
            ],
            "name": "getPair",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
    ]
    UNISWAP_PAIR = [
        {
            "constant": True,
            "inputs": [],
            "name": "getReserves",
            "outputs": [
                {"internalType": "uint112", "name": "_reserve0", "type": "uint112"},
                {"internalType": "uint112", "name": "_reserve1", "type": "uint112"},
                {
                    "internalType": "uint32",
                    "name": "_blockTimestampLast",
                    "type": "uint32",
                },
            ],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [],
            "name": "token0",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [],
            "name": "token1",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
    ]
    SOULSWAP_FACTORY = [
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "user",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "feeToSetter",
                    "type": "address",
                },
            ],
            "name": "FeeToSetter",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "token0",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "token1",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "pair",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256",
                },
            ],
            "name": "PairCreated",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "user",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "feeTo",
                    "type": "address",
                },
            ],
            "name": "SetFeeTo",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "user",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "migrator",
                    "type": "address",
                },
            ],
            "name": "SetMigrator",
            "type": "event",
        },
        {
            "constant": True,
            "inputs": [],
            "name": "INIT_CODE_PAIR_HASH",
            "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "name": "allPairs",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": False,
            "inputs": [
                {"internalType": "address", "name": "tokenA", "type": "address"},
                {"internalType": "address", "name": "tokenB", "type": "address"},
            ],
            "name": "createPair",
            "outputs": [{"internalType": "address", "name": "pair", "type": "address"}],
            "payable": False,
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [],
            "name": "feeTo",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [],
            "name": "feeToSetter",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [
                {"internalType": "address", "name": "", "type": "address"},
                {"internalType": "address", "name": "", "type": "address"},
            ],
            "name": "getPair",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [],
            "name": "migrator",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": False,
            "inputs": [
                {"internalType": "address", "name": "_feeTo", "type": "address"}
            ],
            "name": "setFeeTo",
            "outputs": [],
            "payable": False,
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "constant": False,
            "inputs": [
                {"internalType": "address", "name": "_feeToSetter", "type": "address"}
            ],
            "name": "setFeeToSetter",
            "outputs": [],
            "payable": False,
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "constant": False,
            "inputs": [
                {"internalType": "address", "name": "_migrator", "type": "address"}
            ],
            "name": "setMigrator",
            "outputs": [],
            "payable": False,
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [],
            "name": "totalPairs",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
    ]
    SPARTAN_FACTORY = [
        {
            "inputs": [],
            "name": "BASE",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "allPools",
            "outputs": [
                {"internalType": "address[]", "name": "_allPools", "type": "address[]"}
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "allTokens",
            "outputs": [
                {"internalType": "address[]", "name": "_allTokens", "type": "address[]"}
            ],
            "stateMutability": "view",
            "type": "function",
        },
    ]
    SPARTAN_PAIR = [
        {
            "inputs": [],
            "name": "baseAmountPooled",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "tokenAmountPooled",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
    ]
    MOONSWAP_PAIR = [
        {
            "constant": True,
            "inputs": [],
            "name": "token0",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [],
            "name": "token1",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "fee",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "slippageFee",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "contract IERC20", "name": "token", "type": "address"}
            ],
            "name": "getBalanceForAddition",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
    ]
    MOONSWAP_FACTORY = [
        {
            "inputs": [],
            "name": "isActive",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getAllPools",
            "outputs": [
                {
                    "internalType": "contract Mooniswap[]",
                    "name": "",
                    "type": "address[]",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
    ]
    MDEX_FACTORY = [
        {
            "constant": True,
            "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "name": "allPairs",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [],
            "name": "allPairsLength",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [{"internalType": "address", "name": "pair", "type": "address"}],
            "name": "getPairFees",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
    ]
    AcryptoS_PAIR = [
        {
            "name": "A",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 5199,
        },
        {
            "name": "fee",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 2111,
        },
        {
            "name": "balances",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [{"type": "uint256", "name": "arg0"}],
            "stateMutability": "view",
            "type": "function",
            "gas": 2190,
        },
        {
            "name": "lp_token",
            "outputs": [{"type": "address", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 2231,
        },
    ]
    ELLIPSIS_PAIR = [
        {
            "name": "A",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 5199,
        },
        {
            "name": "fee",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 2111,
        },
        {
            "name": "balances",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [{"type": "uint256", "name": "arg0"}],
            "stateMutability": "view",
            "type": "function",
            "gas": 2190,
        },
        {
            "name": "lp_token",
            "outputs": [{"type": "address", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 2231,
        },
    ]
    VPEG_FACTORY = [
        {
            "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "name": "allPools",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "allPoolsLength",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
    ]
    VPEG_PAIR = [
        {
            "inputs": [{"internalType": "address", "name": "index", "type": "uint8"}],
            "name": "getToken",
            "outputs": [
                {"internalType": "contract IERC20", "name": "", "type": "address"}
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "swapStorage",
            "outputs": [
                {"internalType": "uint256", "name": "initialA", "type": "uint256"},
                {"internalType": "uint256", "name": "futureA", "type": "uint256"},
                {"internalType": "uint256", "name": "initialATime", "type": "uint256"},
                {"internalType": "uint256", "name": "futureATime", "type": "uint256"},
                {"internalType": "uint256", "name": "swapFee", "type": "uint256"},
                {"internalType": "uint256", "name": "adminFee", "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "defaultWithdrawFee",
                    "type": "uint256",
                },
                {
                    "internalType": "contract LPToken",
                    "name": "lpToken",
                    "type": "address",
                },
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getTokenLength",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getA",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "uint8", "name": "index", "type": "uint8"}],
            "name": "getTokenBalance",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getPoolTokens",
            "outputs": [
                {"internalType": "contract IERC20[]", "name": "", "type": "address[]"}
            ],
            "stateMutability": "view",
            "type": "function",
        },
    ]
    DODO_V1_FACTORY = [
        {
            "inputs": [],
            "name": "getDODOs",
            "outputs": [{"internalType": "address[]", "name": "", "type": "address[]"}],
            "stateMutability": "view",
            "type": "function",
        }
    ]
    DODO_V1_PAIR = [
        {
            "inputs": [],
            "name": "_K_",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "_R_STATUS_",
            "outputs": [
                {"internalType": "enum Types.RStatus", "name": "", "type": "uint8"}
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "_BASE_BALANCE_",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "_QUOTE_BALANCE_",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "_LP_FEE_RATE_",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "_MT_FEE_RATE_",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getMidPrice",
            "outputs": [
                {"internalType": "uint256", "name": "midPrice", "type": "uint256"}
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getOraclePrice",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getExpectedTarget",
            "outputs": [
                {"internalType": "uint256", "name": "baseTarget", "type": "uint256"},
                {"internalType": "uint256", "name": "quoteTarget", "type": "uint256"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "_BASE_TOKEN_",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "_QUOTE_TOKEN_",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
    ]
    DODO_V2_FACTORY = {
        "CPfactory": [
            {
                "inputs": [
                    {"internalType": "address", "name": "token0", "type": "address"},
                    {"internalType": "address", "name": "token1", "type": "address"},
                ],
                "name": "getCrowdPoolingBidirection",
                "outputs": [
                    {
                        "internalType": "address[]",
                        "name": "baseToken0Pools",
                        "type": "address[]",
                    },
                    {
                        "internalType": "address[]",
                        "name": "baseToken1Pools",
                        "type": "address[]",
                    },
                ],
                "stateMutability": "view",
                "type": "function",
            }
        ],
        "Dfactory": [
            {
                "inputs": [
                    {"internalType": "address", "name": "token0", "type": "address"},
                    {"internalType": "address", "name": "token1", "type": "address"},
                ],
                "name": "getDODOPoolBidirection",
                "outputs": [
                    {
                        "internalType": "address[]",
                        "name": "baseToken0Pool",
                        "type": "address[]",
                    },
                    {
                        "internalType": "address[]",
                        "name": "baseToken1Pool",
                        "type": "address[]",
                    },
                ],
                "stateMutability": "view",
                "type": "function",
            }
        ],
    }
    DODO_V2_PAIR = [
        {
            "inputs": [],
            "name": "getPMMStateForCall",
            "outputs": [
                {"internalType": "uint256", "name": "i", "type": "uint256"},
                {"internalType": "uint256", "name": "K", "type": "uint256"},
                {"internalType": "uint256", "name": "B", "type": "uint256"},
                {"internalType": "uint256", "name": "Q", "type": "uint256"},
                {"internalType": "uint256", "name": "B0", "type": "uint256"},
                {"internalType": "uint256", "name": "Q0", "type": "uint256"},
                {"internalType": "uint256", "name": "R", "type": "uint256"},
            ],
            "stateMutability": "view",
            "type": "function",
        }
    ]
    EVO_BRIDGE = [
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "uint256",
                    "name": "id",
                    "type": "uint256",
                },
                {
                    "indexed": True,
                    "internalType": "uint8",
                    "name": "dstFrom",
                    "type": "uint8",
                },
            ],
            "name": "OrderCompleted",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "uint256",
                    "name": "id",
                    "type": "uint256",
                },
                {
                    "components": [
                        {"internalType": "uint256", "name": "id", "type": "uint256"},
                        {"internalType": "uint8", "name": "tokenId", "type": "uint8"},
                        {
                            "internalType": "address",
                            "name": "sender",
                            "type": "address",
                        },
                        {
                            "internalType": "bytes32",
                            "name": "target",
                            "type": "bytes32",
                        },
                        {
                            "internalType": "uint256",
                            "name": "amount",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "feeAmount",
                            "type": "uint256",
                        },
                        {"internalType": "uint8", "name": "decimals", "type": "uint8"},
                        {
                            "internalType": "uint8",
                            "name": "destination",
                            "type": "uint8",
                        },
                        {
                            "internalType": "address",
                            "name": "tokenIn",
                            "type": "address",
                        },
                        {
                            "internalType": "bytes32",
                            "name": "tokenOut",
                            "type": "bytes32",
                        },
                    ],
                    "indexed": False,
                    "internalType": "struct Bridge.Order",
                    "name": "order",
                    "type": "tuple",
                },
            ],
            "name": "OrderCreated",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "previousOwner",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "newOwner",
                    "type": "address",
                },
            ],
            "name": "OwnershipTransferred",
            "type": "event",
        },
        {
            "inputs": [{"internalType": "address", "name": "", "type": "address"}],
            "name": "addresses",
            "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256[]", "name": "_orderIds", "type": "uint256[]"}
            ],
            "name": "closeManyOrders",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "orderId", "type": "uint256"}
            ],
            "name": "closeOrder",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "components": [
                        {
                            "internalType": "uint256",
                            "name": "orderId",
                            "type": "uint256",
                        },
                        {"internalType": "uint8", "name": "dstFrom", "type": "uint8"},
                        {"internalType": "uint8", "name": "tokenId", "type": "uint8"},
                        {
                            "internalType": "address payable",
                            "name": "to",
                            "type": "address",
                        },
                        {
                            "internalType": "uint256",
                            "name": "amount",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "decimals",
                            "type": "uint256",
                        },
                        {
                            "internalType": "contract ERC20",
                            "name": "tokenOut",
                            "type": "address",
                        },
                        {
                            "internalType": "address[]",
                            "name": "swapPath",
                            "type": "address[]",
                        },
                    ],
                    "internalType": "struct Bridge.CompleteParams[]",
                    "name": "params",
                    "type": "tuple[]",
                }
            ],
            "name": "completeManyOrders",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "orderId", "type": "uint256"},
                {"internalType": "uint8", "name": "dstFrom", "type": "uint8"},
                {"internalType": "uint8", "name": "tokenId", "type": "uint8"},
                {"internalType": "address payable", "name": "to", "type": "address"},
                {"internalType": "uint256", "name": "amount", "type": "uint256"},
                {"internalType": "uint256", "name": "decimals", "type": "uint256"},
                {
                    "internalType": "contract ERC20",
                    "name": "tokenOut",
                    "type": "address",
                },
                {"internalType": "address[]", "name": "swapPath", "type": "address[]"},
            ],
            "name": "completeOrder",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
            "name": "completed",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint8", "name": "", "type": "uint8"},
                {"internalType": "uint8", "name": "", "type": "uint8"},
            ],
            "name": "configs",
            "outputs": [
                {"internalType": "uint16", "name": "fee", "type": "uint16"},
                {"internalType": "uint256", "name": "feeBase", "type": "uint256"},
                {"internalType": "uint256", "name": "minAmount", "type": "uint256"},
                {"internalType": "uint256", "name": "maxAmount", "type": "uint256"},
                {
                    "internalType": "bool",
                    "name": "directTransferAllowed",
                    "type": "bool",
                },
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint8", "name": "tokenId", "type": "uint8"},
                {"internalType": "uint256", "name": "amount", "type": "uint256"},
                {"internalType": "uint8", "name": "destination", "type": "uint8"},
                {"internalType": "bytes32", "name": "target", "type": "bytes32"},
            ],
            "name": "create",
            "outputs": [],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "contract ERC20",
                    "name": "tokenIn",
                    "type": "address",
                },
                {"internalType": "uint256", "name": "amount", "type": "uint256"},
                {"internalType": "uint8", "name": "destination", "type": "uint8"},
                {"internalType": "bytes32", "name": "target", "type": "bytes32"},
                {"internalType": "bytes32", "name": "tokenOut", "type": "bytes32"},
                {"internalType": "address[]", "name": "swapPath", "type": "address[]"},
            ],
            "name": "createWithSwap",
            "outputs": [],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "orderId", "type": "uint256"},
                {"internalType": "uint8", "name": "dstFrom", "type": "uint8"},
            ],
            "name": "isCompleted",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "listOrders",
            "outputs": [
                {
                    "components": [
                        {"internalType": "uint256", "name": "id", "type": "uint256"},
                        {"internalType": "uint8", "name": "tokenId", "type": "uint8"},
                        {
                            "internalType": "address",
                            "name": "sender",
                            "type": "address",
                        },
                        {
                            "internalType": "bytes32",
                            "name": "target",
                            "type": "bytes32",
                        },
                        {
                            "internalType": "uint256",
                            "name": "amount",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "feeAmount",
                            "type": "uint256",
                        },
                        {"internalType": "uint8", "name": "decimals", "type": "uint8"},
                        {
                            "internalType": "uint8",
                            "name": "destination",
                            "type": "uint8",
                        },
                        {
                            "internalType": "address",
                            "name": "tokenIn",
                            "type": "address",
                        },
                        {
                            "internalType": "bytes32",
                            "name": "tokenOut",
                            "type": "bytes32",
                        },
                    ],
                    "internalType": "struct Bridge.Order[]",
                    "name": "",
                    "type": "tuple[]",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "listTokensNames",
            "outputs": [{"internalType": "string[]", "name": "", "type": "string[]"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "name": "orders",
            "outputs": [
                {"internalType": "uint256", "name": "id", "type": "uint256"},
                {"internalType": "uint8", "name": "tokenId", "type": "uint8"},
                {"internalType": "address", "name": "sender", "type": "address"},
                {"internalType": "bytes32", "name": "target", "type": "bytes32"},
                {"internalType": "uint256", "name": "amount", "type": "uint256"},
                {"internalType": "uint256", "name": "feeAmount", "type": "uint256"},
                {"internalType": "uint8", "name": "decimals", "type": "uint8"},
                {"internalType": "uint8", "name": "destination", "type": "uint8"},
                {"internalType": "address", "name": "tokenIn", "type": "address"},
                {"internalType": "bytes32", "name": "tokenOut", "type": "bytes32"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "owner",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "renounceOwnership",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint8", "name": "tokenId", "type": "uint8"},
                {"internalType": "uint256", "name": "bonus", "type": "uint256"},
            ],
            "name": "setBonus",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint8", "name": "tokenId", "type": "uint8"},
                {"internalType": "uint8", "name": "destination", "type": "uint8"},
                {
                    "components": [
                        {"internalType": "uint16", "name": "fee", "type": "uint16"},
                        {
                            "internalType": "uint256",
                            "name": "feeBase",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "minAmount",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "maxAmount",
                            "type": "uint256",
                        },
                        {
                            "internalType": "bool",
                            "name": "directTransferAllowed",
                            "type": "bool",
                        },
                    ],
                    "internalType": "struct Bridge.Config",
                    "name": "config",
                    "type": "tuple",
                },
            ],
            "name": "setConfig",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint8", "name": "tokenId", "type": "uint8"},
                {"internalType": "uint16", "name": "defaultFee", "type": "uint16"},
            ],
            "name": "setDefaultFee",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint8", "name": "tokenId", "type": "uint8"},
                {
                    "internalType": "uint256",
                    "name": "defaultFeeBase",
                    "type": "uint256",
                },
                {"internalType": "uint8", "name": "inputDecimals", "type": "uint8"},
            ],
            "name": "setDefaultFeeBase",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint8", "name": "tokenId", "type": "uint8"},
                {
                    "internalType": "uint256",
                    "name": "defaultMaxAmount",
                    "type": "uint256",
                },
                {"internalType": "uint8", "name": "inputDecimals", "type": "uint8"},
            ],
            "name": "setDefaultMaxAmount",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint8", "name": "tokenId", "type": "uint8"},
                {
                    "internalType": "uint256",
                    "name": "defaultMinAmount",
                    "type": "uint256",
                },
                {"internalType": "uint8", "name": "inputDecimals", "type": "uint8"},
            ],
            "name": "setDefaultMinAmount",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint8", "name": "tokenId", "type": "uint8"},
                {"internalType": "uint8", "name": "destination", "type": "uint8"},
                {
                    "internalType": "bool",
                    "name": "directTransferAllowed",
                    "type": "bool",
                },
            ],
            "name": "setDirectTransferAllowed",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint8", "name": "tokenId", "type": "uint8"},
                {"internalType": "uint8", "name": "destination", "type": "uint8"},
                {"internalType": "uint16", "name": "fee", "type": "uint16"},
            ],
            "name": "setFee",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint8", "name": "tokenId", "type": "uint8"},
                {"internalType": "uint8", "name": "destination", "type": "uint8"},
                {"internalType": "uint256", "name": "feeBase", "type": "uint256"},
                {"internalType": "uint8", "name": "inputDecimals", "type": "uint8"},
            ],
            "name": "setFeeBase",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint8", "name": "tokenId", "type": "uint8"},
                {"internalType": "address", "name": "feeTarget", "type": "address"},
            ],
            "name": "setFeeTarget",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint8", "name": "tokenId", "type": "uint8"},
                {"internalType": "uint8", "name": "destination", "type": "uint8"},
                {"internalType": "uint256", "name": "maxAmount", "type": "uint256"},
                {"internalType": "uint8", "name": "inputDecimals", "type": "uint8"},
            ],
            "name": "setMaxAmount",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint8", "name": "tokenId", "type": "uint8"},
                {"internalType": "uint8", "name": "destination", "type": "uint8"},
                {"internalType": "uint256", "name": "minAmount", "type": "uint256"},
                {"internalType": "uint8", "name": "inputDecimals", "type": "uint8"},
            ],
            "name": "setMinAmount",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "bool", "name": "allowed", "type": "bool"},
                {"internalType": "uint8", "name": "tokenId", "type": "uint8"},
            ],
            "name": "setSwapSettings",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "contract IBridgeSwap",
                    "name": "newSwapper",
                    "type": "address",
                }
            ],
            "name": "setSwapper",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint8", "name": "tokenId", "type": "uint8"},
                {"internalType": "contract ERC20", "name": "token", "type": "address"},
                {"internalType": "address", "name": "feeTarget", "type": "address"},
                {"internalType": "uint16", "name": "defaultFee", "type": "uint16"},
                {
                    "internalType": "uint256",
                    "name": "defaultFeeBase",
                    "type": "uint256",
                },
                {
                    "internalType": "uint256",
                    "name": "defaultMinAmount",
                    "type": "uint256",
                },
                {
                    "internalType": "uint256",
                    "name": "defaultMaxAmount",
                    "type": "uint256",
                },
                {"internalType": "uint8", "name": "inputDecimals", "type": "uint8"},
                {"internalType": "uint256", "name": "bonus", "type": "uint256"},
            ],
            "name": "setToken",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "user", "type": "address"},
                {"internalType": "bool", "name": "isTrusted", "type": "bool"},
            ],
            "name": "setTrusted",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "swapDefaultTokenId",
            "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "swapper",
            "outputs": [
                {"internalType": "contract IBridgeSwap", "name": "", "type": "address"}
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "swapsAllowed",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "uint8", "name": "", "type": "uint8"}],
            "name": "tokens",
            "outputs": [
                {"internalType": "contract ERC20", "name": "token", "type": "address"},
                {"internalType": "address", "name": "feeTarget", "type": "address"},
                {"internalType": "uint16", "name": "defaultFee", "type": "uint16"},
                {
                    "internalType": "uint256",
                    "name": "defaultFeeBase",
                    "type": "uint256",
                },
                {
                    "internalType": "uint256",
                    "name": "defaultMinAmount",
                    "type": "uint256",
                },
                {
                    "internalType": "uint256",
                    "name": "defaultMaxAmount",
                    "type": "uint256",
                },
                {"internalType": "uint256", "name": "bonus", "type": "uint256"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "newOwner", "type": "address"}
            ],
            "name": "transferOwnership",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "", "type": "address"}],
            "name": "trusted",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint8", "name": "tokenId", "type": "uint8"},
                {"internalType": "address payable", "name": "to", "type": "address"},
                {"internalType": "uint256", "name": "amount", "type": "uint256"},
                {"internalType": "uint8", "name": "inputDecimals", "type": "uint8"},
            ],
            "name": "withdraw",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "contract ERC20", "name": "token", "type": "address"},
                {"internalType": "address payable", "name": "to", "type": "address"},
                {"internalType": "uint256", "name": "amount", "type": "uint256"},
                {"internalType": "uint8", "name": "inputDecimals", "type": "uint8"},
            ],
            "name": "withdrawToken",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {"stateMutability": "payable", "type": "receive"},
    ]
    OUR_BSC_ROUTER = [
        {
            "inputs": [
                {"internalType": "address", "name": "_token", "type": "address"},
                {"internalType": "address", "name": "_dexRouter", "type": "address"},
                {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            ],
            "name": "_approve",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address[]", "name": "_tokens", "type": "address[]"}
            ],
            "name": "_approveInfinity",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "newOwner", "type": "address"}
            ],
            "name": "changeOwner",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "components": [
                        {
                            "internalType": "uint256",
                            "name": "minAmountOut",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "amountIn",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256[]",
                            "name": "amountsIn",
                            "type": "uint256[]",
                        },
                        {
                            "internalType": "uint16[][]",
                            "name": "dexs",
                            "type": "uint16[][]",
                        },
                        {
                            "internalType": "address[][]",
                            "name": "paths",
                            "type": "address[][]",
                        },
                        {
                            "internalType": "address[][]",
                            "name": "pool",
                            "type": "address[][]",
                        },
                        {
                            "internalType": "bool",
                            "name": "withDrawFlag",
                            "type": "bool",
                        },
                    ],
                    "internalType": "struct Proxy.Swap",
                    "name": "route",
                    "type": "tuple",
                }
            ],
            "name": "exchange",
            "outputs": [
                {"internalType": "uint256", "name": "_amountOut", "type": "uint256"}
            ],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "oldOwner",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "newOwner",
                    "type": "address",
                },
            ],
            "name": "OwnerSet",
            "type": "event",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_token", "type": "address"}
            ],
            "name": "transfertome",
            "outputs": [
                {"internalType": "uint256", "name": "_tknBalance", "type": "uint256"}
            ],
            "stateMutability": "payable",
            "type": "function",
        },
        {"stateMutability": "payable", "type": "receive"},
        {
            "inputs": [
                {"internalType": "address", "name": "_token", "type": "address"},
                {"internalType": "address", "name": "_dexRouter", "type": "address"},
            ],
            "name": "_allowance",
            "outputs": [
                {"internalType": "uint256", "name": "_amount", "type": "uint256"}
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "AcryptoS",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "acryptosstablecount",
            "outputs": [{"internalType": "uint16", "name": "", "type": "uint16"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "name": "allRouters",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "Apeswap",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "BakerySwap",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "BNB",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "DODOV1",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "DODOV2",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "Ellipsis",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "ellipsisstablcount",
            "outputs": [{"internalType": "uint16", "name": "", "type": "uint16"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getOwner",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "IcurveVyper",
            "outputs": [{"internalType": "string", "name": "", "type": "string"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "JulSwap",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "MDex",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "PancakeSwapV1",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "PancakeSwapV2",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "StreetSwap",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "SushiSwap",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "SwipSwap",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "TwindexSwap",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "ValueLiquidityPool",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "WaultSwap",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "WBNB",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
    ]
    BATCH_READ = [
        {
            "inputs": [{"internalType": "address", "name": "_WFTM", "type": "address"}],
            "stateMutability": "nonpayable",
            "type": "constructor",
        },
        {
            "inputs": [],
            "name": "DIV_PERCISION",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "Owner",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "address[]",
                    "name": "selectedPath",
                    "type": "address[]",
                },
                {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
                {"internalType": "uint256", "name": "amount_out", "type": "uint256"},
            ],
            "name": "_calculatePriceImpact",
            "outputs": [
                {"internalType": "uint256", "name": "price", "type": "uint256"},
                {"internalType": "int256", "name": "priceImpact", "type": "int256"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "bytes32[]", "name": "poolsId", "type": "bytes32[]"}
            ],
            "name": "beethovenReserves",
            "outputs": [
                {
                    "components": [
                        {
                            "internalType": "bytes32",
                            "name": "poolid",
                            "type": "bytes32",
                        },
                        {
                            "internalType": "uint256[]",
                            "name": "reserves",
                            "type": "uint256[]",
                        },
                        {
                            "internalType": "contract IERC20[]",
                            "name": "tokens",
                            "type": "address[]",
                        },
                        {
                            "internalType": "uint256",
                            "name": "lastChangeBlock",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct BatchReadV2.BeethovenPoolReserves[]",
                    "name": "",
                    "type": "tuple[]",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "beethoven_contract",
            "outputs": [{"internalType": "contract IB", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "contract IERC20", "name": "token", "type": "address"},
                {"internalType": "address", "name": "sender", "type": "address"},
                {"internalType": "address", "name": "recipient", "type": "address"},
                {"internalType": "uint256", "name": "amount", "type": "uint256"},
            ],
            "name": "burn_rate",
            "outputs": [
                {"internalType": "uint256", "name": "pre_balance", "type": "uint256"},
                {"internalType": "uint256", "name": "post_balance", "type": "uint256"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "_default_router",
                    "type": "address",
                },
                {
                    "internalType": "address",
                    "name": "_default_masterchef",
                    "type": "address",
                },
                {"internalType": "address", "name": "_WFTM", "type": "address"},
            ],
            "name": "change_defaults",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "new_owner", "type": "address"}
            ],
            "name": "change_owner",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "token_address", "type": "address"},
                {
                    "internalType": "address[]",
                    "name": "locked_walltes",
                    "type": "address[]",
                },
            ],
            "name": "circulatingSupply",
            "outputs": [
                {"internalType": "uint256", "name": "result", "type": "uint256"}
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "default_factory",
            "outputs": [
                {
                    "internalType": "contract IUniswapV2Factory",
                    "name": "",
                    "type": "address",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "default_masterchef",
            "outputs": [
                {"internalType": "contract IMasterChef", "name": "", "type": "address"}
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "default_router",
            "outputs": [
                {
                    "internalType": "contract IUniswapV2Router",
                    "name": "",
                    "type": "address",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "skip", "type": "uint256"},
                {"internalType": "uint256", "name": "limit", "type": "uint256"},
            ],
            "name": "getAllFactoryPairsDefaultFactorySkipLimit",
            "outputs": [
                {
                    "components": [
                        {
                            "internalType": "address",
                            "name": "pair_address",
                            "type": "address",
                        },
                        {
                            "internalType": "address",
                            "name": "token0",
                            "type": "address",
                        },
                        {
                            "internalType": "address",
                            "name": "token1",
                            "type": "address",
                        },
                    ],
                    "internalType": "struct BatchReadV2.PairObj[]",
                    "name": "",
                    "type": "tuple[]",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "contract IUniswapV2Factory",
                    "name": "factory",
                    "type": "address",
                },
                {"internalType": "uint256", "name": "skip", "type": "uint256"},
                {"internalType": "uint256", "name": "limit", "type": "uint256"},
            ],
            "name": "getAllFactoryPairsSkipLimit",
            "outputs": [
                {
                    "components": [
                        {
                            "internalType": "address",
                            "name": "pair_address",
                            "type": "address",
                        },
                        {
                            "internalType": "address",
                            "name": "token0",
                            "type": "address",
                        },
                        {
                            "internalType": "address",
                            "name": "token1",
                            "type": "address",
                        },
                    ],
                    "internalType": "struct BatchReadV2.PairObj[]",
                    "name": "",
                    "type": "tuple[]",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "amountOut", "type": "uint256"},
                {"internalType": "address", "name": "tokenA", "type": "address"},
                {"internalType": "address", "name": "tokenB", "type": "address"},
            ],
            "name": "getAmountInAddLiquidity",
            "outputs": [
                {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
                {"internalType": "uint256", "name": "share", "type": "uint256"},
                {"internalType": "uint256", "name": "lpCount", "type": "uint256"},
                {"internalType": "uint256", "name": "totalSupply", "type": "uint256"},
                {"internalType": "address", "name": "pairAddress", "type": "address"},
                {"internalType": "uint256", "name": "rA", "type": "uint256"},
                {"internalType": "uint256", "name": "rB", "type": "uint256"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
                {"internalType": "address", "name": "tokenA", "type": "address"},
                {"internalType": "address", "name": "tokenB", "type": "address"},
            ],
            "name": "getAmountOutAddLiquidity",
            "outputs": [
                {"internalType": "uint256", "name": "amountOut", "type": "uint256"},
                {"internalType": "uint256", "name": "share", "type": "uint256"},
                {"internalType": "uint256", "name": "lpCount", "type": "uint256"},
                {"internalType": "uint256", "name": "totalSupply", "type": "uint256"},
                {"internalType": "address", "name": "pairAddress", "type": "address"},
                {"internalType": "uint256", "name": "rA", "type": "uint256"},
                {"internalType": "uint256", "name": "rB", "type": "uint256"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "amountOut", "type": "uint256"},
                {"internalType": "address[][]", "name": "path", "type": "address[][]"},
            ],
            "name": "getAmountsInMulti",
            "outputs": [
                {"internalType": "uint256", "name": "", "type": "uint256"},
                {"internalType": "address[]", "name": "", "type": "address[]"},
                {"internalType": "int256", "name": "", "type": "int256"},
                {"internalType": "uint256", "name": "", "type": "uint256"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
                {"internalType": "address[][]", "name": "path", "type": "address[][]"},
            ],
            "name": "getAmountsOutMulti",
            "outputs": [
                {"internalType": "uint256", "name": "", "type": "uint256"},
                {"internalType": "address[]", "name": "", "type": "address[]"},
                {"internalType": "int256", "name": "", "type": "int256"},
                {"internalType": "uint256", "name": "", "type": "uint256"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "skip", "type": "uint256"},
                {"internalType": "uint256", "name": "limit", "type": "uint256"},
            ],
            "name": "getFarmInfo",
            "outputs": [
                {
                    "components": [
                        {
                            "internalType": "uint256",
                            "name": "poolid",
                            "type": "uint256",
                        },
                        {
                            "components": [
                                {
                                    "internalType": "address",
                                    "name": "pair_address",
                                    "type": "address",
                                },
                                {
                                    "internalType": "address",
                                    "name": "token0",
                                    "type": "address",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "share0",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "address",
                                    "name": "token1",
                                    "type": "address",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "share1",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "share",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "balance",
                                    "type": "uint256",
                                },
                                {
                                    "internalType": "uint256",
                                    "name": "totalSupply",
                                    "type": "uint256",
                                },
                            ],
                            "internalType": "struct BatchReadV2.ShareOfPool",
                            "name": "lpSharenfo",
                            "type": "tuple",
                        },
                        {
                            "internalType": "uint256",
                            "name": "totalLockedSupply",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "totalSupply",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "allocPoint",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "tcsPerDay",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "lastRewardTime",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct BatchReadV2.FarmInfo[]",
                    "name": "",
                    "type": "tuple[]",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "contract IUniswapV2Pair",
                    "name": "pair",
                    "type": "address",
                },
                {"internalType": "address", "name": "tokenA", "type": "address"},
                {"internalType": "address", "name": "tokenB", "type": "address"},
            ],
            "name": "getReserves",
            "outputs": [
                {"internalType": "uint256", "name": "reserveA", "type": "uint256"},
                {"internalType": "uint256", "name": "reserveB", "type": "uint256"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "wallet_address", "type": "address"}
            ],
            "name": "getShareMulti",
            "outputs": [
                {
                    "components": [
                        {
                            "internalType": "address",
                            "name": "pair_address",
                            "type": "address",
                        },
                        {
                            "internalType": "address",
                            "name": "token0",
                            "type": "address",
                        },
                        {
                            "internalType": "uint256",
                            "name": "share0",
                            "type": "uint256",
                        },
                        {
                            "internalType": "address",
                            "name": "token1",
                            "type": "address",
                        },
                        {
                            "internalType": "uint256",
                            "name": "share1",
                            "type": "uint256",
                        },
                        {"internalType": "uint256", "name": "share", "type": "uint256"},
                        {
                            "internalType": "uint256",
                            "name": "balance",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "totalSupply",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct BatchReadV2.ShareOfPool[]",
                    "name": "",
                    "type": "tuple[]",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "wallet_address",
                    "type": "address",
                },
                {"internalType": "address", "name": "token_address", "type": "address"},
            ],
            "name": "getShareMultiExactToken",
            "outputs": [
                {
                    "components": [
                        {
                            "internalType": "address",
                            "name": "pair_address",
                            "type": "address",
                        },
                        {
                            "internalType": "address",
                            "name": "token0",
                            "type": "address",
                        },
                        {
                            "internalType": "uint256",
                            "name": "share0",
                            "type": "uint256",
                        },
                        {
                            "internalType": "address",
                            "name": "token1",
                            "type": "address",
                        },
                        {
                            "internalType": "uint256",
                            "name": "share1",
                            "type": "uint256",
                        },
                        {"internalType": "uint256", "name": "share", "type": "uint256"},
                        {
                            "internalType": "uint256",
                            "name": "balance",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "totalSupply",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct BatchReadV2.ShareOfPool[]",
                    "name": "",
                    "type": "tuple[]",
                },
                {"internalType": "uint256", "name": "result", "type": "uint256"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "wallet_address",
                    "type": "address",
                },
                {"internalType": "uint256", "name": "skip", "type": "uint256"},
                {"internalType": "uint256", "name": "limit", "type": "uint256"},
            ],
            "name": "getShareMultiSkipLimit",
            "outputs": [
                {
                    "components": [
                        {
                            "internalType": "address",
                            "name": "pair_address",
                            "type": "address",
                        },
                        {
                            "internalType": "address",
                            "name": "token0",
                            "type": "address",
                        },
                        {
                            "internalType": "uint256",
                            "name": "share0",
                            "type": "uint256",
                        },
                        {
                            "internalType": "address",
                            "name": "token1",
                            "type": "address",
                        },
                        {
                            "internalType": "uint256",
                            "name": "share1",
                            "type": "uint256",
                        },
                        {"internalType": "uint256", "name": "share", "type": "uint256"},
                        {
                            "internalType": "uint256",
                            "name": "balance",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "totalSupply",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct BatchReadV2.ShareOfPool[]",
                    "name": "",
                    "type": "tuple[]",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "contract IERC20", "name": "token", "type": "address"},
                {"internalType": "address", "name": "owner", "type": "address"},
                {"internalType": "address", "name": "spender", "type": "address"},
                {"internalType": "uint256", "name": "amount", "type": "uint256"},
                {"internalType": "uint256", "name": "deadline", "type": "uint256"},
                {"internalType": "uint8", "name": "v", "type": "uint8"},
                {"internalType": "bytes32", "name": "r", "type": "bytes32"},
                {"internalType": "bytes32", "name": "s", "type": "bytes32"},
            ],
            "name": "has_permit",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "pair_address", "type": "address"}
            ],
            "name": "maintanerLpCount",
            "outputs": [
                {"internalType": "uint256", "name": "liquidity", "type": "uint256"}
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "pair_address", "type": "address"}
            ],
            "name": "maintanerLpCountInPair",
            "outputs": [
                {"internalType": "uint256", "name": "liquidity", "type": "uint256"}
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "totalSupply", "type": "uint256"},
                {"internalType": "uint256", "name": "amount0", "type": "uint256"},
                {"internalType": "uint256", "name": "amount1", "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "MINIMUM_LIQUIDITY",
                    "type": "uint256",
                },
                {"internalType": "uint256", "name": "_reserve0", "type": "uint256"},
                {"internalType": "uint256", "name": "_reserve1", "type": "uint256"},
            ],
            "name": "mintAmount",
            "outputs": [
                {"internalType": "uint256", "name": "liquidity", "type": "uint256"}
            ],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address[]", "name": "tokens", "type": "address[]"},
                {"internalType": "address", "name": "spender", "type": "address"},
                {
                    "internalType": "address",
                    "name": "wallet_address",
                    "type": "address",
                },
            ],
            "name": "multiGetInfo",
            "outputs": [
                {
                    "components": [
                        {"internalType": "address", "name": "token", "type": "address"},
                        {
                            "internalType": "uint256",
                            "name": "balance",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "allowance",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct BatchReadV2.walletInfo[]",
                    "name": "",
                    "type": "tuple[]",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "wallet_address", "type": "address"}
            ],
            "name": "multiGetLPBalances",
            "outputs": [
                {
                    "components": [
                        {
                            "internalType": "address",
                            "name": "LP_token",
                            "type": "address",
                        },
                        {
                            "internalType": "uint256",
                            "name": "balance",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct BatchReadV2.LP_balance[]",
                    "name": "",
                    "type": "tuple[]",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "wallet_address",
                    "type": "address",
                },
                {"internalType": "uint256", "name": "skip", "type": "uint256"},
                {"internalType": "uint256", "name": "limit", "type": "uint256"},
            ],
            "name": "multiGetLPBalancesSkipLimit",
            "outputs": [
                {
                    "components": [
                        {
                            "internalType": "address",
                            "name": "LP_token",
                            "type": "address",
                        },
                        {
                            "internalType": "uint256",
                            "name": "balance",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct BatchReadV2.LP_balance[]",
                    "name": "",
                    "type": "tuple[]",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address[]", "name": "pairs", "type": "address[]"}
            ],
            "name": "multiGetReserves",
            "outputs": [
                {"internalType": "uint256[]", "name": "", "type": "uint256[]"},
                {"internalType": "uint256[]", "name": "", "type": "uint256[]"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "wallet_address", "type": "address"}
            ],
            "name": "userDetails",
            "outputs": [
                {
                    "components": [
                        {
                            "internalType": "uint256",
                            "name": "poolid",
                            "type": "uint256",
                        },
                        {
                            "internalType": "contract IUniswapV2Pair",
                            "name": "lpToken",
                            "type": "address",
                        },
                        {"internalType": "string", "name": "name", "type": "string"},
                        {
                            "internalType": "contract IERC20",
                            "name": "token0",
                            "type": "address",
                        },
                        {
                            "internalType": "contract IERC20",
                            "name": "token1",
                            "type": "address",
                        },
                        {
                            "internalType": "uint256",
                            "name": "totalSupply",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "totalLockedSupply",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "allocPoint",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "lastRewardTime",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "accTCSPerShare",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "amount",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "rewardDebt",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "balanceLptoken",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "reward",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct BatchReadV2.WalletDetail[]",
                    "name": "",
                    "type": "tuple[]",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
    ]
    # REVIEW SHOULD BE ADDING ALL FUNCTIONS >_<
    # CHECK_PAIR_AND_FACTORY = [{'constant': True, 'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'name': 'allPairs', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'},{'constant': True, 'inputs': [], 'name': 'allPairsLength', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'},{'constant': True, 'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'address', 'name': '', 'type': 'address'}],'name': 'getPair', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}, {"constant": True, "inputs": [], "name":"getReserves", "outputs":[{"internalType": "uint112", "name": "_reserve0", "type": "uint112"}, {"internalType": "uint112", "name": "_reserve1", "type": "uint112"}, {"internalType": "uint32", "name": "_blockTimestampLast", "type": "uint32"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": True, "inputs": [], "name":"token0", "outputs":[{"internalType": "address", "name": "", "type": "address"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": True, "inputs": [], "name":"token1", "outputs":[{"internalType": "address", "name": "", "type": "address"}], "payable": False, "stateMutability": "view", "type": "function"}]
    CHECK_PAIR_AND_FACTORY = [
        {
            "constant": True,
            "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "name": "allPairs",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [],
            "name": "allPairsLength",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [
                {"internalType": "address", "name": "", "type": "address"},
                {"internalType": "address", "name": "", "type": "address"},
            ],
            "name": "getPair",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [],
            "name": "getReserves",
            "outputs": [
                {"internalType": "uint112", "name": "_reserve0", "type": "uint112"},
                {"internalType": "uint112", "name": "_reserve1", "type": "uint112"},
                {
                    "internalType": "uint32",
                    "name": "_blockTimestampLast",
                    "type": "uint32",
                },
            ],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [],
            "name": "token0",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [],
            "name": "token1",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
    ]
    CHECK_IS_AMM_PAIR_ABI = [
        {
            "constant": True,
            "inputs": [],
            "name": "getReserves",
            "outputs": [
                {"internalType": "uint112", "name": "_reserve0", "type": "uint112"},
                {"internalType": "uint112", "name": "_reserve1", "type": "uint112"},
                {
                    "internalType": "uint32",
                    "name": "_blockTimestampLast",
                    "type": "uint32",
                },
            ],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        }
    ]
    CHECK_IS_AMM_FACTORY_ABI = [
        {
            "constant": True,
            "inputs": [],
            "name": "allPairsLength",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        }
    ]
    SOLIDLY_FACTORY = [
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "token0",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "token1",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "bool",
                    "name": "stable",
                    "type": "bool",
                },
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "pair",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256",
                },
            ],
            "name": "PairCreated",
            "type": "event",
        },
        {
            "inputs": [],
            "name": "acceptPauser",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "name": "allPairs",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "allPairsLength",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "tokenA", "type": "address"},
                {"internalType": "address", "name": "tokenB", "type": "address"},
                {"internalType": "bool", "name": "stable", "type": "bool"},
            ],
            "name": "createPair",
            "outputs": [{"internalType": "address", "name": "pair", "type": "address"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getInitializable",
            "outputs": [
                {"internalType": "address", "name": "", "type": "address"},
                {"internalType": "address", "name": "", "type": "address"},
                {"internalType": "bool", "name": "", "type": "bool"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "", "type": "address"},
                {"internalType": "address", "name": "", "type": "address"},
                {"internalType": "bool", "name": "", "type": "bool"},
            ],
            "name": "getPair",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "", "type": "address"}],
            "name": "isPair",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "isPaused",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "pairCodeHash",
            "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "pauser",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "pendingPauser",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "bool", "name": "_state", "type": "bool"}],
            "name": "setPause",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_pauser", "type": "address"}
            ],
            "name": "setPauser",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
    ]
    SOLIDLY_PAIR = [
        {"inputs": [], "stateMutability": "nonpayable", "type": "constructor"},
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "owner",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "spender",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount",
                    "type": "uint256",
                },
            ],
            "name": "Approval",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "sender",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount0",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount1",
                    "type": "uint256",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "to",
                    "type": "address",
                },
            ],
            "name": "Burn",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "sender",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "recipient",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount0",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount1",
                    "type": "uint256",
                },
            ],
            "name": "Claim",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "sender",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount0",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount1",
                    "type": "uint256",
                },
            ],
            "name": "Fees",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "sender",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount0",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount1",
                    "type": "uint256",
                },
            ],
            "name": "Mint",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "sender",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount0In",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount1In",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount0Out",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount1Out",
                    "type": "uint256",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "to",
                    "type": "address",
                },
            ],
            "name": "Swap",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "reserve0",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "reserve1",
                    "type": "uint256",
                },
            ],
            "name": "Sync",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "from",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "to",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount",
                    "type": "uint256",
                },
            ],
            "name": "Transfer",
            "type": "event",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "", "type": "address"},
                {"internalType": "address", "name": "", "type": "address"},
            ],
            "name": "allowance",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "spender", "type": "address"},
                {"internalType": "uint256", "name": "amount", "type": "uint256"},
            ],
            "name": "approve",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "", "type": "address"}],
            "name": "balanceOf",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "blockTimestampLast",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "to", "type": "address"}],
            "name": "burn",
            "outputs": [
                {"internalType": "uint256", "name": "amount0", "type": "uint256"},
                {"internalType": "uint256", "name": "amount1", "type": "uint256"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "claimFees",
            "outputs": [
                {"internalType": "uint256", "name": "claimed0", "type": "uint256"},
                {"internalType": "uint256", "name": "claimed1", "type": "uint256"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "", "type": "address"}],
            "name": "claimable0",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "", "type": "address"}],
            "name": "claimable1",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "tokenIn", "type": "address"},
                {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
            ],
            "name": "current",
            "outputs": [
                {"internalType": "uint256", "name": "amountOut", "type": "uint256"}
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "currentCumulativePrices",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "reserve0Cumulative",
                    "type": "uint256",
                },
                {
                    "internalType": "uint256",
                    "name": "reserve1Cumulative",
                    "type": "uint256",
                },
                {
                    "internalType": "uint256",
                    "name": "blockTimestamp",
                    "type": "uint256",
                },
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "decimals",
            "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "fees",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
                {"internalType": "address", "name": "tokenIn", "type": "address"},
            ],
            "name": "getAmountOut",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getReserves",
            "outputs": [
                {"internalType": "uint256", "name": "_reserve0", "type": "uint256"},
                {"internalType": "uint256", "name": "_reserve1", "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "_blockTimestampLast",
                    "type": "uint256",
                },
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "index0",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "index1",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "lastObservation",
            "outputs": [
                {
                    "components": [
                        {
                            "internalType": "uint256",
                            "name": "timestamp",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "reserve0Cumulative",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "reserve1Cumulative",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct BaseV1Pair.Observation",
                    "name": "",
                    "type": "tuple",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "metadata",
            "outputs": [
                {"internalType": "uint256", "name": "dec0", "type": "uint256"},
                {"internalType": "uint256", "name": "dec1", "type": "uint256"},
                {"internalType": "uint256", "name": "r0", "type": "uint256"},
                {"internalType": "uint256", "name": "r1", "type": "uint256"},
                {"internalType": "bool", "name": "st", "type": "bool"},
                {"internalType": "address", "name": "t0", "type": "address"},
                {"internalType": "address", "name": "t1", "type": "address"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "to", "type": "address"}],
            "name": "mint",
            "outputs": [
                {"internalType": "uint256", "name": "liquidity", "type": "uint256"}
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "name",
            "outputs": [{"internalType": "string", "name": "", "type": "string"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "", "type": "address"}],
            "name": "nonces",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "observationLength",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "name": "observations",
            "outputs": [
                {"internalType": "uint256", "name": "timestamp", "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "reserve0Cumulative",
                    "type": "uint256",
                },
                {
                    "internalType": "uint256",
                    "name": "reserve1Cumulative",
                    "type": "uint256",
                },
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "owner", "type": "address"},
                {"internalType": "address", "name": "spender", "type": "address"},
                {"internalType": "uint256", "name": "value", "type": "uint256"},
                {"internalType": "uint256", "name": "deadline", "type": "uint256"},
                {"internalType": "uint8", "name": "v", "type": "uint8"},
                {"internalType": "bytes32", "name": "r", "type": "bytes32"},
                {"internalType": "bytes32", "name": "s", "type": "bytes32"},
            ],
            "name": "permit",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "tokenIn", "type": "address"},
                {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
                {"internalType": "uint256", "name": "points", "type": "uint256"},
            ],
            "name": "prices",
            "outputs": [{"internalType": "uint256[]", "name": "", "type": "uint256[]"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "tokenIn", "type": "address"},
                {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
                {"internalType": "uint256", "name": "granularity", "type": "uint256"},
            ],
            "name": "quote",
            "outputs": [
                {"internalType": "uint256", "name": "amountOut", "type": "uint256"}
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "reserve0",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "reserve0CumulativeLast",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "reserve1",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "reserve1CumulativeLast",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "tokenIn", "type": "address"},
                {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
                {"internalType": "uint256", "name": "points", "type": "uint256"},
                {"internalType": "uint256", "name": "window", "type": "uint256"},
            ],
            "name": "sample",
            "outputs": [{"internalType": "uint256[]", "name": "", "type": "uint256[]"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "to", "type": "address"}],
            "name": "skim",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "stable",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "", "type": "address"}],
            "name": "supplyIndex0",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "", "type": "address"}],
            "name": "supplyIndex1",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "amount0Out", "type": "uint256"},
                {"internalType": "uint256", "name": "amount1Out", "type": "uint256"},
                {"internalType": "address", "name": "to", "type": "address"},
                {"internalType": "bytes", "name": "data", "type": "bytes"},
            ],
            "name": "swap",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "symbol",
            "outputs": [{"internalType": "string", "name": "", "type": "string"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "sync",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "token0",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "token1",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "tokens",
            "outputs": [
                {"internalType": "address", "name": "", "type": "address"},
                {"internalType": "address", "name": "", "type": "address"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "totalSupply",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "dst", "type": "address"},
                {"internalType": "uint256", "name": "amount", "type": "uint256"},
            ],
            "name": "transfer",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "src", "type": "address"},
                {"internalType": "address", "name": "dst", "type": "address"},
                {"internalType": "uint256", "name": "amount", "type": "uint256"},
            ],
            "name": "transferFrom",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
    ]
    CURVE = [
        {
            "name": "Transfer",
            "inputs": [
                {"type": "address", "name": "sender", "indexed": True},
                {"type": "address", "name": "receiver", "indexed": True},
                {"type": "uint256", "name": "value", "indexed": False},
            ],
            "anonymous": False,
            "type": "event",
        },
        {
            "name": "Approval",
            "inputs": [
                {"type": "address", "name": "owner", "indexed": True},
                {"type": "address", "name": "spender", "indexed": True},
                {"type": "uint256", "name": "value", "indexed": False},
            ],
            "anonymous": False,
            "type": "event",
        },
        {
            "name": "TokenExchange",
            "inputs": [
                {"type": "address", "name": "buyer", "indexed": True},
                {"type": "int128", "name": "sold_id", "indexed": False},
                {"type": "uint256", "name": "tokens_sold", "indexed": False},
                {"type": "int128", "name": "bought_id", "indexed": False},
                {"type": "uint256", "name": "tokens_bought", "indexed": False},
            ],
            "anonymous": False,
            "type": "event",
        },
        {
            "name": "AddLiquidity",
            "inputs": [
                {"type": "address", "name": "provider", "indexed": True},
                {"type": "uint256[2]", "name": "token_amounts", "indexed": False},
                {"type": "uint256[2]", "name": "fees", "indexed": False},
                {"type": "uint256", "name": "invariant", "indexed": False},
                {"type": "uint256", "name": "token_supply", "indexed": False},
            ],
            "anonymous": False,
            "type": "event",
        },
        {
            "name": "RemoveLiquidity",
            "inputs": [
                {"type": "address", "name": "provider", "indexed": True},
                {"type": "uint256[2]", "name": "token_amounts", "indexed": False},
                {"type": "uint256[2]", "name": "fees", "indexed": False},
                {"type": "uint256", "name": "token_supply", "indexed": False},
            ],
            "anonymous": False,
            "type": "event",
        },
        {
            "name": "RemoveLiquidityOne",
            "inputs": [
                {"type": "address", "name": "provider", "indexed": True},
                {"type": "uint256", "name": "token_amount", "indexed": False},
                {"type": "uint256", "name": "coin_amount", "indexed": False},
                {"type": "uint256", "name": "token_supply", "indexed": False},
            ],
            "anonymous": False,
            "type": "event",
        },
        {
            "name": "RemoveLiquidityImbalance",
            "inputs": [
                {"type": "address", "name": "provider", "indexed": True},
                {"type": "uint256[2]", "name": "token_amounts", "indexed": False},
                {"type": "uint256[2]", "name": "fees", "indexed": False},
                {"type": "uint256", "name": "invariant", "indexed": False},
                {"type": "uint256", "name": "token_supply", "indexed": False},
            ],
            "anonymous": False,
            "type": "event",
        },
        {
            "name": "CommitNewAdmin",
            "inputs": [
                {"type": "uint256", "name": "deadline", "indexed": True},
                {"type": "address", "name": "admin", "indexed": True},
            ],
            "anonymous": False,
            "type": "event",
        },
        {
            "name": "NewAdmin",
            "inputs": [{"type": "address", "name": "admin", "indexed": True}],
            "anonymous": False,
            "type": "event",
        },
        {
            "name": "CommitNewFee",
            "inputs": [
                {"type": "uint256", "name": "deadline", "indexed": True},
                {"type": "uint256", "name": "fee", "indexed": False},
                {"type": "uint256", "name": "admin_fee", "indexed": False},
            ],
            "anonymous": False,
            "type": "event",
        },
        {
            "name": "NewFee",
            "inputs": [
                {"type": "uint256", "name": "fee", "indexed": False},
                {"type": "uint256", "name": "admin_fee", "indexed": False},
            ],
            "anonymous": False,
            "type": "event",
        },
        {
            "name": "RampA",
            "inputs": [
                {"type": "uint256", "name": "old_A", "indexed": False},
                {"type": "uint256", "name": "new_A", "indexed": False},
                {"type": "uint256", "name": "initial_time", "indexed": False},
                {"type": "uint256", "name": "future_time", "indexed": False},
            ],
            "anonymous": False,
            "type": "event",
        },
        {
            "name": "StopRampA",
            "inputs": [
                {"type": "uint256", "name": "A", "indexed": False},
                {"type": "uint256", "name": "t", "indexed": False},
            ],
            "anonymous": False,
            "type": "event",
        },
        {
            "outputs": [],
            "inputs": [
                {"type": "string", "name": "_name"},
                {"type": "string", "name": "_symbol"},
                {"type": "address", "name": "_owner"},
                {"type": "address[2]", "name": "_coins"},
                {"type": "uint256", "name": "_A"},
                {"type": "uint256", "name": "_fee"},
                {"type": "uint256", "name": "_admin_fee"},
            ],
            "stateMutability": "nonpayable",
            "type": "constructor",
        },
        {
            "name": "decimals",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 261,
        },
        {
            "name": "transfer",
            "outputs": [{"type": "bool", "name": ""}],
            "inputs": [
                {"type": "address", "name": "_to"},
                {"type": "uint256", "name": "_value"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 74713,
        },
        {
            "name": "transferFrom",
            "outputs": [{"type": "bool", "name": ""}],
            "inputs": [
                {"type": "address", "name": "_from"},
                {"type": "address", "name": "_to"},
                {"type": "uint256", "name": "_value"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 111355,
        },
        {
            "name": "approve",
            "outputs": [{"type": "bool", "name": ""}],
            "inputs": [
                {"type": "address", "name": "_spender"},
                {"type": "uint256", "name": "_value"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 37794,
        },
        {
            "name": "A",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 5439,
        },
        {
            "name": "A_precise",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 5401,
        },
        {
            "name": "get_virtual_price",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 1009729,
        },
        {
            "name": "calc_token_amount",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [
                {"type": "uint256[2]", "name": "_amounts"},
                {"type": "bool", "name": "_is_deposit"},
            ],
            "stateMutability": "view",
            "type": "function",
            "gas": 4016564,
        },
        {
            "name": "add_liquidity",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [
                {"type": "uint256[2]", "name": "_amounts"},
                {"type": "uint256", "name": "_min_mint_amount"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 6262149,
        },
        {
            "name": "get_dy",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [
                {"type": "int128", "name": "i"},
                {"type": "int128", "name": "j"},
                {"type": "uint256", "name": "_dx"},
            ],
            "stateMutability": "view",
            "type": "function",
            "gas": 2447901,
        },
        {
            "name": "exchange",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [
                {"type": "int128", "name": "i"},
                {"type": "int128", "name": "j"},
                {"type": "uint256", "name": "_dx"},
                {"type": "uint256", "name": "_min_dy"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 2610850,
        },
        {
            "name": "remove_liquidity",
            "outputs": [{"type": "uint256[2]", "name": ""}],
            "inputs": [
                {"type": "uint256", "name": "_amount"},
                {"type": "uint256[2]", "name": "_min_amounts"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 238744,
        },
        {
            "name": "remove_liquidity_imbalance",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [
                {"type": "uint256[2]", "name": "_amounts"},
                {"type": "uint256", "name": "_max_burn_amount"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 6261825,
        },
        {
            "name": "calc_withdraw_one_coin",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [
                {"type": "uint256", "name": "_token_amount"},
                {"type": "int128", "name": "i"},
            ],
            "stateMutability": "view",
            "type": "function",
            "gas": 1609,
        },
        {
            "name": "remove_liquidity_one_coin",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [
                {"type": "uint256", "name": "_token_amount"},
                {"type": "int128", "name": "i"},
                {"type": "uint256", "name": "_min_amount"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 3947982,
        },
        {
            "name": "ramp_A",
            "outputs": [],
            "inputs": [
                {"type": "uint256", "name": "_future_A"},
                {"type": "uint256", "name": "_future_time"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 152014,
        },
        {
            "name": "stop_ramp_A",
            "outputs": [],
            "inputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 148775,
        },
        {
            "name": "commit_new_fee",
            "outputs": [],
            "inputs": [
                {"type": "uint256", "name": "_new_fee"},
                {"type": "uint256", "name": "_new_admin_fee"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 110491,
        },
        {
            "name": "apply_new_fee",
            "outputs": [],
            "inputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 97272,
        },
        {
            "name": "revert_new_parameters",
            "outputs": [],
            "inputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 21925,
        },
        {
            "name": "commit_transfer_ownership",
            "outputs": [],
            "inputs": [{"type": "address", "name": "_owner"}],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 74663,
        },
        {
            "name": "apply_transfer_ownership",
            "outputs": [],
            "inputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 60740,
        },
        {
            "name": "revert_transfer_ownership",
            "outputs": [],
            "inputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 22015,
        },
        {
            "name": "admin_balances",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [{"type": "uint256", "name": "i"}],
            "stateMutability": "view",
            "type": "function",
            "gas": 3511,
        },
        {
            "name": "withdraw_admin_fees",
            "outputs": [],
            "inputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 15067,
        },
        {
            "name": "donate_admin_fees",
            "outputs": [],
            "inputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 74995,
        },
        {
            "name": "kill_me",
            "outputs": [],
            "inputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 38028,
        },
        {
            "name": "unkill_me",
            "outputs": [],
            "inputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 22165,
        },
        {
            "name": "coins",
            "outputs": [{"type": "address", "name": ""}],
            "inputs": [{"type": "uint256", "name": "arg0"}],
            "stateMutability": "view",
            "type": "function",
            "gas": 2250,
        },
        {
            "name": "balances",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [{"type": "uint256", "name": "arg0"}],
            "stateMutability": "view",
            "type": "function",
            "gas": 2280,
        },
        {
            "name": "fee",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 2201,
        },
        {
            "name": "admin_fee",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 2231,
        },
        {
            "name": "owner",
            "outputs": [{"type": "address", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 2261,
        },
        {
            "name": "initial_A",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 2291,
        },
        {
            "name": "future_A",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 2321,
        },
        {
            "name": "initial_A_time",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 2351,
        },
        {
            "name": "future_A_time",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 2381,
        },
        {
            "name": "admin_actions_deadline",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 2411,
        },
        {
            "name": "transfer_ownership_deadline",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 2441,
        },
        {
            "name": "future_fee",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 2471,
        },
        {
            "name": "future_admin_fee",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 2501,
        },
        {
            "name": "future_owner",
            "outputs": [{"type": "address", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 2531,
        },
        {
            "name": "name",
            "outputs": [{"type": "string", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 8963,
        },
        {
            "name": "symbol",
            "outputs": [{"type": "string", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 8016,
        },
        {
            "name": "balanceOf",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [{"type": "address", "name": "arg0"}],
            "stateMutability": "view",
            "type": "function",
            "gas": 2836,
        },
        {
            "name": "allowance",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [
                {"type": "address", "name": "arg0"},
                {"type": "address", "name": "arg1"},
            ],
            "stateMutability": "view",
            "type": "function",
            "gas": 3081,
        },
        {
            "name": "totalSupply",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 2681,
        },
    ]
    BEETHOVEN = [
        {
            "inputs": [
                {
                    "internalType": "contract IAuthorizer",
                    "name": "authorizer",
                    "type": "address",
                },
                {"internalType": "contract IWETH", "name": "weth", "type": "address"},
                {
                    "internalType": "uint256",
                    "name": "pauseWindowDuration",
                    "type": "uint256",
                },
                {
                    "internalType": "uint256",
                    "name": "bufferPeriodDuration",
                    "type": "uint256",
                },
            ],
            "stateMutability": "nonpayable",
            "type": "constructor",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "contract IAuthorizer",
                    "name": "newAuthorizer",
                    "type": "address",
                }
            ],
            "name": "AuthorizerChanged",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "contract IERC20",
                    "name": "token",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "sender",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "recipient",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount",
                    "type": "uint256",
                },
            ],
            "name": "ExternalBalanceTransfer",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "contract IFlashLoanRecipient",
                    "name": "recipient",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "contract IERC20",
                    "name": "token",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "feeAmount",
                    "type": "uint256",
                },
            ],
            "name": "FlashLoan",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "user",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "contract IERC20",
                    "name": "token",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "int256",
                    "name": "delta",
                    "type": "int256",
                },
            ],
            "name": "InternalBalanceChanged",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "bool",
                    "name": "paused",
                    "type": "bool",
                }
            ],
            "name": "PausedStateChanged",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "bytes32",
                    "name": "poolId",
                    "type": "bytes32",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "liquidityProvider",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "contract IERC20[]",
                    "name": "tokens",
                    "type": "address[]",
                },
                {
                    "indexed": False,
                    "internalType": "int256[]",
                    "name": "deltas",
                    "type": "int256[]",
                },
                {
                    "indexed": False,
                    "internalType": "uint256[]",
                    "name": "protocolFeeAmounts",
                    "type": "uint256[]",
                },
            ],
            "name": "PoolBalanceChanged",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "bytes32",
                    "name": "poolId",
                    "type": "bytes32",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "assetManager",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "contract IERC20",
                    "name": "token",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "int256",
                    "name": "cashDelta",
                    "type": "int256",
                },
                {
                    "indexed": False,
                    "internalType": "int256",
                    "name": "managedDelta",
                    "type": "int256",
                },
            ],
            "name": "PoolBalanceManaged",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "bytes32",
                    "name": "poolId",
                    "type": "bytes32",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "poolAddress",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "enum IVault.PoolSpecialization",
                    "name": "specialization",
                    "type": "uint8",
                },
            ],
            "name": "PoolRegistered",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "relayer",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "sender",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "bool",
                    "name": "approved",
                    "type": "bool",
                },
            ],
            "name": "RelayerApprovalChanged",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "bytes32",
                    "name": "poolId",
                    "type": "bytes32",
                },
                {
                    "indexed": True,
                    "internalType": "contract IERC20",
                    "name": "tokenIn",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "contract IERC20",
                    "name": "tokenOut",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amountIn",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amountOut",
                    "type": "uint256",
                },
            ],
            "name": "Swap",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "bytes32",
                    "name": "poolId",
                    "type": "bytes32",
                },
                {
                    "indexed": False,
                    "internalType": "contract IERC20[]",
                    "name": "tokens",
                    "type": "address[]",
                },
            ],
            "name": "TokensDeregistered",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "bytes32",
                    "name": "poolId",
                    "type": "bytes32",
                },
                {
                    "indexed": False,
                    "internalType": "contract IERC20[]",
                    "name": "tokens",
                    "type": "address[]",
                },
                {
                    "indexed": False,
                    "internalType": "address[]",
                    "name": "assetManagers",
                    "type": "address[]",
                },
            ],
            "name": "TokensRegistered",
            "type": "event",
        },
        {
            "inputs": [],
            "name": "WETH",
            "outputs": [
                {"internalType": "contract IWETH", "name": "", "type": "address"}
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "enum IVault.SwapKind",
                    "name": "kind",
                    "type": "uint8",
                },
                {
                    "components": [
                        {
                            "internalType": "bytes32",
                            "name": "poolId",
                            "type": "bytes32",
                        },
                        {
                            "internalType": "uint256",
                            "name": "assetInIndex",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "assetOutIndex",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "amount",
                            "type": "uint256",
                        },
                        {"internalType": "bytes", "name": "userData", "type": "bytes"},
                    ],
                    "internalType": "struct IVault.BatchSwapStep[]",
                    "name": "swaps",
                    "type": "tuple[]",
                },
                {
                    "internalType": "contract IAsset[]",
                    "name": "assets",
                    "type": "address[]",
                },
                {
                    "components": [
                        {
                            "internalType": "address",
                            "name": "sender",
                            "type": "address",
                        },
                        {
                            "internalType": "bool",
                            "name": "fromInternalBalance",
                            "type": "bool",
                        },
                        {
                            "internalType": "address payable",
                            "name": "recipient",
                            "type": "address",
                        },
                        {
                            "internalType": "bool",
                            "name": "toInternalBalance",
                            "type": "bool",
                        },
                    ],
                    "internalType": "struct IVault.FundManagement",
                    "name": "funds",
                    "type": "tuple",
                },
                {"internalType": "int256[]", "name": "limits", "type": "int256[]"},
                {"internalType": "uint256", "name": "deadline", "type": "uint256"},
            ],
            "name": "batchSwap",
            "outputs": [
                {"internalType": "int256[]", "name": "assetDeltas", "type": "int256[]"}
            ],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "bytes32", "name": "poolId", "type": "bytes32"},
                {
                    "internalType": "contract IERC20[]",
                    "name": "tokens",
                    "type": "address[]",
                },
            ],
            "name": "deregisterTokens",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "bytes32", "name": "poolId", "type": "bytes32"},
                {"internalType": "address", "name": "sender", "type": "address"},
                {
                    "internalType": "address payable",
                    "name": "recipient",
                    "type": "address",
                },
                {
                    "components": [
                        {
                            "internalType": "contract IAsset[]",
                            "name": "assets",
                            "type": "address[]",
                        },
                        {
                            "internalType": "uint256[]",
                            "name": "minAmountsOut",
                            "type": "uint256[]",
                        },
                        {"internalType": "bytes", "name": "userData", "type": "bytes"},
                        {
                            "internalType": "bool",
                            "name": "toInternalBalance",
                            "type": "bool",
                        },
                    ],
                    "internalType": "struct IVault.ExitPoolRequest",
                    "name": "request",
                    "type": "tuple",
                },
            ],
            "name": "exitPool",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "contract IFlashLoanRecipient",
                    "name": "recipient",
                    "type": "address",
                },
                {
                    "internalType": "contract IERC20[]",
                    "name": "tokens",
                    "type": "address[]",
                },
                {"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"},
                {"internalType": "bytes", "name": "userData", "type": "bytes"},
            ],
            "name": "flashLoan",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "bytes4", "name": "selector", "type": "bytes4"}
            ],
            "name": "getActionId",
            "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getAuthorizer",
            "outputs": [
                {"internalType": "contract IAuthorizer", "name": "", "type": "address"}
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getDomainSeparator",
            "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "user", "type": "address"},
                {
                    "internalType": "contract IERC20[]",
                    "name": "tokens",
                    "type": "address[]",
                },
            ],
            "name": "getInternalBalance",
            "outputs": [
                {"internalType": "uint256[]", "name": "balances", "type": "uint256[]"}
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "user", "type": "address"}],
            "name": "getNextNonce",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getPausedState",
            "outputs": [
                {"internalType": "bool", "name": "paused", "type": "bool"},
                {
                    "internalType": "uint256",
                    "name": "pauseWindowEndTime",
                    "type": "uint256",
                },
                {
                    "internalType": "uint256",
                    "name": "bufferPeriodEndTime",
                    "type": "uint256",
                },
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "bytes32", "name": "poolId", "type": "bytes32"}
            ],
            "name": "getPool",
            "outputs": [
                {"internalType": "address", "name": "", "type": "address"},
                {
                    "internalType": "enum IVault.PoolSpecialization",
                    "name": "",
                    "type": "uint8",
                },
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "bytes32", "name": "poolId", "type": "bytes32"},
                {"internalType": "contract IERC20", "name": "token", "type": "address"},
            ],
            "name": "getPoolTokenInfo",
            "outputs": [
                {"internalType": "uint256", "name": "cash", "type": "uint256"},
                {"internalType": "uint256", "name": "managed", "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "lastChangeBlock",
                    "type": "uint256",
                },
                {"internalType": "address", "name": "assetManager", "type": "address"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "bytes32", "name": "poolId", "type": "bytes32"}
            ],
            "name": "getPoolTokens",
            "outputs": [
                {
                    "internalType": "contract IERC20[]",
                    "name": "tokens",
                    "type": "address[]",
                },
                {"internalType": "uint256[]", "name": "balances", "type": "uint256[]"},
                {
                    "internalType": "uint256",
                    "name": "lastChangeBlock",
                    "type": "uint256",
                },
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getProtocolFeesCollector",
            "outputs": [
                {
                    "internalType": "contract ProtocolFeesCollector",
                    "name": "",
                    "type": "address",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "user", "type": "address"},
                {"internalType": "address", "name": "relayer", "type": "address"},
            ],
            "name": "hasApprovedRelayer",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "bytes32", "name": "poolId", "type": "bytes32"},
                {"internalType": "address", "name": "sender", "type": "address"},
                {"internalType": "address", "name": "recipient", "type": "address"},
                {
                    "components": [
                        {
                            "internalType": "contract IAsset[]",
                            "name": "assets",
                            "type": "address[]",
                        },
                        {
                            "internalType": "uint256[]",
                            "name": "maxAmountsIn",
                            "type": "uint256[]",
                        },
                        {"internalType": "bytes", "name": "userData", "type": "bytes"},
                        {
                            "internalType": "bool",
                            "name": "fromInternalBalance",
                            "type": "bool",
                        },
                    ],
                    "internalType": "struct IVault.JoinPoolRequest",
                    "name": "request",
                    "type": "tuple",
                },
            ],
            "name": "joinPool",
            "outputs": [],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "components": [
                        {
                            "internalType": "enum IVault.PoolBalanceOpKind",
                            "name": "kind",
                            "type": "uint8",
                        },
                        {
                            "internalType": "bytes32",
                            "name": "poolId",
                            "type": "bytes32",
                        },
                        {
                            "internalType": "contract IERC20",
                            "name": "token",
                            "type": "address",
                        },
                        {
                            "internalType": "uint256",
                            "name": "amount",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct IVault.PoolBalanceOp[]",
                    "name": "ops",
                    "type": "tuple[]",
                }
            ],
            "name": "managePoolBalance",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "components": [
                        {
                            "internalType": "enum IVault.UserBalanceOpKind",
                            "name": "kind",
                            "type": "uint8",
                        },
                        {
                            "internalType": "contract IAsset",
                            "name": "asset",
                            "type": "address",
                        },
                        {
                            "internalType": "uint256",
                            "name": "amount",
                            "type": "uint256",
                        },
                        {
                            "internalType": "address",
                            "name": "sender",
                            "type": "address",
                        },
                        {
                            "internalType": "address payable",
                            "name": "recipient",
                            "type": "address",
                        },
                    ],
                    "internalType": "struct IVault.UserBalanceOp[]",
                    "name": "ops",
                    "type": "tuple[]",
                }
            ],
            "name": "manageUserBalance",
            "outputs": [],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "enum IVault.SwapKind",
                    "name": "kind",
                    "type": "uint8",
                },
                {
                    "components": [
                        {
                            "internalType": "bytes32",
                            "name": "poolId",
                            "type": "bytes32",
                        },
                        {
                            "internalType": "uint256",
                            "name": "assetInIndex",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "assetOutIndex",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "amount",
                            "type": "uint256",
                        },
                        {"internalType": "bytes", "name": "userData", "type": "bytes"},
                    ],
                    "internalType": "struct IVault.BatchSwapStep[]",
                    "name": "swaps",
                    "type": "tuple[]",
                },
                {
                    "internalType": "contract IAsset[]",
                    "name": "assets",
                    "type": "address[]",
                },
                {
                    "components": [
                        {
                            "internalType": "address",
                            "name": "sender",
                            "type": "address",
                        },
                        {
                            "internalType": "bool",
                            "name": "fromInternalBalance",
                            "type": "bool",
                        },
                        {
                            "internalType": "address payable",
                            "name": "recipient",
                            "type": "address",
                        },
                        {
                            "internalType": "bool",
                            "name": "toInternalBalance",
                            "type": "bool",
                        },
                    ],
                    "internalType": "struct IVault.FundManagement",
                    "name": "funds",
                    "type": "tuple",
                },
            ],
            "name": "queryBatchSwap",
            "outputs": [{"internalType": "int256[]", "name": "", "type": "int256[]"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "enum IVault.PoolSpecialization",
                    "name": "specialization",
                    "type": "uint8",
                }
            ],
            "name": "registerPool",
            "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "bytes32", "name": "poolId", "type": "bytes32"},
                {
                    "internalType": "contract IERC20[]",
                    "name": "tokens",
                    "type": "address[]",
                },
                {
                    "internalType": "address[]",
                    "name": "assetManagers",
                    "type": "address[]",
                },
            ],
            "name": "registerTokens",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "contract IAuthorizer",
                    "name": "newAuthorizer",
                    "type": "address",
                }
            ],
            "name": "setAuthorizer",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "bool", "name": "paused", "type": "bool"}],
            "name": "setPaused",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "sender", "type": "address"},
                {"internalType": "address", "name": "relayer", "type": "address"},
                {"internalType": "bool", "name": "approved", "type": "bool"},
            ],
            "name": "setRelayerApproval",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "components": [
                        {
                            "internalType": "bytes32",
                            "name": "poolId",
                            "type": "bytes32",
                        },
                        {
                            "internalType": "enum IVault.SwapKind",
                            "name": "kind",
                            "type": "uint8",
                        },
                        {
                            "internalType": "contract IAsset",
                            "name": "assetIn",
                            "type": "address",
                        },
                        {
                            "internalType": "contract IAsset",
                            "name": "assetOut",
                            "type": "address",
                        },
                        {
                            "internalType": "uint256",
                            "name": "amount",
                            "type": "uint256",
                        },
                        {"internalType": "bytes", "name": "userData", "type": "bytes"},
                    ],
                    "internalType": "struct IVault.SingleSwap",
                    "name": "singleSwap",
                    "type": "tuple",
                },
                {
                    "components": [
                        {
                            "internalType": "address",
                            "name": "sender",
                            "type": "address",
                        },
                        {
                            "internalType": "bool",
                            "name": "fromInternalBalance",
                            "type": "bool",
                        },
                        {
                            "internalType": "address payable",
                            "name": "recipient",
                            "type": "address",
                        },
                        {
                            "internalType": "bool",
                            "name": "toInternalBalance",
                            "type": "bool",
                        },
                    ],
                    "internalType": "struct IVault.FundManagement",
                    "name": "funds",
                    "type": "tuple",
                },
                {"internalType": "uint256", "name": "limit", "type": "uint256"},
                {"internalType": "uint256", "name": "deadline", "type": "uint256"},
            ],
            "name": "swap",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "amountCalculated",
                    "type": "uint256",
                }
            ],
            "stateMutability": "payable",
            "type": "function",
        },
        {"stateMutability": "payable", "type": "receive"},
    ]
    BEETHOVEN_VAULT = [
        {
            "inputs": [
                {
                    "internalType": "contract IAuthorizer",
                    "name": "authorizer",
                    "type": "address",
                },
                {"internalType": "contract IWETH", "name": "weth", "type": "address"},
                {
                    "internalType": "uint256",
                    "name": "pauseWindowDuration",
                    "type": "uint256",
                },
                {
                    "internalType": "uint256",
                    "name": "bufferPeriodDuration",
                    "type": "uint256",
                },
            ],
            "stateMutability": "nonpayable",
            "type": "constructor",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "contract IAuthorizer",
                    "name": "newAuthorizer",
                    "type": "address",
                }
            ],
            "name": "AuthorizerChanged",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "contract IERC20",
                    "name": "token",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "sender",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "recipient",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount",
                    "type": "uint256",
                },
            ],
            "name": "ExternalBalanceTransfer",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "contract IFlashLoanRecipient",
                    "name": "recipient",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "contract IERC20",
                    "name": "token",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "feeAmount",
                    "type": "uint256",
                },
            ],
            "name": "FlashLoan",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "user",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "contract IERC20",
                    "name": "token",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "int256",
                    "name": "delta",
                    "type": "int256",
                },
            ],
            "name": "InternalBalanceChanged",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "bool",
                    "name": "paused",
                    "type": "bool",
                }
            ],
            "name": "PausedStateChanged",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "bytes32",
                    "name": "poolId",
                    "type": "bytes32",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "liquidityProvider",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "contract IERC20[]",
                    "name": "tokens",
                    "type": "address[]",
                },
                {
                    "indexed": False,
                    "internalType": "int256[]",
                    "name": "deltas",
                    "type": "int256[]",
                },
                {
                    "indexed": False,
                    "internalType": "uint256[]",
                    "name": "protocolFeeAmounts",
                    "type": "uint256[]",
                },
            ],
            "name": "PoolBalanceChanged",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "bytes32",
                    "name": "poolId",
                    "type": "bytes32",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "assetManager",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "contract IERC20",
                    "name": "token",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "int256",
                    "name": "cashDelta",
                    "type": "int256",
                },
                {
                    "indexed": False,
                    "internalType": "int256",
                    "name": "managedDelta",
                    "type": "int256",
                },
            ],
            "name": "PoolBalanceManaged",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "bytes32",
                    "name": "poolId",
                    "type": "bytes32",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "poolAddress",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "enum IVault.PoolSpecialization",
                    "name": "specialization",
                    "type": "uint8",
                },
            ],
            "name": "PoolRegistered",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "relayer",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "sender",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "bool",
                    "name": "approved",
                    "type": "bool",
                },
            ],
            "name": "RelayerApprovalChanged",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "bytes32",
                    "name": "poolId",
                    "type": "bytes32",
                },
                {
                    "indexed": True,
                    "internalType": "contract IERC20",
                    "name": "tokenIn",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "contract IERC20",
                    "name": "tokenOut",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amountIn",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amountOut",
                    "type": "uint256",
                },
            ],
            "name": "Swap",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "bytes32",
                    "name": "poolId",
                    "type": "bytes32",
                },
                {
                    "indexed": False,
                    "internalType": "contract IERC20[]",
                    "name": "tokens",
                    "type": "address[]",
                },
            ],
            "name": "TokensDeregistered",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "bytes32",
                    "name": "poolId",
                    "type": "bytes32",
                },
                {
                    "indexed": False,
                    "internalType": "contract IERC20[]",
                    "name": "tokens",
                    "type": "address[]",
                },
                {
                    "indexed": False,
                    "internalType": "address[]",
                    "name": "assetManagers",
                    "type": "address[]",
                },
            ],
            "name": "TokensRegistered",
            "type": "event",
        },
        {
            "inputs": [],
            "name": "WETH",
            "outputs": [
                {"internalType": "contract IWETH", "name": "", "type": "address"}
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "enum IVault.SwapKind",
                    "name": "kind",
                    "type": "uint8",
                },
                {
                    "components": [
                        {
                            "internalType": "bytes32",
                            "name": "poolId",
                            "type": "bytes32",
                        },
                        {
                            "internalType": "uint256",
                            "name": "assetInIndex",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "assetOutIndex",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "amount",
                            "type": "uint256",
                        },
                        {"internalType": "bytes", "name": "userData", "type": "bytes"},
                    ],
                    "internalType": "struct IVault.BatchSwapStep[]",
                    "name": "swaps",
                    "type": "tuple[]",
                },
                {
                    "internalType": "contract IAsset[]",
                    "name": "assets",
                    "type": "address[]",
                },
                {
                    "components": [
                        {
                            "internalType": "address",
                            "name": "sender",
                            "type": "address",
                        },
                        {
                            "internalType": "bool",
                            "name": "fromInternalBalance",
                            "type": "bool",
                        },
                        {
                            "internalType": "address payable",
                            "name": "recipient",
                            "type": "address",
                        },
                        {
                            "internalType": "bool",
                            "name": "toInternalBalance",
                            "type": "bool",
                        },
                    ],
                    "internalType": "struct IVault.FundManagement",
                    "name": "funds",
                    "type": "tuple",
                },
                {"internalType": "int256[]", "name": "limits", "type": "int256[]"},
                {"internalType": "uint256", "name": "deadline", "type": "uint256"},
            ],
            "name": "batchSwap",
            "outputs": [
                {"internalType": "int256[]", "name": "assetDeltas", "type": "int256[]"}
            ],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "bytes32", "name": "poolId", "type": "bytes32"},
                {
                    "internalType": "contract IERC20[]",
                    "name": "tokens",
                    "type": "address[]",
                },
            ],
            "name": "deregisterTokens",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "bytes32", "name": "poolId", "type": "bytes32"},
                {"internalType": "address", "name": "sender", "type": "address"},
                {
                    "internalType": "address payable",
                    "name": "recipient",
                    "type": "address",
                },
                {
                    "components": [
                        {
                            "internalType": "contract IAsset[]",
                            "name": "assets",
                            "type": "address[]",
                        },
                        {
                            "internalType": "uint256[]",
                            "name": "minAmountsOut",
                            "type": "uint256[]",
                        },
                        {"internalType": "bytes", "name": "userData", "type": "bytes"},
                        {
                            "internalType": "bool",
                            "name": "toInternalBalance",
                            "type": "bool",
                        },
                    ],
                    "internalType": "struct IVault.ExitPoolRequest",
                    "name": "request",
                    "type": "tuple",
                },
            ],
            "name": "exitPool",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "contract IFlashLoanRecipient",
                    "name": "recipient",
                    "type": "address",
                },
                {
                    "internalType": "contract IERC20[]",
                    "name": "tokens",
                    "type": "address[]",
                },
                {"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"},
                {"internalType": "bytes", "name": "userData", "type": "bytes"},
            ],
            "name": "flashLoan",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "bytes4", "name": "selector", "type": "bytes4"}
            ],
            "name": "getActionId",
            "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getAuthorizer",
            "outputs": [
                {"internalType": "contract IAuthorizer", "name": "", "type": "address"}
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getDomainSeparator",
            "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "user", "type": "address"},
                {
                    "internalType": "contract IERC20[]",
                    "name": "tokens",
                    "type": "address[]",
                },
            ],
            "name": "getInternalBalance",
            "outputs": [
                {"internalType": "uint256[]", "name": "balances", "type": "uint256[]"}
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "address", "name": "user", "type": "address"}],
            "name": "getNextNonce",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getPausedState",
            "outputs": [
                {"internalType": "bool", "name": "paused", "type": "bool"},
                {
                    "internalType": "uint256",
                    "name": "pauseWindowEndTime",
                    "type": "uint256",
                },
                {
                    "internalType": "uint256",
                    "name": "bufferPeriodEndTime",
                    "type": "uint256",
                },
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "bytes32", "name": "poolId", "type": "bytes32"}
            ],
            "name": "getPool",
            "outputs": [
                {"internalType": "address", "name": "", "type": "address"},
                {
                    "internalType": "enum IVault.PoolSpecialization",
                    "name": "",
                    "type": "uint8",
                },
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "bytes32", "name": "poolId", "type": "bytes32"},
                {"internalType": "contract IERC20", "name": "token", "type": "address"},
            ],
            "name": "getPoolTokenInfo",
            "outputs": [
                {"internalType": "uint256", "name": "cash", "type": "uint256"},
                {"internalType": "uint256", "name": "managed", "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "lastChangeBlock",
                    "type": "uint256",
                },
                {"internalType": "address", "name": "assetManager", "type": "address"},
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "bytes32", "name": "poolId", "type": "bytes32"}
            ],
            "name": "getPoolTokens",
            "outputs": [
                {
                    "internalType": "contract IERC20[]",
                    "name": "tokens",
                    "type": "address[]",
                },
                {"internalType": "uint256[]", "name": "balances", "type": "uint256[]"},
                {
                    "internalType": "uint256",
                    "name": "lastChangeBlock",
                    "type": "uint256",
                },
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getProtocolFeesCollector",
            "outputs": [
                {
                    "internalType": "contract ProtocolFeesCollector",
                    "name": "",
                    "type": "address",
                }
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "user", "type": "address"},
                {"internalType": "address", "name": "relayer", "type": "address"},
            ],
            "name": "hasApprovedRelayer",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "bytes32", "name": "poolId", "type": "bytes32"},
                {"internalType": "address", "name": "sender", "type": "address"},
                {"internalType": "address", "name": "recipient", "type": "address"},
                {
                    "components": [
                        {
                            "internalType": "contract IAsset[]",
                            "name": "assets",
                            "type": "address[]",
                        },
                        {
                            "internalType": "uint256[]",
                            "name": "maxAmountsIn",
                            "type": "uint256[]",
                        },
                        {"internalType": "bytes", "name": "userData", "type": "bytes"},
                        {
                            "internalType": "bool",
                            "name": "fromInternalBalance",
                            "type": "bool",
                        },
                    ],
                    "internalType": "struct IVault.JoinPoolRequest",
                    "name": "request",
                    "type": "tuple",
                },
            ],
            "name": "joinPool",
            "outputs": [],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "components": [
                        {
                            "internalType": "enum IVault.PoolBalanceOpKind",
                            "name": "kind",
                            "type": "uint8",
                        },
                        {
                            "internalType": "bytes32",
                            "name": "poolId",
                            "type": "bytes32",
                        },
                        {
                            "internalType": "contract IERC20",
                            "name": "token",
                            "type": "address",
                        },
                        {
                            "internalType": "uint256",
                            "name": "amount",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct IVault.PoolBalanceOp[]",
                    "name": "ops",
                    "type": "tuple[]",
                }
            ],
            "name": "managePoolBalance",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "components": [
                        {
                            "internalType": "enum IVault.UserBalanceOpKind",
                            "name": "kind",
                            "type": "uint8",
                        },
                        {
                            "internalType": "contract IAsset",
                            "name": "asset",
                            "type": "address",
                        },
                        {
                            "internalType": "uint256",
                            "name": "amount",
                            "type": "uint256",
                        },
                        {
                            "internalType": "address",
                            "name": "sender",
                            "type": "address",
                        },
                        {
                            "internalType": "address payable",
                            "name": "recipient",
                            "type": "address",
                        },
                    ],
                    "internalType": "struct IVault.UserBalanceOp[]",
                    "name": "ops",
                    "type": "tuple[]",
                }
            ],
            "name": "manageUserBalance",
            "outputs": [],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "enum IVault.SwapKind",
                    "name": "kind",
                    "type": "uint8",
                },
                {
                    "components": [
                        {
                            "internalType": "bytes32",
                            "name": "poolId",
                            "type": "bytes32",
                        },
                        {
                            "internalType": "uint256",
                            "name": "assetInIndex",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "assetOutIndex",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "amount",
                            "type": "uint256",
                        },
                        {"internalType": "bytes", "name": "userData", "type": "bytes"},
                    ],
                    "internalType": "struct IVault.BatchSwapStep[]",
                    "name": "swaps",
                    "type": "tuple[]",
                },
                {
                    "internalType": "contract IAsset[]",
                    "name": "assets",
                    "type": "address[]",
                },
                {
                    "components": [
                        {
                            "internalType": "address",
                            "name": "sender",
                            "type": "address",
                        },
                        {
                            "internalType": "bool",
                            "name": "fromInternalBalance",
                            "type": "bool",
                        },
                        {
                            "internalType": "address payable",
                            "name": "recipient",
                            "type": "address",
                        },
                        {
                            "internalType": "bool",
                            "name": "toInternalBalance",
                            "type": "bool",
                        },
                    ],
                    "internalType": "struct IVault.FundManagement",
                    "name": "funds",
                    "type": "tuple",
                },
            ],
            "name": "queryBatchSwap",
            "outputs": [{"internalType": "int256[]", "name": "", "type": "int256[]"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "enum IVault.PoolSpecialization",
                    "name": "specialization",
                    "type": "uint8",
                }
            ],
            "name": "registerPool",
            "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "bytes32", "name": "poolId", "type": "bytes32"},
                {
                    "internalType": "contract IERC20[]",
                    "name": "tokens",
                    "type": "address[]",
                },
                {
                    "internalType": "address[]",
                    "name": "assetManagers",
                    "type": "address[]",
                },
            ],
            "name": "registerTokens",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "contract IAuthorizer",
                    "name": "newAuthorizer",
                    "type": "address",
                }
            ],
            "name": "setAuthorizer",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "bool", "name": "paused", "type": "bool"}],
            "name": "setPaused",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "sender", "type": "address"},
                {"internalType": "address", "name": "relayer", "type": "address"},
                {"internalType": "bool", "name": "approved", "type": "bool"},
            ],
            "name": "setRelayerApproval",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "components": [
                        {
                            "internalType": "bytes32",
                            "name": "poolId",
                            "type": "bytes32",
                        },
                        {
                            "internalType": "enum IVault.SwapKind",
                            "name": "kind",
                            "type": "uint8",
                        },
                        {
                            "internalType": "contract IAsset",
                            "name": "assetIn",
                            "type": "address",
                        },
                        {
                            "internalType": "contract IAsset",
                            "name": "assetOut",
                            "type": "address",
                        },
                        {
                            "internalType": "uint256",
                            "name": "amount",
                            "type": "uint256",
                        },
                        {"internalType": "bytes", "name": "userData", "type": "bytes"},
                    ],
                    "internalType": "struct IVault.SingleSwap",
                    "name": "singleSwap",
                    "type": "tuple",
                },
                {
                    "components": [
                        {
                            "internalType": "address",
                            "name": "sender",
                            "type": "address",
                        },
                        {
                            "internalType": "bool",
                            "name": "fromInternalBalance",
                            "type": "bool",
                        },
                        {
                            "internalType": "address payable",
                            "name": "recipient",
                            "type": "address",
                        },
                        {
                            "internalType": "bool",
                            "name": "toInternalBalance",
                            "type": "bool",
                        },
                    ],
                    "internalType": "struct IVault.FundManagement",
                    "name": "funds",
                    "type": "tuple",
                },
                {"internalType": "uint256", "name": "limit", "type": "uint256"},
                {"internalType": "uint256", "name": "deadline", "type": "uint256"},
            ],
            "name": "swap",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "amountCalculated",
                    "type": "uint256",
                }
            ],
            "stateMutability": "payable",
            "type": "function",
        },
        {"stateMutability": "payable", "type": "receive"},
    ]
    BATCH_EVERYTING = [
        {
            "inputs": [
                {"internalType": "address[]", "name": "addresses", "type": "address[]"},
                {"internalType": "bytes[]", "name": "data", "type": "bytes[]"},
            ],
            "name": "callContracts",
            "outputs": [{"internalType": "bytes[]", "name": "", "type": "bytes[]"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "components": [
                        {"internalType": "address", "name": "add", "type": "address"},
                        {"internalType": "bytes", "name": "data", "type": "bytes"},
                    ],
                    "internalType": "struct SimpleContract.Entry[]",
                    "name": "entries",
                    "type": "tuple[]",
                }
            ],
            "name": "callContractsWithStruct",
            "outputs": [{"internalType": "bytes[]", "name": "", "type": "bytes[]"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "contractAddress",
                    "type": "address",
                },
                {"internalType": "bytes", "name": "data", "type": "bytes"},
            ],
            "name": "safeCall",
            "outputs": [{"internalType": "bytes", "name": "", "type": "bytes"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
    ]
    CURVE = [
        {
            "name": "Transfer",
            "inputs": [
                {"type": "address", "name": "sender", "indexed": True},
                {"type": "address", "name": "receiver", "indexed": True},
                {"type": "uint256", "name": "value", "indexed": False},
            ],
            "anonymous": False,
            "type": "event",
        },
        {
            "name": "Approval",
            "inputs": [
                {"type": "address", "name": "owner", "indexed": True},
                {"type": "address", "name": "spender", "indexed": True},
                {"type": "uint256", "name": "value", "indexed": False},
            ],
            "anonymous": False,
            "type": "event",
        },
        {
            "name": "TokenExchange",
            "inputs": [
                {"type": "address", "name": "buyer", "indexed": True},
                {"type": "int128", "name": "sold_id", "indexed": False},
                {"type": "uint256", "name": "tokens_sold", "indexed": False},
                {"type": "int128", "name": "bought_id", "indexed": False},
                {"type": "uint256", "name": "tokens_bought", "indexed": False},
            ],
            "anonymous": False,
            "type": "event",
        },
        {
            "name": "AddLiquidity",
            "inputs": [
                {"type": "address", "name": "provider", "indexed": True},
                {"type": "uint256[2]", "name": "token_amounts", "indexed": False},
                {"type": "uint256[2]", "name": "fees", "indexed": False},
                {"type": "uint256", "name": "invariant", "indexed": False},
                {"type": "uint256", "name": "token_supply", "indexed": False},
            ],
            "anonymous": False,
            "type": "event",
        },
        {
            "name": "RemoveLiquidity",
            "inputs": [
                {"type": "address", "name": "provider", "indexed": True},
                {"type": "uint256[2]", "name": "token_amounts", "indexed": False},
                {"type": "uint256[2]", "name": "fees", "indexed": False},
                {"type": "uint256", "name": "token_supply", "indexed": False},
            ],
            "anonymous": False,
            "type": "event",
        },
        {
            "name": "RemoveLiquidityOne",
            "inputs": [
                {"type": "address", "name": "provider", "indexed": True},
                {"type": "uint256", "name": "token_amount", "indexed": False},
                {"type": "uint256", "name": "coin_amount", "indexed": False},
                {"type": "uint256", "name": "token_supply", "indexed": False},
            ],
            "anonymous": False,
            "type": "event",
        },
        {
            "name": "RemoveLiquidityImbalance",
            "inputs": [
                {"type": "address", "name": "provider", "indexed": True},
                {"type": "uint256[2]", "name": "token_amounts", "indexed": False},
                {"type": "uint256[2]", "name": "fees", "indexed": False},
                {"type": "uint256", "name": "invariant", "indexed": False},
                {"type": "uint256", "name": "token_supply", "indexed": False},
            ],
            "anonymous": False,
            "type": "event",
        },
        {
            "name": "CommitNewAdmin",
            "inputs": [
                {"type": "uint256", "name": "deadline", "indexed": True},
                {"type": "address", "name": "admin", "indexed": True},
            ],
            "anonymous": False,
            "type": "event",
        },
        {
            "name": "NewAdmin",
            "inputs": [{"type": "address", "name": "admin", "indexed": True}],
            "anonymous": False,
            "type": "event",
        },
        {
            "name": "CommitNewFee",
            "inputs": [
                {"type": "uint256", "name": "deadline", "indexed": True},
                {"type": "uint256", "name": "fee", "indexed": False},
                {"type": "uint256", "name": "admin_fee", "indexed": False},
            ],
            "anonymous": False,
            "type": "event",
        },
        {
            "name": "NewFee",
            "inputs": [
                {"type": "uint256", "name": "fee", "indexed": False},
                {"type": "uint256", "name": "admin_fee", "indexed": False},
            ],
            "anonymous": False,
            "type": "event",
        },
        {
            "name": "RampA",
            "inputs": [
                {"type": "uint256", "name": "old_A", "indexed": False},
                {"type": "uint256", "name": "new_A", "indexed": False},
                {"type": "uint256", "name": "initial_time", "indexed": False},
                {"type": "uint256", "name": "future_time", "indexed": False},
            ],
            "anonymous": False,
            "type": "event",
        },
        {
            "name": "StopRampA",
            "inputs": [
                {"type": "uint256", "name": "A", "indexed": False},
                {"type": "uint256", "name": "t", "indexed": False},
            ],
            "anonymous": False,
            "type": "event",
        },
        {
            "outputs": [],
            "inputs": [
                {"type": "string", "name": "_name"},
                {"type": "string", "name": "_symbol"},
                {"type": "address", "name": "_owner"},
                {"type": "address[2]", "name": "_coins"},
                {"type": "uint256", "name": "_A"},
                {"type": "uint256", "name": "_fee"},
                {"type": "uint256", "name": "_admin_fee"},
            ],
            "stateMutability": "nonpayable",
            "type": "constructor",
        },
        {
            "name": "decimals",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 261,
        },
        {
            "name": "transfer",
            "outputs": [{"type": "bool", "name": ""}],
            "inputs": [
                {"type": "address", "name": "_to"},
                {"type": "uint256", "name": "_value"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 74713,
        },
        {
            "name": "transferFrom",
            "outputs": [{"type": "bool", "name": ""}],
            "inputs": [
                {"type": "address", "name": "_from"},
                {"type": "address", "name": "_to"},
                {"type": "uint256", "name": "_value"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 111355,
        },
        {
            "name": "approve",
            "outputs": [{"type": "bool", "name": ""}],
            "inputs": [
                {"type": "address", "name": "_spender"},
                {"type": "uint256", "name": "_value"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 37794,
        },
        {
            "name": "A",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 5439,
        },
        {
            "name": "A_precise",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 5401,
        },
        {
            "name": "get_virtual_price",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 1009729,
        },
        {
            "name": "calc_token_amount",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [
                {"type": "uint256[2]", "name": "_amounts"},
                {"type": "bool", "name": "_is_deposit"},
            ],
            "stateMutability": "view",
            "type": "function",
            "gas": 4016564,
        },
        {
            "name": "add_liquidity",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [
                {"type": "uint256[2]", "name": "_amounts"},
                {"type": "uint256", "name": "_min_mint_amount"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 6262149,
        },
        {
            "name": "get_dy",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [
                {"type": "int128", "name": "i"},
                {"type": "int128", "name": "j"},
                {"type": "uint256", "name": "_dx"},
            ],
            "stateMutability": "view",
            "type": "function",
            "gas": 2447901,
        },
        {
            "name": "exchange",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [
                {"type": "int128", "name": "i"},
                {"type": "int128", "name": "j"},
                {"type": "uint256", "name": "_dx"},
                {"type": "uint256", "name": "_min_dy"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 2610850,
        },
        {
            "name": "remove_liquidity",
            "outputs": [{"type": "uint256[2]", "name": ""}],
            "inputs": [
                {"type": "uint256", "name": "_amount"},
                {"type": "uint256[2]", "name": "_min_amounts"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 238744,
        },
        {
            "name": "remove_liquidity_imbalance",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [
                {"type": "uint256[2]", "name": "_amounts"},
                {"type": "uint256", "name": "_max_burn_amount"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 6261825,
        },
        {
            "name": "calc_withdraw_one_coin",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [
                {"type": "uint256", "name": "_token_amount"},
                {"type": "int128", "name": "i"},
            ],
            "stateMutability": "view",
            "type": "function",
            "gas": 1609,
        },
        {
            "name": "remove_liquidity_one_coin",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [
                {"type": "uint256", "name": "_token_amount"},
                {"type": "int128", "name": "i"},
                {"type": "uint256", "name": "_min_amount"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 3947982,
        },
        {
            "name": "ramp_A",
            "outputs": [],
            "inputs": [
                {"type": "uint256", "name": "_future_A"},
                {"type": "uint256", "name": "_future_time"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 152014,
        },
        {
            "name": "stop_ramp_A",
            "outputs": [],
            "inputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 148775,
        },
        {
            "name": "commit_new_fee",
            "outputs": [],
            "inputs": [
                {"type": "uint256", "name": "_new_fee"},
                {"type": "uint256", "name": "_new_admin_fee"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 110491,
        },
        {
            "name": "apply_new_fee",
            "outputs": [],
            "inputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 97272,
        },
        {
            "name": "revert_new_parameters",
            "outputs": [],
            "inputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 21925,
        },
        {
            "name": "commit_transfer_ownership",
            "outputs": [],
            "inputs": [{"type": "address", "name": "_owner"}],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 74663,
        },
        {
            "name": "apply_transfer_ownership",
            "outputs": [],
            "inputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 60740,
        },
        {
            "name": "revert_transfer_ownership",
            "outputs": [],
            "inputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 22015,
        },
        {
            "name": "admin_balances",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [{"type": "uint256", "name": "i"}],
            "stateMutability": "view",
            "type": "function",
            "gas": 3511,
        },
        {
            "name": "withdraw_admin_fees",
            "outputs": [],
            "inputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 15067,
        },
        {
            "name": "donate_admin_fees",
            "outputs": [],
            "inputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 74995,
        },
        {
            "name": "kill_me",
            "outputs": [],
            "inputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 38028,
        },
        {
            "name": "unkill_me",
            "outputs": [],
            "inputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
            "gas": 22165,
        },
        {
            "name": "coins",
            "outputs": [{"type": "address", "name": ""}],
            "inputs": [{"type": "uint256", "name": "arg0"}],
            "stateMutability": "view",
            "type": "function",
            "gas": 2250,
        },
        {
            "name": "balances",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [{"type": "uint256", "name": "arg0"}],
            "stateMutability": "view",
            "type": "function",
            "gas": 2280,
        },
        {
            "name": "fee",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 2201,
        },
        {
            "name": "admin_fee",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 2231,
        },
        {
            "name": "owner",
            "outputs": [{"type": "address", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 2261,
        },
        {
            "name": "initial_A",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 2291,
        },
        {
            "name": "future_A",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 2321,
        },
        {
            "name": "initial_A_time",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 2351,
        },
        {
            "name": "future_A_time",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 2381,
        },
        {
            "name": "admin_actions_deadline",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 2411,
        },
        {
            "name": "transfer_ownership_deadline",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 2441,
        },
        {
            "name": "future_fee",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 2471,
        },
        {
            "name": "future_admin_fee",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 2501,
        },
        {
            "name": "future_owner",
            "outputs": [{"type": "address", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 2531,
        },
        {
            "name": "name",
            "outputs": [{"type": "string", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 8963,
        },
        {
            "name": "symbol",
            "outputs": [{"type": "string", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 8016,
        },
        {
            "name": "balanceOf",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [{"type": "address", "name": "arg0"}],
            "stateMutability": "view",
            "type": "function",
            "gas": 2836,
        },
        {
            "name": "allowance",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [
                {"type": "address", "name": "arg0"},
                {"type": "address", "name": "arg1"},
            ],
            "stateMutability": "view",
            "type": "function",
            "gas": 3081,
        },
        {
            "name": "totalSupply",
            "outputs": [{"type": "uint256", "name": ""}],
            "inputs": [],
            "stateMutability": "view",
            "type": "function",
            "gas": 2681,
        },
    ]
    DODO_V2_PAIR = [
        {
            "inputs": [],
            "name": "getPMMStateForCall",
            "outputs": [
                {"internalType": "uint256", "name": "i", "type": "uint256"},
                {"internalType": "uint256", "name": "K", "type": "uint256"},
                {"internalType": "uint256", "name": "B", "type": "uint256"},
                {"internalType": "uint256", "name": "Q", "type": "uint256"},
                {"internalType": "uint256", "name": "B0", "type": "uint256"},
                {"internalType": "uint256", "name": "Q0", "type": "uint256"},
                {"internalType": "uint256", "name": "R", "type": "uint256"},
            ],
            "stateMutability": "view",
            "type": "function",
        }
    ]
    ROUTER = [
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "uint16",
                    "name": "OldAmount",
                    "type": "uint16",
                },
                {
                    "indexed": False,
                    "internalType": "uint16",
                    "name": "NewAmount",
                    "type": "uint16",
                },
            ],
            "name": "FeeAmountChange",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "previousOwner",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "newOwner",
                    "type": "address",
                },
            ],
            "name": "OwnershipTransferred",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "userAddress",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "fromToken",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "toToken",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amountIn",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amountOut",
                    "type": "uint256",
                },
            ],
            "name": "Swapped",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "bytes32",
                    "name": "",
                    "type": "bytes32",
                }
            ],
            "name": "print",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "",
                    "type": "address",
                }
            ],
            "name": "print_address",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {"indexed": False, "internalType": "uint8", "name": "", "type": "uint8"}
            ],
            "name": "print_index",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256",
                }
            ],
            "name": "print_uint",
            "type": "event",
        },
        {
            "inputs": [
                {"internalType": "bytes32", "name": "routeData", "type": "bytes32"},
                {"internalType": "address", "name": "tokenA", "type": "address"},
                {"internalType": "address", "name": "tokenB", "type": "address"},
                {"internalType": "uint256", "name": "_amountIn", "type": "uint256"},
                {"internalType": "address", "name": "recipient", "type": "address"},
            ],
            "name": "BeethovenRouterSwap",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "amountCalculated",
                    "type": "uint256",
                }
            ],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "BeethovenVault",
            "outputs": [{"internalType": "contract IB", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "COUNTOFZERO",
            "outputs": [{"internalType": "uint16", "name": "", "type": "uint16"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint16", "name": "_feeAmount", "type": "uint16"}
            ],
            "name": "ChangeFeeAmount",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "FEE_PERSICION",
            "outputs": [{"internalType": "uint16", "name": "", "type": "uint16"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "FTM",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "FeeAmount",
            "outputs": [{"internalType": "uint16", "name": "", "type": "uint16"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "IcurveVyper",
            "outputs": [{"internalType": "string", "name": "", "type": "string"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "MAX_FEE_AMOUNT",
            "outputs": [{"internalType": "uint16", "name": "", "type": "uint16"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "MAX_SUPPORTED_PROTOCOLS_INDEX",
            "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "bytes32", "name": "routeData", "type": "bytes32"},
                {"internalType": "address", "name": "tokenA", "type": "address"},
                {"internalType": "address", "name": "tokenB", "type": "address"},
                {"internalType": "uint256", "name": "_amountIn", "type": "uint256"},
                {"internalType": "address", "name": "to", "type": "address"},
            ],
            "name": "SwapTokens",
            "outputs": [
                {"internalType": "uint256", "name": "amountOut", "type": "uint256"}
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "WFTM",
            "outputs": [
                {"internalType": "contract IWFTM", "name": "", "type": "address"}
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "bytes32", "name": "routeData", "type": "bytes32"},
                {"internalType": "address", "name": "tokenA", "type": "address"},
                {"internalType": "address", "name": "tokenB", "type": "address"},
                {"internalType": "uint256", "name": "_amountIn", "type": "uint256"},
                {"internalType": "address", "name": "recipient", "type": "address"},
            ],
            "name": "curveRouterAmountOutResult",
            "outputs": [
                {"internalType": "uint256", "name": "outputAmount", "type": "uint256"}
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "bytes32", "name": "routeData", "type": "bytes32"},
                {"internalType": "address", "name": "tokenA", "type": "address"},
                {"internalType": "address", "name": "tokenB", "type": "address"},
                {"internalType": "uint256", "name": "_amountIn", "type": "uint256"},
                {"internalType": "address", "name": "recipient", "type": "address"},
            ],
            "name": "curveRouterFindAmountOut",
            "outputs": [
                {"internalType": "uint256", "name": "outputAmount", "type": "uint256"}
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "cuvreTokenCounts",
            "outputs": [{"internalType": "uint16", "name": "", "type": "uint16"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "components": [
                        {
                            "internalType": "uint256",
                            "name": "minAmountOut",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "amountIn",
                            "type": "uint256",
                        },
                        {
                            "internalType": "contract IERC20",
                            "name": "tokenA",
                            "type": "address",
                        },
                        {
                            "internalType": "contract IERC20",
                            "name": "tokenB",
                            "type": "address",
                        },
                        {
                            "internalType": "uint256[]",
                            "name": "amountsIn",
                            "type": "uint256[]",
                        },
                        {
                            "internalType": "address[][]",
                            "name": "tokens",
                            "type": "address[][]",
                        },
                        {
                            "internalType": "bytes32[][]",
                            "name": "routeData",
                            "type": "bytes32[][]",
                        },
                        {
                            "internalType": "uint256",
                            "name": "bitMap",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct Request.Swap",
                    "name": "request",
                    "type": "tuple",
                }
            ],
            "name": "exchange",
            "outputs": [
                {"internalType": "uint256", "name": "_amountOut", "type": "uint256"}
            ],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "owner",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "renounceOwnership",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "newOwner", "type": "address"}
            ],
            "name": "transferOwnership",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {"stateMutability": "payable", "type": "receive"},
    ]
    ROUTER_V2 = [
        {
            "inputs": [
                {
                    "internalType": "contract ISpender",
                    "name": "_spender",
                    "type": "address",
                },
                {
                    "internalType": "contract IProxy",
                    "name": "_proxy",
                    "type": "address",
                },
            ],
            "stateMutability": "nonpayable",
            "type": "constructor",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "token",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "from",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "to",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount",
                    "type": "uint256",
                },
            ],
            "name": "DispatchTransfer",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "uint16",
                    "name": "OldAmount",
                    "type": "uint16",
                },
                {
                    "indexed": False,
                    "internalType": "uint16",
                    "name": "NewAmount",
                    "type": "uint16",
                },
            ],
            "name": "FeeAmountChange",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "oldCollector",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "newCollector",
                    "type": "address",
                },
            ],
            "name": "FeeCollectorChange",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "previousOwner",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "newOwner",
                    "type": "address",
                },
            ],
            "name": "OwnershipTransferred",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "userAddress",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "fromToken",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "toToken",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amountIn",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amountOut",
                    "type": "uint256",
                },
            ],
            "name": "Swapped",
            "type": "event",
        },
        {
            "inputs": [
                {"internalType": "bytes32", "name": "routeData", "type": "bytes32"},
                {"internalType": "address", "name": "tokenA", "type": "address"},
                {"internalType": "address", "name": "tokenB", "type": "address"},
                {"internalType": "uint256", "name": "_amountIn", "type": "uint256"},
                {"internalType": "address", "name": "recipient", "type": "address"},
            ],
            "name": "BeethovenRouterSwap",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "amountCalculated",
                    "type": "uint256",
                }
            ],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "BeethovenVault",
            "outputs": [{"internalType": "contract IB", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint16", "name": "_feeAmount", "type": "uint16"}
            ],
            "name": "ChangeFeeAmount",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "FeeCollectorAddress_",
                    "type": "address",
                }
            ],
            "name": "ChangeFeeCollectorAddress",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "contract IProxy", "name": "_proxy", "type": "address"}
            ],
            "name": "ChangeRouter",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "FEE_PERSICION",
            "outputs": [{"internalType": "uint16", "name": "", "type": "uint16"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "FTM",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "FeeAmount",
            "outputs": [{"internalType": "uint16", "name": "", "type": "uint16"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "FeeCollectorAddress",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "IcurveVyper",
            "outputs": [{"internalType": "string", "name": "", "type": "string"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "MAX_FEE_AMOUNT",
            "outputs": [{"internalType": "uint16", "name": "", "type": "uint16"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "MAX_SUPPORTED_PROTOCOLS_INDEX",
            "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "bytes32", "name": "routeData", "type": "bytes32"},
                {"internalType": "address", "name": "tokenA", "type": "address"},
                {"internalType": "address", "name": "tokenB", "type": "address"},
                {"internalType": "uint256", "name": "_amountIn", "type": "uint256"},
                {"internalType": "address", "name": "to", "type": "address"},
            ],
            "name": "SwapTokens",
            "outputs": [
                {"internalType": "uint256", "name": "amountOut", "type": "uint256"}
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "WFTM",
            "outputs": [
                {"internalType": "contract IWFTM", "name": "", "type": "address"}
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_token", "type": "address"},
                {"internalType": "address", "name": "_dexRouter", "type": "address"},
            ],
            "name": "allowance",
            "outputs": [
                {"internalType": "uint256", "name": "_amount", "type": "uint256"}
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_token", "type": "address"},
                {"internalType": "address", "name": "_dexRouter", "type": "address"},
                {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            ],
            "name": "approve",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address[]", "name": "_tokens", "type": "address[]"},
                {
                    "internalType": "address[]",
                    "name": "_dexAddresses",
                    "type": "address[]",
                },
                {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            ],
            "name": "approveInfinity",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "contract IERC20[]",
                    "name": "tokens",
                    "type": "address[]",
                }
            ],
            "name": "collectFee",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "bytes32", "name": "routeData", "type": "bytes32"},
                {"internalType": "address", "name": "tokenA", "type": "address"},
                {"internalType": "address", "name": "tokenB", "type": "address"},
                {"internalType": "uint256", "name": "_amountIn", "type": "uint256"},
                {"internalType": "address", "name": "recipient", "type": "address"},
            ],
            "name": "curveRouterAmountOutResult",
            "outputs": [
                {"internalType": "uint256", "name": "outputAmount", "type": "uint256"}
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "bytes32", "name": "routeData", "type": "bytes32"},
                {"internalType": "address", "name": "tokenA", "type": "address"},
                {"internalType": "address", "name": "tokenB", "type": "address"},
                {"internalType": "uint256", "name": "_amountIn", "type": "uint256"},
                {"internalType": "address", "name": "recipient", "type": "address"},
            ],
            "name": "curveRouterFindAmountOut",
            "outputs": [
                {"internalType": "uint256", "name": "outputAmount", "type": "uint256"}
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "cuvreTokenCounts",
            "outputs": [{"internalType": "uint16", "name": "", "type": "uint16"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "components": [
                        {
                            "internalType": "uint256",
                            "name": "minAmountOut",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "amountIn",
                            "type": "uint256",
                        },
                        {
                            "internalType": "contract IERC20",
                            "name": "tokenA",
                            "type": "address",
                        },
                        {
                            "internalType": "contract IERC20",
                            "name": "tokenB",
                            "type": "address",
                        },
                        {
                            "internalType": "uint256[]",
                            "name": "amountsIn",
                            "type": "uint256[]",
                        },
                        {
                            "internalType": "address[][]",
                            "name": "tokens",
                            "type": "address[][]",
                        },
                        {
                            "internalType": "bytes32[][]",
                            "name": "routeData",
                            "type": "bytes32[][]",
                        },
                        {
                            "internalType": "uint256",
                            "name": "bitMap",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "deadline",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct Request.Swap",
                    "name": "request",
                    "type": "tuple",
                },
                {"internalType": "address", "name": "callee", "type": "address"},
            ],
            "name": "exchange",
            "outputs": [
                {"internalType": "uint256", "name": "_amountOut", "type": "uint256"}
            ],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "owner",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "proxy",
            "outputs": [
                {"internalType": "contract IProxy", "name": "", "type": "address"}
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "renounceOwnership",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "newOwner", "type": "address"}
            ],
            "name": "transferOwnership",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {"stateMutability": "payable", "type": "receive"},
    ]
    SPENDER = [
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "user",
                    "type": "address",
                }
            ],
            "name": "AddAuthorizedEvent",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "previousOwner",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "newOwner",
                    "type": "address",
                },
            ],
            "name": "OwnershipTransferred",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "from",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "to",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amount",
                    "type": "uint256",
                },
            ],
            "name": "ProxiedTransferEvent",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "user",
                    "type": "address",
                }
            ],
            "name": "RemoveAuthorizedEvent",
            "type": "event",
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "_authorizedUser",
                    "type": "address",
                }
            ],
            "name": "addAuthorizedUser",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "owner",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "contract IERC20", "name": "token", "type": "address"},
                {"internalType": "address", "name": "from", "type": "address"},
                {"internalType": "address", "name": "to", "type": "address"},
                {"internalType": "uint256", "name": "amount", "type": "uint256"},
            ],
            "name": "proxiedTransfer",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "_authorizedUser",
                    "type": "address",
                }
            ],
            "name": "removeAuthorizedUser",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "renounceOwnership",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "newOwner", "type": "address"}
            ],
            "name": "transferOwnership",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
    ]
    PROXY = [
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "bytes",
                    "name": "response",
                    "type": "bytes",
                }
            ],
            "name": "ContractResponse",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "components": [
                        {
                            "internalType": "uint256",
                            "name": "minAmountOut",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "amountIn",
                            "type": "uint256",
                        },
                        {
                            "internalType": "contract IERC20",
                            "name": "tokenA",
                            "type": "address",
                        },
                        {
                            "internalType": "contract IERC20",
                            "name": "tokenB",
                            "type": "address",
                        },
                        {
                            "internalType": "uint256[]",
                            "name": "amountsIn",
                            "type": "uint256[]",
                        },
                        {
                            "internalType": "address[][]",
                            "name": "tokens",
                            "type": "address[][]",
                        },
                        {
                            "internalType": "bytes32[][]",
                            "name": "routeData",
                            "type": "bytes32[][]",
                        },
                        {
                            "internalType": "uint256",
                            "name": "bitMap",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "deadline",
                            "type": "uint256",
                        },
                    ],
                    "indexed": False,
                    "internalType": "struct Request.Swap",
                    "name": "_request",
                    "type": "tuple",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "_amountOut",
                    "type": "uint256",
                },
            ],
            "name": "ExchangeEvent",
            "type": "event",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "previousOwner",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "newOwner",
                    "type": "address",
                },
            ],
            "name": "OwnershipTransferred",
            "type": "event",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_router", "type": "address"},
                {"internalType": "uint256", "name": "routerIndex", "type": "uint256"},
            ],
            "name": "changeRouter",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "routerIndex", "type": "uint256"},
                {"internalType": "bytes", "name": "data", "type": "bytes"},
            ],
            "name": "emergencyRawCallWithCallee",
            "outputs": [{"internalType": "bytes", "name": "", "type": "bytes"}],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "routerIndex", "type": "uint256"},
                {
                    "components": [
                        {
                            "internalType": "uint256",
                            "name": "minAmountOut",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "amountIn",
                            "type": "uint256",
                        },
                        {
                            "internalType": "contract IERC20",
                            "name": "tokenA",
                            "type": "address",
                        },
                        {
                            "internalType": "contract IERC20",
                            "name": "tokenB",
                            "type": "address",
                        },
                        {
                            "internalType": "uint256[]",
                            "name": "amountsIn",
                            "type": "uint256[]",
                        },
                        {
                            "internalType": "address[][]",
                            "name": "tokens",
                            "type": "address[][]",
                        },
                        {
                            "internalType": "bytes32[][]",
                            "name": "routeData",
                            "type": "bytes32[][]",
                        },
                        {
                            "internalType": "uint256",
                            "name": "bitMap",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "deadline",
                            "type": "uint256",
                        },
                    ],
                    "internalType": "struct Request.Swap",
                    "name": "_request",
                    "type": "tuple",
                },
            ],
            "name": "exchange",
            "outputs": [
                {"internalType": "uint256", "name": "_amountOut", "type": "uint256"}
            ],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "owner",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "renounceOwnership",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "name": "router",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "routerIndex", "type": "uint256"},
                {"internalType": "bytes", "name": "data", "type": "bytes"},
            ],
            "name": "safeRawCallWithCallee",
            "outputs": [{"internalType": "bytes", "name": "", "type": "bytes"}],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "newOwner", "type": "address"}
            ],
            "name": "transferOwnership",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
    ]
    ROUTER_SP = [
        {
            "inputs": [
                {"internalType": "address", "name": "_data_storage", "type": "address"}
            ],
            "stateMutability": "nonpayable",
            "type": "constructor",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "userAddress",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "fromToken",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "toToken",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amountIn",
                    "type": "uint256",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "amountOut",
                    "type": "uint256",
                },
            ],
            "name": "Swapped",
            "type": "event",
        },
        {
            "inputs": [],
            "name": "FTM",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "IcurveVyper",
            "outputs": [{"internalType": "string", "name": "", "type": "string"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "WFTM",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_token", "type": "address"},
                {"internalType": "address", "name": "_dexRouter", "type": "address"},
            ],
            "name": "allowance",
            "outputs": [
                {"internalType": "uint256", "name": "_amount", "type": "uint256"}
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_token", "type": "address"},
                {"internalType": "address", "name": "_dexRouter", "type": "address"},
                {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            ],
            "name": "approve",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address[]", "name": "_tokens", "type": "address[]"},
                {
                    "internalType": "address[]",
                    "name": "_dexAddresses",
                    "type": "address[]",
                },
                {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            ],
            "name": "approveInfinity",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_new_owner", "type": "address"}
            ],
            "name": "changeOwner",
            "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "cuvreTokenCounts",
            "outputs": [{"internalType": "uint16", "name": "", "type": "uint16"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address payable", "name": "_owner", "type": "address"}
            ],
            "name": "destroySmartContract",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "components": [
                        {
                            "internalType": "uint256",
                            "name": "minAmountOut",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "amountIn",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256[]",
                            "name": "amountsIn",
                            "type": "uint256[]",
                        },
                        {
                            "internalType": "uint16[][]",
                            "name": "dexs",
                            "type": "uint16[][]",
                        },
                        {
                            "internalType": "address[][]",
                            "name": "paths",
                            "type": "address[][]",
                        },
                        {
                            "internalType": "address[][]",
                            "name": "pool",
                            "type": "address[][]",
                        },
                        {
                            "internalType": "bool",
                            "name": "withdrawFlag",
                            "type": "bool",
                        },
                    ],
                    "internalType": "struct ProxySupportingFee.Swap",
                    "name": "route",
                    "type": "tuple",
                }
            ],
            "name": "exchange",
            "outputs": [
                {"internalType": "uint256", "name": "_amountOut", "type": "uint256"}
            ],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_token", "type": "address"}
            ],
            "name": "transferToOwner",
            "outputs": [
                {"internalType": "uint256", "name": "_token_amount", "type": "uint256"}
            ],
            "stateMutability": "payable",
            "type": "function",
        },
        {"stateMutability": "payable", "type": "receive"},
    ]
    BSC_ROUTER = [
        {
            "inputs": [
                {"internalType": "address", "name": "_token", "type": "address"},
                {"internalType": "address", "name": "_dexRouter", "type": "address"},
                {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            ],
            "name": "_approve",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address[]", "name": "_tokens", "type": "address[]"}
            ],
            "name": "_approveInfinity",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "newOwner", "type": "address"}
            ],
            "name": "changeOwner",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {
                    "components": [
                        {
                            "internalType": "uint256",
                            "name": "minAmountOut",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256",
                            "name": "amountIn",
                            "type": "uint256",
                        },
                        {
                            "internalType": "uint256[]",
                            "name": "amountsIn",
                            "type": "uint256[]",
                        },
                        {
                            "internalType": "uint16[][]",
                            "name": "dexs",
                            "type": "uint16[][]",
                        },
                        {
                            "internalType": "address[][]",
                            "name": "paths",
                            "type": "address[][]",
                        },
                        {
                            "internalType": "address[][]",
                            "name": "pool",
                            "type": "address[][]",
                        },
                        {
                            "internalType": "bool",
                            "name": "withdrawflag",
                            "type": "bool",
                        },
                    ],
                    "internalType": "struct Proxy.Swap",
                    "name": "route",
                    "type": "tuple",
                }
            ],
            "name": "exchange",
            "outputs": [
                {"internalType": "uint256", "name": "_amountOut", "type": "uint256"}
            ],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "oldOwner",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "newOwner",
                    "type": "address",
                },
            ],
            "name": "OwnerSet",
            "type": "event",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "_token", "type": "address"}
            ],
            "name": "transfertome",
            "outputs": [
                {"internalType": "uint256", "name": "_tknBalance", "type": "uint256"}
            ],
            "stateMutability": "payable",
            "type": "function",
        },
        {"stateMutability": "payable", "type": "receive"},
        {
            "inputs": [
                {"internalType": "address", "name": "_token", "type": "address"},
                {"internalType": "address", "name": "_dexRouter", "type": "address"},
            ],
            "name": "_allowance",
            "outputs": [
                {"internalType": "uint256", "name": "_amount", "type": "uint256"}
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "AcryptoS",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "acryptosstablecount",
            "outputs": [{"internalType": "uint16", "name": "", "type": "uint16"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "name": "allRouters",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "Apeswap",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "BakerySwap",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "BNB",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "DODOV1",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "DODOV2",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "Ellipsis",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "ellipsisstablcount",
            "outputs": [{"internalType": "uint16", "name": "", "type": "uint16"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "getOwner",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "IcurveVyper",
            "outputs": [{"internalType": "string", "name": "", "type": "string"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "JulSwap",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "MDex",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "PancakeSwapV1",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "PancakeSwapV2",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "StreetSwap",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "SushiSwap",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "SwipSwap",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "TwindexSwap",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "ValueLiquidityPool",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "WaultSwap",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "WBNB",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
    ]
