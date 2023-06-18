import requests
from InquirerPy import prompt
import json

question = [
    {
        "type": "list",
        "message": "\nWhat's the currency you want to convert?",
        "choices": ["INR", "USD", "EUR","JPY" ,"CNY","KRW","SGD","NZD","CAD","ZAR"]
    },
    {
        "type": "list",
        "message": "\nWhat's the currency you want to convert into?",
        "choices": ["INR", "USD", "EUR","JPY" ,"CNY","KRW","SGD","NZD","CAD","ZAR"]
    }
]
result = prompt(question)
cur1=result[0]
cur2=result[1]


amount=float(input("\nEnter the amount to convert :"))

url = 'https://api.exchangerate.host/convert'
params = {'from': cur1, 'to': cur2}

response = requests.get(url, params=params)
data = response.json()

if 'result' in data:
    rate = data['result']
    print("\nThe conversion rate from",cur1,"to",cur2, "is:", rate)
else:
    print("\nFailed to retrieve conversion rate")

print("\nTherefore the amount after conversion is:",amount*rate,"\n")

