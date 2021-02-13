import requests, os

address = os.environ.get('ethereum_address')
api_key = os.environ.get('etherscan_apikey')
json = requests.get(f"https://api.etherscan.io/api?module=account&action=tokentx&address={address}&startblock=0&endblock=999999999&sort=asc&apikey={api_key}").json()
result = json['result']

print("Your ERC-20 Wallet balance:")
currencies = {}
for entry in result:
    token = entry['tokenSymbol']
    tokenDecimal = int(entry['tokenDecimal'])
    tokenCount = float(entry['value']) / (10 ** tokenDecimal)
    if token in currencies:
        data = {token: currencies.get(token) + tokenCount}
        currencies.update(data)
    else:
        data = {token: tokenCount}
        currencies.update(data)
for token in currencies:
    print(f"{token}: {currencies.get(token)}")