# MinhaPrimeiraAPI
API de cotação de dolar usando Python

Claro, aqui está um exemplo de texto para o README do seu projeto de API de cotação de dólar:

---

# API de Cotação de Dólar

Esta é uma API simples para consultar a cotação atual do dólar. Ideal para desenvolvedores que precisam integrar informações de câmbio em seus aplicativos ou serviços.

## Endpoints Disponíveis

### cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
Retorna a cotação atual do dólar em relação à moeda local.

#### Exemplo de Uso:
```
cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

Resposta:
{
  "Cotação do dolar": "R$ 5,4821"
  "Atualização": "2024-06-26 09:16:58"
}
```

## Como Usar

1. Faça uma requisição GET para `/https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL`.
2. A resposta será um JSON contendo a data da cotação, o valor atual do dólar e a fonte da informação.
3. Utilize os dados recebidos conforme necessário em seu aplicativo.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar este projeto.

## Licença

Este projeto não está licenciado.

---

Sinta-se à vontade para personalizar este texto de acordo com os detalhes específicos do seu projeto e incluir mais informações conforme necessário.
