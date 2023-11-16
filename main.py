import webbrowser

import telebot

bot = telebot.TeleBot('6410141456:AAHPadR2RJZ-i56xmWTpPQ_dSZ9iK58ZTk8')

@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://ori4life.ru')

@bot.message_handler(commands=['converter'])
def conv(message):
    bot.send_message(message.chat.id, f'Вы зашли в конвертер!')


@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Помощь')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        print('зашли сюда')
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')

    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
        print('зашли вот сюда')

bot.infinity_polling()