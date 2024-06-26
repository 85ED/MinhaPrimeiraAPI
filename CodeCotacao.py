import requests
import json

# esse link pode mudar se os donos da API mudarem
cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
cotacao_dolar = cotacoes['USDBRL']["bid"]
data = cotacoes['USDBRL']["create_date"]
ComVirgula = str(cotacao_dolar).replace('.', ',')
print("Cotação do dolar: R$ "+ ComVirgula)
print("Atualização: " + data)
