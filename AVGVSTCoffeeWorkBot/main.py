import telebot
import config


bot = telebot.TeleBot(config.TOKEN)

recipes = {}


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Салют, {0.first_name}'.format(message.from_user, bot.get_me()),
                     parse_mode='html')

    sti = open('static/giphy.mp4', 'rb')
    bot.send_video(message.chat.id, sti)


@bot.message_handler(content_types=['photo'])
def haha(message: telebot.types.Message):
    bot.reply_to(message, 'Nice MEME XD')




bot.polling(none_stop=True)