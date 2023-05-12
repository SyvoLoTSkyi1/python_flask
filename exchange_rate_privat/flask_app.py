from flask import Flask, request

from utils import get_currancy_exchange_rate

app = Flask(__name__)


@app.route('/rates', methods=['GET'])
def get_rates():
    date = request.args.get('date', default='11.05.2023')
    currency_base = request.args.get('currency_base', default='UAH')
    currency_exchange = request.args.get('currency_exchange', default='EUR')
    bank = request.args.get('bank', default='PB')
    result = get_currancy_exchange_rate(date, currency_base, currency_exchange, bank)
    return result
