import requests

COINMARKETCAP_API_KEY = ''
def fetch_top_cryptos(api_key, limit=100):
    base_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    params = {
        'start': '1',
        'limit': str(limit),
        'convert': 'USD'
    }

    response = requests.get(base_url, headers=headers, params=params)
    
    if response.status_code == 200:
        cryptos = response.json()['data']
        for i, crypto in enumerate(cryptos, start=1):
            print(f"{i}. {crypto['name']} ({crypto['symbol']}): ${crypto['quote']['USD']['market_cap']}")
        return cryptos
    else:
        print("Failed to fetch market data")
        return None
    
top_100 = fetch_top_cryptos()
print(top_100)
