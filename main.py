# import telegram
# chat_id = colocar o id do chat do heades
# bot = telegram.Bot(token='6018080288:AAFyspXm_Is-y7re2GKpOC2P6H9Od_KRMco')
# print(bot.get_me())
#
# atualizacoes = bot.get_updates()
#
#
# bot.send_message(text="Ola  Aqui é sue chat bot", chat_id=99999999999
import locale
from datetime import datetime
from time import sleep

import requests
import telegram
locale.setlocale(locale.LC_ALL, 'pr_BR.UTF-8')


bot = telegram.Bot(token='6018080288:AAFyspXm_Is-y7re2GKpOC2P6H9Od_KRMco')

URL_BASE = 'https://api.coingecko.com/api/v3'
ENDPOINT_PING = f'{URL_BASE}/ping'
ENDPOINT_PRECOS = f'{URL_BASE}/simple/price'

while True:
    resposta = requests.get(ENDPOINT_PING)

    if resposta.status_code == 200:
        url = f'{ENDPOINT_PRECOS}?ids=ethereum&vs_currencies=BRL&include_last_updated_at=true'

        resposta = requests.get(url).json()

        dados_da_moeda = resposta.get('ethereum', None)
        preco = dados_da_moeda.get('brl', None)
        atualizado_em = dados_da_moeda.get('last_updated_at', None)
        data_hora = datetime.fromtimestamp(atualizado_em).strftime('%x %X')

        mensagem = None

        if preco < 8000:
            mensagem = f'*Cotação do Ethereum:* \n\t*Preço:* R$: {preco}' \
                       f'\n\t*Horário*: {data_hora}\n\t*Motivo*: Valor menor que o minimo'
        elif preco > 9000:
            mensagem = f'*Cotação do Ethereum:* \n\t*Preço:* R$: {preco}' \
                       f'\n\t*Horário*: {data_hora}\n\t*Motivo*: Valor maior que o máximo'

        if mensagem:
            bot.send_message(text=mensagem, chat_id=, parse_mode=telegram.ParseMode.MARKDOWN)

    else:
        print('API OFFline')

    sleep(300)
