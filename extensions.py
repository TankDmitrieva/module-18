# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json

import requests

from config import keys


class APIException(Exception):
    pass


class GetPrice:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'При конвертации {amount} {base} в {base} получилось {amount}. Как неожиданно...')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не определить валюту {quote}. \nПосмотреть допустимые варианты можно с помощью команды /values.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось определить валюту {base}. \nПосмотреть допустимые варианты можно с помощью команды /values.')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Указанное количество не является допустимым. Введите положительное число.')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        total_base *= amount
        return total_base
