import requests
import json

import config


class ConvertionException(Exception):
    pass


class Convert:
    @staticmethod
    def get_price(base=str, quote=str, amount=str):

        if quote == base:
            raise ConvertionException(f'Вы ввели одинаковые типы валют: {base}.')

        try:
            quote_ticker = config.keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось конвертировать валюту: {quote}.\n'
                                      f'Проверьте правильность ввода. При необходимости обратитесь к инструкции.')

        try:
            base_ticker = config.keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось конвертировать валюту: {base}.\n'
                                      f'Проверьте правильность ввода. При необходимости обратитесь к инструкции.')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось конвертировать данное количество ("{amount}") валюты.\n'
                                      f'Проверьте правильность ввода. При необходимости обратитесь к инструкции.')

        url = f"https://api.apilayer.com/currency_data/convert?to={quote_ticker}&from={base_ticker}&amount={amount}"
        req = requests.request('GET', url, headers=config.headers)
        total_base = json.loads(req.content)['result']

        return total_base
