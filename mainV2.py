import locale
from datetime import datetime
from time import sleep
from classes import CoinGeckoAPI, TelegramBot
locale.setlocale(locale.LC_ALL, 'pr_BR.UTF-8')

api = CoinGeckoAPI(url_base='https://api.coingecko.com/api/v3')
bot = TelegramBot(token='6018080288:AAFyspXm_Is-y7re2GKXuhpOC2P6H9Od_KRMco', chat_id=999999)


while True:

    if api.ping():
        print('API Online')
        preco, atualizado_em = api.consulta_preco(id_moeda='ethereum')
        print('Consulta realizada com sucesso')
        data_hora = datetime.fromtimestamp(atualizado_em).strftime('%x %X')
        mensagem = None

        if preco < 8000:
            mensagem = f'*Cotação do Ethereum:* \n\t*Preço:* R$: {preco}' \
                       f'\n\t*Horário*: {data_hora}\n\t*Motivo*: Valor menor que o minimo'
        elif preco > 9000:
            mensagem = f'*Cotação do Ethereum:* \n\t*Preço:* R$: {preco}' \
                       f'\n\t*Horário*: {data_hora}\n\t*Motivo*: Valor maior que o máximo'

        if mensagem:
            bot.envia_mensagem(texto_markdown=mensagem)

    else:
        print('API OFFline')

    sleep(300)
