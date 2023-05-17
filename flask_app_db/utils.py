import os
from typing import List

from db_utils import execute_query


def get_filtered_customers(city=None, state=None) -> List:
    '''
    Returns customers filtered by city and state
     :param city: city
    :param state: state
    :return: client's list
    '''
    db_path = os.path.join(os.getcwd(), 'chinook.db')
    query_sql = f'''
        SELECT *
          FROM customers
    '''
    if city and state:
        query_sql += f"   WHERE City = '{city}' AND STATE = '{state}';"
    elif city:
        query_sql += f"   WHERE City = '{city}';"
    elif state:
        query_sql += f"   WHERE State = '{state}';"
    return execute_query(query_sql, db_path)


def get_repeat_customers_by_sql() -> List:
    '''
    Returns first name and ones count repeating. Using SQL
    :return: first name and count repeating
    '''
    db_path = os.path.join(os.getcwd(), 'chinook.db')
    query_sql = '''
        SELECT FirstName, count(FirstName)
          FROM customers
          GROUP BY FirstName
          HAVING count(FirstName) > 0;
    '''
    return execute_query(query_sql, db_path)


def get_repeat_customers_by_python() -> List:
    '''
    Returns first name and one's count repeating. Using Python
    :return: first name and count repeating
    '''
    query_sql = '''
        SELECT FirstName
          FROM customers;
    '''
    db_path = os.path.join(os.getcwd(), 'chinook.db')
    repeat_customers = {}
    for i in execute_query(query_sql, db_path):
        repeat = execute_query(query_sql, db_path).count(i)
        repeat_customers.update({i: repeat})

    return list(repeat_customers.items())


def get_profit_by_sql() -> List:
    '''
    Returns total amount orders. Using SQL
    :return: total amount of orders
    '''
    db_path = os.path.join(os.getcwd(), 'chinook.db')
    query_sql = '''
        SELECT sum(UnitPrice*Quantity)
          FROM invoice_items;
    '''
    return execute_query(query_sql, db_path)
