import telebot
from telebot import types

bot = telebot.TeleBot('6410141456:AAHPadR2RJZ-i56xmWTpPQ_dSZ9iK58ZTk8')
user_data = {}
user_data.update({'cnt': 0, 'ball': 0})

@bot.message_handler(commands=['start', 'play', 'go'])
def start(message):

    user_data.update({message.chat.id: {'cnt': 0, 'ball': 0}})
    user_data[message.chat.id]['cnt'] = 0
    user_data[message.chat.id]['ball'] = 0
    bot.send_message(message.chat.id, 'Привет вы находитесь в чат боте ОГЭ информатика! ')
    markup = types.InlineKeyboardMarkup()
    var1 = types.InlineKeyboardButton(f'Вариант 1', callback_data='Вариант 1')
    markup.row(var1)
    bot.send_message(message.chat.id, f'Выберете вариант!', reply_markup=markup)


@bot.message_handler()
def result(message):

    otvets = ['барс', 'монгол', '32', '10', '6', '4', '7341256', '111', '27', '25']
    if message.text.lower() == otvets[user_data[message.chat.id]['cnt']]:
        bot.reply_to(message, f'Правильно!')
        user_data[message.chat.id]['cnt'] += 1
        user_data[message.chat.id]['ball'] += 1
        new(message)
    else:
        bot.reply_to(message, f'Неправильно')
        markup2 = types.InlineKeyboardMarkup()
        reset = types.InlineKeyboardButton(f'Сначала', callback_data="Сначала")
        next_num = types.InlineKeyboardButton(f'Следующий номер', callback_data="Следующий номер")
        old_num = types.InlineKeyboardButton(f'Предыдущий номер', callback_data="Предыдущий номер")
        markup2.row(next_num, old_num, reset)

        bot.send_message(message.chat.id, f'Пробуйте отвечать дальше или выберете,что делать дальше!', reply_markup=markup2)


@bot.message_handler()
def new(message):
    try:
        file = open(f"./var1/{user_data[message.chat.id]['cnt']}.png", 'rb')
        bot.send_photo(message.chat.id, file)
        messtime(message)

    except FileNotFoundError:
        print('Файлы кончились')
        bot.send_message(message.chat.id, f'Задания закончились вы набрали {user_data[message.chat.id]['ball']} баллов из 10')


@bot.message_handler()
def messtime(message):
    bot.register_next_step_handler(message, result)


@bot.callback_query_handler(func=lambda call: call.data == 'Сначала')
def choice(call):

    #if call.data == 'Сначала':
    bot.send_message(call.message.chat.id, 'Вы начали сначала!')
    start(call.message)
    bot.delete_message(call.message.chat.id, call.message.message_id)

@bot.callback_query_handler(func=lambda call: call.data == 'Следующий номер' or call.data == 'Предыдущий номер')
def choice2(call):
    global cnt
    if call.data == 'Следующий номер':
        bot.send_message(call.message.chat.id, 'Вы перешли на следующий номер!')
        user_data[call.message.chat.id]['cnt'] += 1
        new(call.message)
    if call.data == 'Предыдущий номер':
        bot.send_message(call.message.chat.id, 'Вы перешли на предыдущий номер!')
        user_data[call.message.chat.id]['cnt'] -= 1
        new(call.message)
    bot.delete_message(call.message.chat.id, call.message.message_id)
@bot.callback_query_handler(func=lambda callback: callback.data == 'Вариант 1')
def varianty(callback):
    #if callback.data == 'Вариант 1':
    bot.send_message(callback.message.chat.id, 'Вы зашли в первый вариант!')
    new(callback.message)
    bot.delete_message(callback.message.chat.id, callback.message.message_id)


bot.polling(none_stop=True)