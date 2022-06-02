import requests
import json

moedas_favoritas = []
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
# Retorno: array
def consult_price():
    arr_prices = []

    for currency in moedas_favoritas:
        data_currency = request_currency(currency)
        if data_currency:
            json_data_currency = json.loads(data_currency.text)

            price = str(round(float(json_data_currency["ticker"]["last"]), 2))
            arr_prices.append(currency + ': R$' + price)

    return arr_prices

def add_favorites(currency):
    if check_currency(currency):
        moedas_favoritas.append(currency)
        return "Adicionamos " + currency + " aos seus favoritos, deseja favoritar outra?"

    return "Moeda não encontrada"