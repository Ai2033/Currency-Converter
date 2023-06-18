import requests
from InquirerPy import prompt
import json

question1 = [
    {
        "type": "list",
        "message": "What's the currency you want to convert?",
        "choices": ["INR", "USD", "EUR","JPY" ,"CNY","KRW","SGD","NZD","CAD","ZAR"]
    },
    {
        "type": "list",
        "message": "What's the currency you want to convert into?",
        "choices": ["INR", "USD", "EUR","JPY" ,"CNY","KRW","SGD","NZD","CAD","ZAR"]
    }
]
result = prompt(question1)
cur1=result[0]
cur2=result[1]


amount=float(input("Enter the amount to convert :"))

url = 'https://api.exchangerate.host/convert'
params = {'from': cur1, 'to': cur2}

response = requests.get(url, params=params)
data = response.json()

if 'result' in data:
    rate = data['result']
    print("The conversion rate from",cur1,"to",cur2, "is:", rate)
else:
    print("Failed to retrieve conversion rate")

print("Therefore the amount after conversion is:",amount*rate)

