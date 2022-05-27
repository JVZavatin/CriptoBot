import requests
import json

# Obtem os dados da moeda na corretora
# Parâmetros: currency - string
# Retorno: string
def request_currency(currency):
    request_url = "https://www.mercadobitcoin.net/api/" + currency + "/ticker/"
    data_currency = requests.get(request_url)

    return data_currency

# Checa se a moeda existe na corretora
# Parâmetros: currency - string
# Retorno: boolean
def check_currency(currency):

    data_currency = request_currency(currency)
    
    return True if data_currency else False

# Obtem o preço do array de moedas
# Parâmetros: arr_favorite_coins - array
# Retorno: array
def consult_price(arr_favorite_coins):
    arr_prices = []

    for currency in arr_favorite_coins:
        data_currency = request_currency(currency)
        if data_currency:
            json_data_currency = json.loads(data_currency.text)

            price = str(round(float(json_data_currency["ticker"]["last"]), 2))
            arr_prices.append(currency + ': R$' + price)

    return arr_prices

print(consult_price(['BTC', 'ETH', 'ADA', 'USDT']))