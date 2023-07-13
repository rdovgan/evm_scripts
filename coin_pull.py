from requests import Request, Session
# TODO need to refactor this
import resources.variables as config
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

cmk_api_key = config.CMK_API_KEY
cmk_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
cmk_quote = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol='

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': cmk_api_key,
}

session = Session()
session.headers.update(headers)


def get_quote_for_coin(coin_code):
    try:
        response = session.get(cmk_quote + coin_code.upper())
        data = json.loads(response.text)
        print(data)
        try:
            if data['status'] is None or data['status']['error_code'] != 0:
                print(data['status']['error_message'] + '. Try again or press `/cancel`')
                return
        except KeyError as e:
            print(e)
        coin_info = define_coin_info(coin_code, data)
        return coin_info
    except (ConnectionError, Timeout, TooManyRedirects, KeyError, TypeError) as e:
        print(e)


def define_coin_info(coin_code, data):
    dto = data['data'][coin_code.upper()]
    quote = dto['quote']['USD']

    info = dto['name'] + '\n' + 'Rank: ' + str(dto['cmc_rank']) + '\n'
    info = info + 'Price: ' + define_coin_price(quote['price']) + '\n'
    info = info + 'Percent change for last day: ' + define_coin_percent_change(quote['percent_change_24h']) + '\n'
    info = info + 'Capitalization: ' + define_capitalization(quote['market_cap'])
    return info


def get_all_coins_price(parameter):
    try:
        if 'cancel' in parameter.lower():
            return
        limit = 100
        try:
            limit = int(parameter)
        except ValueError:
            print('It\'s wrong number. Please, input correct number or type `/cancel`')
        response = session.get(cmk_url, params=define_parameters(limit))
        data = json.loads(response.text)
        print(data['status'])
        coins = ''
        count = 0
        for item in data['data']:
            coins = coins + str(item['cmc_rank']) + '   ' + item['symbol'] + ' (' + define_coin_price(
                item['quote']['USD']['price']) + ')\n' + '----------------' + '\n'
            count = count + 1
            if count >= 50:
                count = 0
                print(coins)
                coins = ''
        if count > 0:
            print(coins)
        return coins
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def define_parameters(limit):
    return {
        'start': '1',
        'limit': limit,
        'convert': 'USD'
    }


def define_coin_price(price_str):
    try:
        price = float(price_str)
        if price > 10:
            return str(round(price, 2))
        elif price > 0.1:
            return str(round(price, 4))
        else:
            return str(round(price, 6))
    except ValueError:
        return '0.0'


def define_capitalization(capitalization):
    try:
        return f'{round(capitalization,0):,}'
    except ValueError:
        return '0.0'


def define_coin_percent_change(percent):
    try:
        if percent > 10:
            return str(round(percent, 1))
        elif percent > 1:
            return str(round(percent, 2))
        else:
            return str(round(percent, 3))
    except ValueError:
        return '0.0'
