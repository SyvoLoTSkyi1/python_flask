from flask import Flask, request

from utils import get_filtered_customers, get_repeat_customers_by_sql, get_profit_by_sql, \
    get_repeat_customers_by_python, get_profit_by_python


app = Flask(__name__)


@app.route('/filtered_customers', methods=['GET'])
def filtered_customers():
    city = request.args.get('city', default=None)
    state = request.args.get('state', default=None)
    result = get_filtered_customers(city, state)
    return result


@app.route('/sql_repeat_customers')
def repeat_customers_sql():
    return get_repeat_customers_by_sql()


@app.route('/py_repeat_customers')
def repeat_customers_py():
    return get_repeat_customers_by_python()


@app.route('/sql_get_profit')
def get_profit_sql():
    return get_profit_by_sql()

