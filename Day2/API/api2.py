import json, requests

try:
    btc_api = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    data = requests.get(btc_api).json()
    
    with open("btc.json", "w") as f:
        json.dump(data, f)
except ValueError as e:
    print("error")

    