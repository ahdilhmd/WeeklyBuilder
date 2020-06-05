import requests



bitcoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
response = requests.get(bitcoin_api_url)
response_json = response.json()
# type(response_json) # The API returns a list



# Bitcoin data is the first element of the list
bitcoin = response_json[0]

print(bitcoin)