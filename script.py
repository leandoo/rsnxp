import hmac
import json
import hashlib
import time
import requests

# Definindo as credenciais da API da Binance
api_key = 'f15V4VrGEROjW8khfcjbdciCdKPXLly3x3w1e0RtJ70Wtg94tuZSi9dOnMlae7Tg'
api_secret = 'OcVZgpHQ6sFUAbxBKHmn8Bhns9lSwl4MECSw864iKgyQUiBwRQNqdWTwaOcuvnzb'

# Definindo as informações para as ordens de compra e venda
symbol = 'BTCBRL'
amount = '40'
order_side_sell = 'SELL'
order_side_buy = 'BUY'
profit_threshold = 1  # Em percentual

# Definindo as informações da API da Binance
endpoint = 'https://api.binance.com'
method = '/api/v3/order'
headers = {'X-MBX-APIKEY': api_key}

# Função para realizar ordem de compra ou venda
def place_order(order_side, symbol, amount):
    timestamp = int(time.time() * 1000)
    params = {
        'symbol': symbol,
        'side': order_side,
        'type': 'MARKET',
        'quoteOrderQty': amount,
        'timestamp': timestamp
    }

    query_string = '&'.join([f'{k}={v}' for k, v in params.items()])
    signature = hmac.new(api_secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

    url = f'{endpoint}{method}?{query_string}&signature={signature}'
    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(response.json())
        return None

# Função para obter a cotação atual do par de moedas
def get_ticker_price():
    url = f'{endpoint}/api/v3/ticker/price?symbol={symbol}'
    response = requests.get(url)

    if response.status_code == 200:
        return float(response.json()['price'])
    else:
        print(response.json())
        return None

# Loop infinito para monitorar o preço do par de moedas e realizar as ordens
while True:
    price = get_ticker_price()

    if price is not None:
        # Verifica se o preço subiu o suficiente para realizar a venda
        if price >= (1 + (profit_threshold / 100)) * float(amount):
            place_order(order_side_sell, symbol, amount)
            print(f'{symbol} vendido por {price} BRL')

        # Verifica se o preço caiu o suficiente para realizar a compra
        elif price <= (1 - (profit_threshold / 100)) * float(amount):
            place_order(order_side_buy, symbol, amount)
            print(f'{symbol} comprado por {price} BRL')
            
# Função para obter o saldo em criptomoedas
def get_crypto_balance(asset):
    timestamp = int(time.time() * 1000)
    params = {
        'timestamp': timestamp
    }

    query_string = '&'.join([f'{k}={v}' for k, v in params.items()])
    signature = hmac.new(api_secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

    url = f'{endpoint}/api/v3/account?{query_string}&signature={signature}'
    headers = {'X-MBX-APIKEY': api_key}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        balances = response.json()['balances']
        for balance in balances:
            if balance['asset'] == asset:
                return float(balance['free'])
    else:
        print(response.json())
        return None

# Obter saldo em Bitcoin e exibir na tela
btc_balance = get_crypto_balance('BTC')
print(f'Saldo em BTC: {btc_balance}')

# Espera 5 segundos até a próxima iteração
time.sleep(5)
