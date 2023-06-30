import requests


data = requests.get("https://tiptop.ua/shop/noutbuky")
print(data.text)