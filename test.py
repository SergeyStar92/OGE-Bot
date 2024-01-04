# @bot.callback_query_handler(func=lambda callback: True)
# def choice(callback):
#     global cnt
#     if callback.data == 'Сначала':
#         bot.send_message(callback.message.chat.id, 'Вы начали сначала!')
#         start(callback.message)
#
#     if callback.data == 'Следующий номер':
#         bot.send_message(callback.message.chat.id, 'Вы перешли на следующий номер!')
#         cnt += 1
#         new(callback.message)

#name = None
# @bot.message_handler(commands=['start'])
# def start(message):
#     conn = sqlite3.connect('bd.sql')
#     cur = conn.cursor()
#
#     cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
#     conn.commit()
#     cur.close()
#     conn.close()
#     bot.send_message(message.chat.id, 'Привет, сейчас я тебя зарегистрирую! Введи свое имя ')
#     bot.register_next_step_handler(message, user_name)
#
# def user_name(message):
#     global name
#     name = message.text.strip()
#     bot.send_message(message.chat.id, 'Введите пароль')
#     bot.register_next_step_handler(message, user_pass)
#
# def user_pass(message):
#     password = message.text.strip()
#     conn = sqlite3.connect('bd.sql')
#     cur = conn.cursor()
#
#     cur.execute(f"INSERT INTO users (name, pass) VALUES ('%s', '%s')" % (name, password))
#     conn.commit()
#     cur.close()
#     conn.close()
#
#     markup = telebot.types.InlineKeyboardMarkup()
#     markup.add(telebot.types.InlineKeyboardButton('Список пользователей:', callback_data='users'))
#     bot.send_message(message.chat.id, 'Пользователь зарегистрирован!', reply_markup=markup)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     conn = sqlite3.connect('bd.sql')
#     cur = conn.cursor()
#
#     cur.execute(f"SELECT * FROM users")
#     users = cur.fetchall()
#     info = ''
#     for el in users:
#         info += f'Имя: {el[1]}, пароль: {el[2]}\n'
#     cur.close()
#     conn.close()
#     bot.send_message(call.message.chat.id, info)

# @bot.message_handler(commands=['site', 'website'])
# def site(message):
#     webbrowser.open('https://ori4life.ru')
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup()
#     btn1 = types.KeyboardButton('Перейти на сайт')
#     markup.row(btn1)
#     btn2 = types.KeyboardButton(f'Удалить фото')
#     btn3 = types.KeyboardButton(f'Изменить текст')
#     markup.row(btn2, btn3)
#     bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
#
#
# @bot.message_handler(content_types=['photo'])
# def photo(message):
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton('Перейти на сайт', url='http://vk.com')
#     markup.row(btn1)
#     btn2 = types.InlineKeyboardButton(f'Удалить фото', callback_data='delete')
#
#     btn3 = types.InlineKeyboardButton(f'Изменить текст', callback_data='edit')
#     markup.row(btn2, btn3)
#
#     bot.reply_to(message, f'Какое красивое фото', reply_markup=markup)
#
# @bot.callback_query_handler(func=lambda callback: True)
# def callback_msg(callback):
#     if callback.data == 'delete':
#         bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
#     elif callback.data == 'edit':
#         bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)
# @bot.message_handler(commands=['converter'])
# def conv(message):
#     bot.send_message(message.chat.id, f'Вы зашли в конвертер!')
#
#
# @bot.message_handler(commands=['start', 'main', 'hello'])
# def main(message):
#     bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
#
# @bot.message_handler(commands=['help'])
# def main(message):
#     bot.send_message(message.chat.id, 'Помощь')
#
# @bot.message_handler()
# def info(message):
#     if message.text.lower() == 'привет':
#         print('зашли сюда')
#         bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
#
#     elif message.text.lower() == 'id':
#         bot.reply_to(message, f'ID: {message.from_user.id}')
#         print('зашли вот сюда')
# import datetime
# g = 0
# a = datetime.datetime.now()
# print(a)
# c = input()
# b = datetime.datetime.now()
# print(b)
# c = input()
# f = datetime.datetime.now()
# print(f - b)

# import telebot
# from telebot import types
# from time import sleep
#
# bot = telebot.TeleBot('6410141456:AAHPadR2RJZ-i56xmWTpPQ_dSZ9iK58ZTk8')
# user_data = {}
# user_data.update({'cnt': 0, 'ball': 0, 'var': 0})
# markup = None
# mark = False
# mark_btn = False
# @bot.message_handler(commands=['start', 'play', 'go'])
# def start(message):
#     global markup
#     global mark
#     try:
#         user_data.update({message.chat.id: {'cnt': 0, 'ball': 0}})
#         user_data[message.chat.id]['cnt'] = 0
#         user_data[message.chat.id]['ball'] = 0
#         bot.send_message(message.chat.id, 'Привет вы находитесь в чат боте ОГЭ информатика! ')
#         markup = types.InlineKeyboardMarkup()
#         var1 = types.InlineKeyboardButton(f'Вариант 1', callback_data='Вариант 1')
#         var2 = types.InlineKeyboardButton(f'Вариант 2', callback_data='Вариант 2')
#         var3 = types.InlineKeyboardButton(f'Вариант 3', callback_data='Вариант 3')
#         markup.row(var1, var2, var3)
#         bot.send_message(message.chat.id, f'Выберете вариант!', reply_markup=markup)
#     except KeyError:
#         bot.send_message(message.chat.id, f'Выберете вариант!', reply_markup=markup)
#         bot.delete_message(message.chat.id, message.message_id - 1)
#     finally:
#         mark = True
#
# @bot.message_handler()
# def result(message):
#     try:
#         if message.text.lower() == '/start':
#             start(message)
#         if message.text.lower() == '/go':
#             start(message)
#         else:
#             if user_data[message.chat.id]['var'] == 1:
#                 otvets = ['барс', 'монгол', '32', '10', '6', '4', '7341256', '111', '27', '25']
#
#             elif user_data[message.chat.id]['var'] == 2:
#                 otvets = ['баран', 'рапира', '38', '14', '9', '7', '2735146', '89', '16', '51']
#
#             elif user_data[message.chat.id]['var'] == 3:
#                 otvets = ['медведь', 'лекало', '17', '13', '7', '3', '1423657', '116', '22', '52']
#
#             if message.text.lower() == otvets[user_data[message.chat.id]['cnt']]:
#                 bot.reply_to(message, f'Правильно!')
#                 user_data[message.chat.id]['cnt'] += 1
#                 user_data[message.chat.id]['ball'] += 1
#                 new(message)
#             else:
#                 bot.reply_to(message, f'Неправильно')
#                 markup2 = types.InlineKeyboardMarkup()
#                 reset = types.InlineKeyboardButton(f'Выбрать вариант', callback_data="Сначала")
#                 next_num = types.InlineKeyboardButton(f'Следующий номер', callback_data="Следующий номер")
#                 markup2.row(next_num, reset)
#
#                 bot.send_message(message.chat.id, f'Пробуйте отвечать дальше или выберете один из вариантов ниже!', reply_markup=markup2)
#     except IndexError:
#         start(message)
#     except KeyError:
#         if mark == False:
#             bot.send_message(message.chat.id, f'Введите команду /start')
#         else:
#             print(f'Зашли зашли {mark}')
#             bot.send_message(message.chat.id, f'Выберете вариант!', reply_markup=markup)
#             bot.delete_message(message.chat.id, message.message_id - 1)
#
# @bot.message_handler()
# def new(message):
#     try:
#         file = open(f"./var{user_data[message.chat.id]['var']}/{user_data[message.chat.id]['cnt']}.png", 'rb')
#         bot.send_photo(message.chat.id, file)
#         messtime(message)
#
#     except FileNotFoundError:
#         print('Файлы кончились')
#         bot.send_message(message.chat.id, f"Задания закончились вы набрали {user_data[message.chat.id]['ball']} баллов из 10")
#
#
# @bot.message_handler()
# def messtime(message):
#     bot.register_next_step_handler(message, result)
#
#
# @bot.callback_query_handler(func=lambda callback: True)
# def varianty(callback):
#
#     if callback.data == 'Вариант 1':
#         bot.send_message(callback.message.chat.id, 'Вы зашли в первый вариант!')
#         user_data[callback.message.chat.id]['var'] = 1
#         new(callback.message)
#
#     elif callback.data == 'Вариант 2':
#         bot.send_message(callback.message.chat.id, 'Вы зашли во второй вариант!')
#         user_data[callback.message.chat.id]['var'] = 2
#         new(callback.message)
#
#     elif callback.data == 'Вариант 3':
#         bot.send_message(callback.message.chat.id, 'Вы зашли в третий вариант!')
#         user_data[callback.message.chat.id]['var'] = 3
#         new(callback.message)
#
#     elif callback.data == 'Следующий номер':
#         bot.send_message(callback.message.chat.id, 'Вы перешли на следующий номер!')
#         user_data[callback.message.chat.id]['cnt'] += 1
#         new(callback.message)
#
#     elif callback.data == 'Сначала':
#         bot.send_message(callback.message.chat.id, 'Вы начали сначала!')
#         start(callback.message)
#
#     bot.delete_message(callback.message.chat.id, callback.message.message_id)
#
# bot.polling(none_stop=True)

# while True:
#     try:
#         bot.polling(none_stop=True)
#     except Exception as _ex:
#         print(_ex)
#         sleep(1)


def test(a, b):
    c = []
    for i in range(a, b):
        c.append(i)

    return c


print(test(15, 19))


e = lambda x: x + 56
print(e(54))