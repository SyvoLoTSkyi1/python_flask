import requests


def get_currancy_exchange_rate(date: str, currency_base: str,
                               currency_exchange: str, bank: str) -> str:
    response = requests.get(f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}')
    json = response.json()

    if response.status_code == 200:
        exchange_rate = json['exchangeRate']
        for i in range(len(exchange_rate)):
            if exchange_rate[i].get('baseCurrency') == currency_base \
                    and exchange_rate[i].get('currency') == currency_exchange:

                if bank == 'NB':
                    rate_buy = exchange_rate[i].get('purchaseRateNB')
                    rate_sell = exchange_rate[i].get('saleRateNB')
                    return f'NB`s exchange rate {currency_base} to {currency_exchange} ' \
                           f'for {date}: rate buy - {rate_buy},  rate sell - {rate_sell}'

                elif bank == 'PB':
                    rate_buy = exchange_rate[i].get('purchaseRate')
                    rate_sell = exchange_rate[i].get('saleRate')
                    return f'PB`s exchange rate {currency_base} to {currency_exchange} ' \
                           f'for {date}: rate buy - {rate_buy},  ' \
                           f'rate sell - {rate_sell}'

                else:
                    return f'Error: bank as {bank} not found'
            else:
                return f'Error: exchange rate {currency_base} to {currency_exchange} not found'

    else:
        f'Api error {response.status_code}: {json.get("errorDescription")}'
