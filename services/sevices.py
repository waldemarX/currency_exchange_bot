import requests

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()


def get_currency(text: str) -> tuple:
    currency = data["Valute"][text]["Name"]
    price = str(data["Valute"][text]["Value"])
    return currency, price
