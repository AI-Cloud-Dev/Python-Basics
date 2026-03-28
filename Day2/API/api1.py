import requests
try:
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
    if response.status_code == 200:
        data = response.json()
        print("BTC in USD:", data['bitcoin']['usd'])
        # print("sucess")
except ValueError as e:
    print("API error:", e)
    print("API error:", response.status_code)
