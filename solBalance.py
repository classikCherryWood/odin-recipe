

import requests

url = "https://docs-demo.solana-mainnet.quiknode.pro/"

headers = {
    "Content-Type": "application/json"
}

data = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "getBalance",
    "params": [
        "DRU8zKcYPMTRWfP8jaLjAc8HXzWAtZreLEcybkhUpRf",
        {"encoding": "base58"}
    ]
}

response = requests.post(url, headers=headers, json=data)
print(response.json())