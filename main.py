import requests

url = 'https://api.exchangerate.host/convert'
params = {'from': 'USD', 'to': 'EUR'}

response = requests.get(url, params=params)
data = response.json()

if 'result' in data:
    conversion_rate = data['result']
    print(f"The conversion rate from USD to EUR is: {conversion_rate}")
else:
    print("Failed to retrieve conversion rate")
