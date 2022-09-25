# Адыев Тимур FPW-85 Skillfactory
# Итоговая практическая работа по курсу ООП
# Telegram Bot, по запросу выдающий актуальный курс валюты (доллар, евро, рубль)

#   В config.py, хранятся TOKEN данного Бота, APIKey для доступа к сайту, c которого будет
#               браться актуальный курс валют, и список доступных к конвертации типов валют
import config

#   В extensions хранятся классы исключений ConvertionException и Convert, содержащий в себе метод get_prise, отправляющий
#               запрос на сервер и возвращающий актуальный курс
from extensions import Convert, ConvertionException

import telebot

bot = telebot.TeleBot(config.TOKEN)

#  Приветствие от Бота
@bot.message_handler(commands=['start'])
def hello(message: telebot.types.Message):
    sti = open('static/giphy.mp4', 'rb')
    bot.send_video(message.chat.id, sti)
    text = f'Приветствую! Для того, чтобы ознакомиться с инструкцией введите команду /help.\n' \
           f'Если вы ознакомлены с инструкцией, то можете ввести ваш запрос.'
    bot.send_message(message.chat.id, text)


#  Вывод инструкции при запросе /help
@bot.message_handler(commands=['help'])
def instr(message: telebot.types.Message):
    text = f'Запрос должен быть выполнен в следующей форме:\n' \
           f'<FROM> <TO> <AMOUNT>\n' \
           f'<FROM> - валюта, цена которой вас интересует.\n' \
           f'<TO> - валюта, в которой надо узнать цену интересующей вас валюты.\n' \
           f'<AMOUNT> - количество конвертируемой валюты.\n' \
           f'Для того, чтобы ознакомиться со списком доступной к конвертации валюты воспользуйтесь командой /values.'
    bot.reply_to(message, text)


#  Вывод списка доступной к конвертации валюты при запросе /values
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = f'Для конвертации доступны: '
    for key in config.keys.keys():
        text = '\n'.join((text, key.upper(), ))
    bot.reply_to(message, text)


#  Вывод актуального курса для запрашиваемых типов и количества валюты
@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.lower().split(' ')

        if len(values) != 3:
            raise ConvertionException('Необходимо ввести три параметра!')

        base, quote, amount = values
        total_base = Convert.get_price(base, quote, amount)
    except ConvertionException as e:
        bot.reply_to(message, f"Неверный формат ввода данных.\n{e}")
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Стоимость {amount} {config.keys[base]} в {config.keys[quote]} равна {total_base}.'
        bot.send_message(message.chat.id, text)


bot.polling()
