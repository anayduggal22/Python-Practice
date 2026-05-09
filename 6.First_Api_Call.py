import requests

r = requests.get(
    "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
)

print(r.status_code)
print(r.text)

data = r.json()  # Converts JSON to Python dictionary

print(data['bitcoin']['usd'])