import requests

from datetime import datetime


def get_currency_iso_code(currency: str) -> int:
    currency_dict = {
        'UAH': 980,
        'USD': 840,
        'EUR': 978,
        'GBP': 826,
        'AZN': 944,
        'CAD': 124,
        'PLN': 985
    }
    try:
        return currency_dict[currency]
    except:
        raise KeyError('Currency not found! Update currencies information')
