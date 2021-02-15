import requests, os

from requests.models import HTTPBasicAuth

address = os.environ.get('ethereum_address')
etherscan_api_key = os.environ.get('etherscan_apikey')
cmc_apikey = os.environ.get('cmc_apikey')

json = requests.get(f"https://api.etherscan.io/api?module=account&action=tokentx&address={address}&startblock=0&endblock=999999999&sort=asc&apikey={etherscan_api_key}").json()
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

my_headers = {'X-CMC_PRO_API_KEY' : f"{cmc_apikey}"}
response = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest', headers=my_headers)
price = 0
for entry in response.json()['data']:
    if (entry['symbol'] == 'GRT'):
        price = entry['quote']['USD']['price']
print(f"Wallet value: ${price*currencies['GRT']}")
