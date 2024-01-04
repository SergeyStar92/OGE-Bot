import telebot
from telebot import types
import datetime
import os
import random

bot = telebot.TeleBot('TOKEN')
user_data = {}
user_data.update({'cnt': 0, 'ball': 0, 'var': 0, 'nach': 0,
                  'kon': 0, 'dtime': 0, 'ndtime': 0, 'kdtime': 0,
                  'psticker': [], 'nsticker': [], 'hsticker': [],
                  'hesticker': [], 'dhsticker': []})
mark = False
markup = None
startmark = False


try:
    @bot.message_handler(commands=['statistic'])
    def statistic(message):
        allfile = os.listdir('./')
        for i in allfile:
            if '.txt' in i:
                bot.send_document(message.chat.id, open(f'{i}', 'rb'))

    @bot.message_handler(commands=['start', 'play', 'go'])
    def start(message):
        global mark
        global markup
        global startmark
        try:
            user_data.update({message.chat.id: {'cnt': 0, 'ball': 0, 'var': 0, 'nach': 0,
                                                'kon': 0, 'dtime': 0, 'ndtime': 0, 'kdtime': 0,
                                                'psticker': [], 'nsticker': [], 'hsticker': [],
                                                'hesticker': [], 'dhsticker': []}})
            user_data[message.chat.id]['cnt'] = 0
            user_data[message.chat.id]['ball'] = 0
            user_data[message.chat.id]['dtime'] = datetime.datetime.now()
            user_data[message.chat.id]['psticker'] = [
                'CAACAgIAAxkBAAECHpxlYAZ8m4BC1mQpnCYIXpOHcmRyLwACcxcAAuTR2Emu3qN9K1YIqjME',
                'CAACAgIAAxkBAAECIZplYWgXtu8hU-N6Acro5KTEmd2ydQAC_gADVp29CtoEYTAu-df_MwQ',
                'CAACAgIAAxkBAAECIZxlYWgpEwZKWuP9-ZNFt5S1E9sc1AAC9wADVp29CgtyJB1I9A0wMwQ',
                'CAACAgIAAxkBAAECIZ5lYWhYrVog7pPhhzaSPZOG3L8UbwACRgADUomRI_j-5eQK1QodMwQ',
                'CAACAgIAAxkBAAECIaBlYWmk5mlzhmXEZvYcrbU0aQEbAQACQQADUomRI9XWV0rTZHFWMwQ',
                'CAACAgIAAxkBAAECIaRlYWnVr4AB70ycCVdMdJp1vlM0hgACXAADUomRI1aEI4rcKZp0MwQ',
                'CAACAgIAAxkBAAECIaZlYWn6jS_XCdSP7S_8DrhXMC7kkgACXwADUomRI014vAzAfPkqMwQ',
                'CAACAgIAAxkBAAECIahlYWoknlGVoX9v2Gh4lIJSeUM1sQACGwkAAhhC7gjcuaXV80quyDME',
                'CAACAgIAAxkBAAECIaxlYWqlV7y3p8NKoQu_vqQV4chqQwACNg8AAh4J8UlSVZzp6JZtezME',
                'CAACAgIAAxkBAAECIa5lYWqyd6V2C82pjT1hsruWRiQ_JgACJgwAAnhJeUowATipj2RUwjME',
                'CAACAgIAAxkBAAECIa5lYWqyd6V2C82pjT1hsruWRiQ_JgACJgwAAnhJeUowATipj2RUwjME',
                'CAACAgIAAxkBAAECIeplYXYxCx1aOqd4rR1f8qr7HQl_pAACkQEAAiteUwvdpgv5KiBOTzME',
                'CAACAgIAAxkBAAECIexlYXZOvSO4twjfy6AqF_ESr-pqogAChwEAAiteUwt4J9ZNhn9pYDME',
                'CAACAgIAAxkBAAECIe5lYXZtSGLhsyLIWS2k6TJzDLVeKQACjwEAAiteUwtSWZbMUSUiwjME',
                'CAACAgIAAxkBAAECIf5lYYwfR-awqQZMkJ40dgABNySAxVgAAlsAA05c0ilHqb4HXQwCDDME',
                'CAACAgIAAxkBAAECIgJlYYx_izLTAtV0nzUwIQ9j1cGmngACIAADlp-MDqz9QTP0qm_5MwQ',
                'CAACAgIAAxkBAAECIgZlYYya8Rn4z8vnSdyzXNO-4YhOIwACMwADlp-MDuc2aeJh7C3XMwQ',
                'CAACAgIAAxkBAAECIghlYYyksGTacyad2566hsvhk6zNPQACXgADlp-MDvzxYKa5x71oMwQ',
                'CAACAgIAAxkBAAECIgplYYy8nNscRIM8RAlbYOF2uh0vRgACawADlp-MDjLiqoj24Z4lMwQ',
                'CAACAgEAAxkBAAECIgxlYYzcr68706e2_s5RGuPlTyTHbAACEAEAAjgOghH-1L_EjUKlzDME',
                'CAACAgEAAxkBAAECIg5lYYzhm5rqlrSuffUYIYJt5B5eTQAC_wADOA6CEct71ndrpd51MwQ',
                'CAACAgIAAxkBAAECIhBlYY0I83kcbKDcv-JHxqcR7vKwpgACRAMAArVx2gYMtzsTtIZDMDME',
                'CAACAgIAAxkBAAECIhJlYY0119tgTbFLx4tXVTIyxfMv5QACuAkAAs0hOEupTsJmAAHi-SwzBA',
                'CAACAgIAAxkBAAECIhRlYY1BhIvF2G-DcM97G3Ql3iK46wACxg4AAvnaKEsBVdAP-H2DVjME',
                'CAACAgIAAxkBAAECIhhlYY1cX3-2KSkXTsKKNsOah4fUAgAC_QsAAjgW6EtuJ6lmKggbJDME',
                'CAACAgIAAxkBAAECIhplYY1lad4emdrA3PGxTboT0aqo7gACChAAAgRGEUiotv9tJ3dOTzME',
                'CAACAgIAAxkBAAECIhxlYY11SAXlcJZx7aKIO9XDOv_KCgACkAoAAoCwQEin5TI0NecH7zME']

            user_data[message.chat.id]['nsticker'] = [
                'CAACAgIAAxkBAAECJnplY0BfFK7K0I5RWzEbKkqTXRpiSwACuQ4AAmxu8Emp2F_Xn3emBjME',
                'CAACAgIAAxkBAAECJnxlY0Bqr3F-rEFpfdFUOUyr3hwwrAACXwADTlzSKXaSHy8QpwgkMwQ',
                'CAACAgIAAxkBAAECJn5lY0B1IZUawoNhRd01SDnX9PShkwACRAADUomRI3hic0tMxIRXMwQ',
                'CAACAgIAAxkBAAECJoBlY0B9xrjSDQvSC_OovuM5slZUjQACRwMAAm2wQgNSVSv5NcWAgjME',
                'CAACAgIAAxkBAAECJoJlY0CRKLVyCPHKtcV7iBr5-SieoAACrwADwZxgDNPvAhjBQx5TMwQ',
                'CAACAgIAAxkBAAECJoRlY0CgjEGDRBT4amFm0Tvg1pgorQACDwwAAuKOOUotFzfMTUK3UDME',
                'CAACAgIAAxkBAAECJoZlY0DBYZez3OhQBHmDU6JNOcIyLwAC8wAD9wLID4Z5pOaW8BMuMwQ',
                'CAACAgIAAxkBAAECJohlY0DMBEUL6nf_pECf0Mov8_CH4wACOQ8AAnayKUr6_EzRpTCdWjME',
                'CAACAgEAAxkBAAECJoplY0EIuykp-jD_PyylfDmz6CvRawAC8gEAAjgOghFkeRhU3RO6BjME',
                'CAACAgIAAxkBAAECJoxlY0EZOzFnrv5YS43FQVnVhSlwtQACAQADr8ZRGhLj3-N0EyK_MwQ',
                'CAACAgIAAxkBAAECJo5lY0ErLG321WpVnZM9S4LPOLlGsAACfQAD9wLIDy7JuwrdyyJJMwQ',
                'CAACAgIAAxkBAAECJpJlY0E_t-BMEF2d6MmZc4GaS8rUXwACTgADr8ZRGvFh67KaK5_kMwQ']

            user_data[message.chat.id]['hsticker'] = [
                'CAACAgIAAxkBAAECJkBlYzdPBJ_wkpoRg-v346JbQ6uBkQACZwADlp-MDskGZ8xB2w1PMwQ',
                'CAACAgIAAxkBAAECKsZlZJxF0re5OoBlei5rmSRIPb2jbwACsQ0AAjppOUjINKv7N0gdWjME',
                'CAACAgIAAxkBAAECJkRlYzhDndkAAQwBh4m2dirBtKc5iv4AAgEBAAJWnb0KIr6fDrjC5jQzBA',
                'CAACAgIAAxkBAAECJkZlYzhQ9VQ5hfYpqIniF_j9SLPiBQACdAwAAra7OEuOzqfMQMSAJTME',
                'CAACAgIAAxkBAAECJkhlYzkSZ-gWkWrzhjSYSa6yPSIIsAACrwsAAv1pgUph8CTBF6FPxDME',
                'CAACAgIAAxkBAAECJkplYzkXXSFyBT-b9NkDqmeo31E6TQACRQMAArVx2gaTiBAcidwNGzME',
                'CAACAgIAAxkBAAECJkxlYzkm5KIn5kRbw5XBsu2WwtWrNgACWxkAApITQEg3UQr5oSE8nzME',
                'CAACAgIAAxkBAAECJk5lYzkyOoar7KH2jkRIKS1WpFT8MgACYyYAAhdAsUqFbO_0U5e9pjME',
                'CAACAgIAAxkBAAECJlZlYznpe4RxxDUaDD0QEoAYsVQ3DgACaTEAAnzk-UpTbk5qf7hyeDME',
                'CAACAgIAAxkBAAECJlhlYzn3ASSR3cwu33ncTTNK00DuhgACjgADFkJrCr6khn1tfi1cMwQ',
                'CAACAgIAAxkBAAECJlplYzof92GfGlTQ4R22l2p612Lx4gACoAADlp-MDmce7YYzVgABVTME',
                'CAACAgIAAxkBAAECJlxlYzsxRbh3FieiGcRsGgdLio3WwgACLgADJHFiGojoNkNqQEMUMwQ',
                'CAACAgIAAxkBAAECJl5lYzs6nOBAuAhFBXOyJZp0guqpNAACIAADWbv8JYWKlpoITcl9MwQ',
                'CAACAgIAAxkBAAECJmBlYztKy0aI50uH63FqSvHdN5mTlwACSgADWbv8JZ3yyYHsNyFgMwQ',
                'CAACAgIAAxkBAAECJmhlYzxrlQMVqWIyNvKIG8MPMVAo-AACbwADwZxgDMsOfYvA3U1WMwQ',
                'CAACAgIAAxkBAAECJmplYzyhmUtfkJNqp_N6f5r05sF50wACIQADrWW8FDqjnb_bXuNIMwQ',
                'CAACAgIAAxkBAAECJmxlYzzMWxo0BISA5mXcYoFIDGej_wAClwADO2AkFLPjVSHrbN7ZMwQ',
                'CAACAgIAAxkBAAECJmZlYzxZcWNYSltu6-zQJESYeOSPngAC9wEAAhZCawo59nBvtGN_xDME']

            user_data[message.chat.id]['hesticker'] = [
                'CAACAgIAAxkBAAECKshlZJzCBdl0dG_J_PJplTaGWtuz6QACAQwAArbpmEtKWijuVpAoPjME',
                'CAACAgIAAxkBAAECKsxlZJzL4fX35inwot-zVXhNUuGTXgACNwADlp-MDjXGAq7f-3ZJMwQ',
                'CAACAgIAAxkBAAECKs5lZJzUh5uxLBKq0NSBUJBsk69MIwACYwADTlzSKUXAcwl55a_wMwQ',
                'CAACAgIAAxkBAAECKtBlZJzfz9B5iK_7XBBular9caYMlAACQAADUomRIzVcuj961kKJMwQ',
                'CAACAgIAAxkBAAECKtJlZJz1LcSDP9QdaFPopbk7RVlcYAACHwADlp-MDldYXcQNhO6MMwQ',
                'CAACAgIAAxkBAAECKtRlZJz_eYOKL7vA9FITppakWe-7nAACiQADFkJrCkbL2losgrCOMwQ',
                'CAACAgIAAxkBAAECKtZlZJ0QiL57MnuUcNUCZWO69ijZvgACdywAAk3SKUuG1xCiZQOjwDME',
                'CAACAgIAAxkBAAECKthlZJ0darU1JKBWa7DrF-VRvxRULwACYhQAAoxzQUmp5bwL8cqPBjME',
                'CAACAgIAAxkBAAECKtplZJ002TVHEUJ7DOcX3yj1MZ7ATwACdwUAAj-VzApljNMsSkHZTjME',
                'CAACAgIAAxkBAAECKt5lZJ1W6l603LPV3mX0eGR2wMDqogACTQADWbv8JSiBoG3dG4L3MwQ',
                'CAACAgIAAxkBAAECKuBlZJ1yo6t88SkXFVAauKElnaLHBAACKQADJHFiGiKockiM5SMwMwQ',
                'CAACAgIAAxkBAAECKuJlZJ2Kd_Q8AXqRxZbJ1qU5YwcKNQACpwADO2AkFO1Zfh42qVroMwQ',
                'CAACAgIAAxkBAAECKuRlZJ2vWX5j2AKNUEbWNfGvv7VgAwAChQADwZxgDIuMHR9IU10iMwQ',
                'CAACAgIAAxkBAAECKuZlZJ3MJa73Web7W_0J18cj_1b1vgAClAAD9wLID6LmvuevDazoMwQ',
                'CAACAgIAAxkBAAECKuhlZJ3-5oPH9XIRND75vEZxvIGrsQACHQADr8ZRGlyO-uEKz2-8MwQ']

            user_data[message.chat.id]['dhsticker'] = [
                'CAACAgIAAxkBAAECKvJlZKBTNORbIr7R-TsiTThTw3558gAChQEAAiteUwuroLLCvfR5lzME',
                'CAACAgIAAxkBAAECKvRlZKBfGSdVqs_pTIl7JnHHULX-OQAC_gsAAvPRaUsLGXjsxSxNoDME',
                'CAACAgIAAxkBAAECKvZlZKBppa2cwoddp_1FYy9hnchO7gACnSkAAqbg-UomiGvhgZp_ZjME',
                'CAACAgIAAxkBAAECKvhlZKB1hEURAuUvEp_suX54zJZpsQACWQADUomRI5_hf3uttGWoMwQ',
                'CAACAgIAAxkBAAECKvplZKCDRHnBj5mt2_RDpQ8IGCyryQACLAADlp-MDlsHuP9kDfaFMwQ',
                'CAACAgIAAxkBAAECKvxlZKCb37U6sXwgnW7Pu_Vmy0balQACggMAAm2wQgNtUbWjKH5iFzME',
                'CAACAgIAAxkBAAECKv5lZKCsQVH6qLHwCV0LV2xC8PXoTwACxw8AAhat2Ul-GYhU8r2drjME',
                'CAACAgIAAxkBAAECKwABZWSg0f3v6p4-4z_l3ow9uG23QKsAAkwPAAKxP5lLTEsaEuvBykozBA',
                'CAACAgIAAxkBAAECKwJlZKDfORuMRF395gybZxMmm0hNGgACOBkAArwaWErdwJPJDGh06zME',
                'CAACAgIAAxkBAAECKwRlZKD-tNQsZzu16AqEspl7AAH1FHIAAqoAA1KJkSPxEMMDHZA87zME',
                'CAACAgIAAxkBAAECKwZlZKESwayeMb3unOcI3Z8M83Zz6QAC3QAD5KDOB2yVwjLQclMoMwQ',
                'CAACAgIAAxkBAAECKwhlZKEhYQ7Xq297jXap6Zk8V8eunwACdQADwZxgDDA1Zd15EjDEMwQ',
                'CAACAgIAAxkBAAECKwhlZKEhYQ7Xq297jXap6Zk8V8eunwACdQADwZxgDDA1Zd15EjDEMwQ',
                'CAACAgIAAxkBAAECKwxlZKFKz2TzWNrNfB1AH_Ca-qvfrQACNgADWbv8JSW6dSLrfJB1MwQ',
                'CAACAgIAAxkBAAECKw5lZKGQCzinDaG9uJz56A1sGHkICgACLwADwZxgDK-MRHjuZdGKMwQ']

            bot.send_sticker(message.chat.id, random.choice(user_data[message.chat.id]['hsticker']))#
            bot.send_message(message.chat.id, f'Привет {message.chat.first_name} {message.chat.last_name}, '
                                              f'ты находишся в чат-боте ОГЭ информатика! Дата: {user_data[message.chat.id]['dtime'].date()}, '
                                              f'время: {user_data[message.chat.id]['dtime'].strftime("%H:%M:%S")}')

            markup = types.InlineKeyboardMarkup()
            var1 = types.InlineKeyboardButton(f'1', callback_data='Вариант 1')
            var2 = types.InlineKeyboardButton(f'2', callback_data='Вариант 2')
            var3 = types.InlineKeyboardButton(f'3', callback_data='Вариант 3')
            var4 = types.InlineKeyboardButton(f'4', callback_data='Вариант 4')
            var5 = types.InlineKeyboardButton(f'5', callback_data='Вариант 5')
            var6 = types.InlineKeyboardButton(f'6', callback_data='Вариант 6')
            var7 = types.InlineKeyboardButton(f'7', callback_data='Вариант 7')
            var8 = types.InlineKeyboardButton(f'8', callback_data='Вариант 8')
            var9 = types.InlineKeyboardButton(f'9', callback_data='Вариант 9')
            var10 = types.InlineKeyboardButton(f'10', callback_data='Вариант 10')
            markup.row(var1, var2, var3, var4, var5)
            markup.row(var6, var7, var8, var9, var10)
            print('Первый раз выбрать!')
            bot.send_message(message.chat.id, f'Выбери вариант!', reply_markup=markup)
        except KeyError:
            print('Отработала ошибка KeyError 0')
            bot.send_message(message.chat.id, f'Выберите вариант!', reply_markup=markup)
            bot.delete_message(message.chat.id, message.message_id - 1)
        finally:
            mark = True
            startmark = True



    @bot.message_handler()
    def result(message):
        global startmark
        try:
            if message.text.lower() == '/start' or message.text.lower() == '/go' or message.text.lower() == '/play':
                start(message)
            if message.text.lower() == '/statistic':
                statistic(message)
            else:
                if user_data[message.chat.id]['var'] == 1:
                    otvets = ['барс', 'монгол', '32', '10', '6', '4', '7341256', '111', '27', '25']

                elif user_data[message.chat.id]['var'] == 2:
                    otvets = ['баран', 'рапира', '38', '14', '9', '7', '2735146', '89', '16', '51']

                elif user_data[message.chat.id]['var'] == 3:
                    otvets = ['медведь', 'лекало', '17', '13', '7', '3', '1423657', '116', '22', '52']

                elif user_data[message.chat.id]['var'] == 4:
                    otvets = ['корова', 'разрез', '11', '11', '4', '7', '5362471', '15', '20', '39']

                elif user_data[message.chat.id]['var'] == 5:
                    otvets = ['жираф', 'просто', '26', '12', '3', '6', '2736145', '165', '24', '30']

                elif user_data[message.chat.id]['var'] == 6:
                    otvets = ['коза', 'физика', '20', '11', '5', '3', '6473512', '54', '13', '28']

                elif user_data[message.chat.id]['var'] == 7:
                    otvets = ['лис', 'гитара', '50', '15', '4', '5', '3147256', '47', '33', '46']

                elif user_data[message.chat.id]['var'] == 8:
                    otvets = ['бык', 'кавказ', '59', '16', '6', '8', '5362471', '13', '21', '47']

                elif user_data[message.chat.id]['var'] == 9:
                    otvets = ['гепард', 'ворона', '31', '17', '9', '2', '467351582', '11', '28', '51']

                elif user_data[message.chat.id]['var'] == 10:
                    otvets = ['верблюд', 'кружка', '48', '19', '8', '5', '658472713', '3', '48', '61']

                if message.text.lower() == otvets[user_data[message.chat.id]['cnt']]:
                    bot.reply_to(message, f'Правильно!')
                    bot.send_sticker(message.chat.id, random.choice(user_data[message.chat.id]['psticker']))
                    user_data[message.chat.id]['cnt'] += 1
                    user_data[message.chat.id]['ball'] += 1
                    new(message)

                else:
                    bot.reply_to(message, f'Неправильно')
                    bot.send_sticker(message.chat.id, random.choice(user_data[message.chat.id]['nsticker']))
                    markup2 = types.InlineKeyboardMarkup()

                    reset = types.InlineKeyboardButton(f'Выбрать вариант', callback_data="Сначала")
                    next_num = types.InlineKeyboardButton(f'Следующий номер', callback_data="Следующий номер")

                    markup2.row(next_num, reset)

                    bot.send_message(message.chat.id, f'{message.chat.first_name}, отвечайте дальше или выберете один из вариантов ниже!', reply_markup=markup2)
        except IndexError:
            print('Отработала ошибка IndexError')
            if startmark == True:
                pass
            else:
                start(message)
                startmark = False
        except KeyError:
            print('Отработала ошибка KeyError 1')
            if mark == False:
                bot.send_message(message.chat.id, f'Введите команду /start')
            else:
                print('Второй раз выбрать!')
                bot.send_message(message.chat.id, f'Выберите вариант!', reply_markup=markup)
                bot.delete_message(message.chat.id, message.message_id - 1)
        except UnboundLocalError:
            print('Отработала ошибка UnboundLocalError 1')
            # bot.send_message(message.chat.id, f'Выберите вариант!', reply_markup=markup)
            # bot.delete_message(message.chat.id, message.message_id - 1)
        except AttributeError:
            print('Отработала ошибка AttributeError')
            bot.delete_message(message.chat.id, message.message_id)


    @bot.message_handler()
    def new(message):
        global startmark
        try:
            file = open(f"./var{user_data[message.chat.id]['var']}/{user_data[message.chat.id]['cnt']}.png", 'rb')
            bot.send_photo(message.chat.id, file)
            file.close()
            bot.send_message(message.chat.id, f'Введите ответ:')
            messtime(message)

        except FileNotFoundError:
            print('Отработала ошибка FileNotFoundError')
            if user_data[message.chat.id]['ball'] > 4:
                bot.send_sticker(message.chat.id, random.choice(user_data[message.chat.id]['hesticker']))
                bot.send_message(message.chat.id, '🎉🎉🎉Ура вы прошли порог, мы вас поздравляем!!!🎉🎉🎉')
            else:
                bot.send_sticker(message.chat.id, random.choice(user_data[message.chat.id]['dhsticker']))
                bot.send_message(message.chat.id, '😞😞😞Вы не прошли порог, очень жаль, попробуйте снова!!!\n Главное не останавливаться и все получится!!!')
            user_data[message.chat.id]['kdtime'] = datetime.datetime.now()
            timespent = user_data[message.chat.id]['kdtime'] - user_data[message.chat.id]['ndtime']
            bot.send_message(message.chat.id, f"{message.chat.first_name} {message.chat.last_name} вы закончили {user_data[message.chat.id]['dtime'].date()} в {user_data[message.chat.id]['kdtime'].strftime("%H:%M:%S")}, "
                                              f"затрачено времени {int(timespent.total_seconds())//3600}ч. {(int(timespent.total_seconds())//60)%60}м. {int(timespent.total_seconds())%60}с. "
                                              f"вы решали (вариант {user_data[message.chat.id]['var']}) "
                                              f"- задания закончились вы набрали {user_data[message.chat.id]['ball']} баллов из 10")
            user_data[message.chat.id]['kon'] = open(f'{message.chat.first_name}_{message.chat.last_name}.txt', 'a+', encoding="utf-8")
            user_data[message.chat.id]['kon'].write(f"Закончил {user_data[message.chat.id]['dtime'].date()} в {user_data[message.chat.id]['kdtime'].strftime("%H:%M:%S")} "
                                                    f"затрачено времени {int(timespent.total_seconds())//3600}ч. {(int(timespent.total_seconds())//60)%60}м. {int(timespent.total_seconds())%60}с. "
                                                    f"{message.chat.first_name} {message.chat.last_name}, (вариант {user_data[message.chat.id]['var']}) "
                                                    f"- набрал {user_data[message.chat.id]['ball']} баллов из 10\n\n")
            user_data[message.chat.id]['kon'].close()

            markup3 = types.InlineKeyboardMarkup()
            reset = types.InlineKeyboardButton(f'Выбрать вариант', callback_data="Сначала")
            markup3.row(reset)

            bot.send_message(message.chat.id, f'Для продолжения нажмите кнопку 👇', reply_markup=markup3)
        finally:
            startmark = False


    @bot.message_handler()
    def messtime(message):
        bot.register_next_step_handler(message, result)


    @bot.callback_query_handler(func=lambda callback: True)
    def varianty(callback):


        if callback.data == 'Вариант 1':
            user_data[callback.message.chat.id]['ndtime'] = datetime.datetime.now()
            bot.send_message(callback.message.chat.id,f'Время начала {user_data[callback.message.chat.id]['ndtime'].strftime("%H:%M:%S")}')
            bot.send_message(callback.message.chat.id, f'Вы зашли в первый вариант!')
            user_data[callback.message.chat.id]['var'] = 1
            new(callback.message)

            user_data[callback.message.chat.id]['nach'] = open(
                f'{callback.message.chat.first_name}_{callback.message.chat.last_name}.txt', 'a+', encoding="utf-8")
            user_data[callback.message.chat.id]['nach'].write(
                f"Начал {user_data[callback.message.chat.id]['dtime'].date()} в {user_data[callback.message.chat.id]['ndtime'].strftime("%H:%M:%S")} "   
                f"{callback.message.chat.first_name} {callback.message.chat.last_name}, "
                f"(вариант {user_data[callback.message.chat.id]['var']})\n")
            user_data[callback.message.chat.id]['nach'].close()

        elif callback.data == 'Вариант 2':
            user_data[callback.message.chat.id]['ndtime'] = datetime.datetime.now()
            bot.send_message(callback.message.chat.id, f'Время начала {user_data[callback.message.chat.id]['ndtime'].strftime("%H:%M:%S")}')
            bot.send_message(callback.message.chat.id, 'Вы зашли во второй вариант!')
            user_data[callback.message.chat.id]['var'] = 2
            new(callback.message)

            user_data[callback.message.chat.id]['nach'] = open(
                f'{callback.message.chat.first_name}_{callback.message.chat.last_name}.txt', 'a+', encoding="utf-8")
            user_data[callback.message.chat.id]['nach'].write(
                f"Начал {user_data[callback.message.chat.id]['dtime'].date()} в {user_data[callback.message.chat.id]['ndtime'].strftime("%H:%M:%S")} "  # 
                f"{callback.message.chat.first_name} {callback.message.chat.last_name}, "
                f"(вариант {user_data[callback.message.chat.id]['var']})\n")
            user_data[callback.message.chat.id]['nach'].close()

        elif callback.data == 'Вариант 3':
            user_data[callback.message.chat.id]['ndtime'] = datetime.datetime.now()
            bot.send_message(callback.message.chat.id, f'Время начала {user_data[callback.message.chat.id]['ndtime'].strftime("%H:%M:%S")}')
            bot.send_message(callback.message.chat.id, 'Вы зашли в третий вариант!')
            user_data[callback.message.chat.id]['var'] = 3
            new(callback.message)

            user_data[callback.message.chat.id]['nach'] = open(
                f'{callback.message.chat.first_name}_{callback.message.chat.last_name}.txt', 'a+', encoding="utf-8")
            user_data[callback.message.chat.id]['nach'].write(
                f"Начал {user_data[callback.message.chat.id]['dtime'].date()} в {user_data[callback.message.chat.id]['ndtime'].strftime("%H:%M:%S")} "  # 
                f"{callback.message.chat.first_name} {callback.message.chat.last_name}, "
                f"(вариант {user_data[callback.message.chat.id]['var']})\n")
            user_data[callback.message.chat.id]['nach'].close()

        elif callback.data == 'Вариант 4':
            user_data[callback.message.chat.id]['ndtime'] = datetime.datetime.now()
            bot.send_message(callback.message.chat.id, f'Время начала {user_data[callback.message.chat.id]['ndtime'].strftime("%H:%M:%S")}')
            bot.send_message(callback.message.chat.id, 'Вы зашли в четвертый вариант!')
            user_data[callback.message.chat.id]['var'] = 4
            new(callback.message)

            user_data[callback.message.chat.id]['nach'] = open(
                f'{callback.message.chat.first_name}_{callback.message.chat.last_name}.txt', 'a+', encoding="utf-8")
            user_data[callback.message.chat.id]['nach'].write(
                f"Начал {user_data[callback.message.chat.id]['dtime'].date()} в {user_data[callback.message.chat.id]['ndtime'].strftime("%H:%M:%S")} "  # 
                f"{callback.message.chat.first_name} {callback.message.chat.last_name}, "
                f"(вариант {user_data[callback.message.chat.id]['var']})\n")
            user_data[callback.message.chat.id]['nach'].close()

        elif callback.data == 'Вариант 5':
            user_data[callback.message.chat.id]['ndtime'] = datetime.datetime.now()
            bot.send_message(callback.message.chat.id, f'Время начала {user_data[callback.message.chat.id]['ndtime'].strftime("%H:%M:%S")}')
            bot.send_message(callback.message.chat.id, 'Вы зашли в пятый вариант!')
            user_data[callback.message.chat.id]['var'] = 5
            new(callback.message)

            user_data[callback.message.chat.id]['nach'] = open(
                f'{callback.message.chat.first_name}_{callback.message.chat.last_name}.txt', 'a+', encoding="utf-8")
            user_data[callback.message.chat.id]['nach'].write(
                f"Начал {user_data[callback.message.chat.id]['dtime'].date()} в {user_data[callback.message.chat.id]['ndtime'].strftime("%H:%M:%S")} "  # 
                f"{callback.message.chat.first_name} {callback.message.chat.last_name}, "
                f"(вариант {user_data[callback.message.chat.id]['var']})\n")
            user_data[callback.message.chat.id]['nach'].close()

        elif callback.data == 'Вариант 6':
            user_data[callback.message.chat.id]['ndtime'] = datetime.datetime.now()
            bot.send_message(callback.message.chat.id, f'Время начала {user_data[callback.message.chat.id]['ndtime'].strftime("%H:%M:%S")}')
            bot.send_message(callback.message.chat.id, 'Вы зашли в шестой вариант!')
            user_data[callback.message.chat.id]['var'] = 6
            new(callback.message)

            user_data[callback.message.chat.id]['nach'] = open(
                f'{callback.message.chat.first_name}_{callback.message.chat.last_name}.txt', 'a+', encoding="utf-8")
            user_data[callback.message.chat.id]['nach'].write(
                f"Начал {user_data[callback.message.chat.id]['dtime'].date()} в {user_data[callback.message.chat.id]['ndtime'].strftime("%H:%M:%S")} "  # 
                f"{callback.message.chat.first_name} {callback.message.chat.last_name}, "
                f"(вариант {user_data[callback.message.chat.id]['var']})\n")
            user_data[callback.message.chat.id]['nach'].close()

        elif callback.data == 'Вариант 7':
            user_data[callback.message.chat.id]['ndtime'] = datetime.datetime.now()
            bot.send_message(callback.message.chat.id, f'Время начала {user_data[callback.message.chat.id]['ndtime'].strftime("%H:%M:%S")}')
            bot.send_message(callback.message.chat.id, 'Вы зашли в седьмой вариант!')
            user_data[callback.message.chat.id]['var'] = 7
            new(callback.message)

            user_data[callback.message.chat.id]['nach'] = open(
                f'{callback.message.chat.first_name}_{callback.message.chat.last_name}.txt', 'a+', encoding="utf-8")
            user_data[callback.message.chat.id]['nach'].write(
                f"Начал {user_data[callback.message.chat.id]['dtime'].date()} в {user_data[callback.message.chat.id]['ndtime'].strftime("%H:%M:%S")} "  # 
                f"{callback.message.chat.first_name} {callback.message.chat.last_name}, "
                f"(вариант {user_data[callback.message.chat.id]['var']})\n")
            user_data[callback.message.chat.id]['nach'].close()

        elif callback.data == 'Вариант 8':
            user_data[callback.message.chat.id]['ndtime'] = datetime.datetime.now()
            bot.send_message(callback.message.chat.id, f'Время начала {user_data[callback.message.chat.id]['ndtime'].strftime("%H:%M:%S")}')
            bot.send_message(callback.message.chat.id, 'Вы зашли в восьмой вариант!')
            user_data[callback.message.chat.id]['var'] = 8
            new(callback.message)

            user_data[callback.message.chat.id]['nach'] = open(
                f'{callback.message.chat.first_name}_{callback.message.chat.last_name}.txt', 'a+', encoding="utf-8")
            user_data[callback.message.chat.id]['nach'].write(
                f"Начал {user_data[callback.message.chat.id]['dtime'].date()} в {user_data[callback.message.chat.id]['ndtime'].strftime("%H:%M:%S")} "  # 
                f"{callback.message.chat.first_name} {callback.message.chat.last_name}, "
                f"(вариант {user_data[callback.message.chat.id]['var']})\n")
            user_data[callback.message.chat.id]['nach'].close()

        elif callback.data == 'Вариант 9':
            user_data[callback.message.chat.id]['ndtime'] = datetime.datetime.now()
            bot.send_message(callback.message.chat.id, f'Время начала {user_data[callback.message.chat.id]['ndtime'].strftime("%H:%M:%S")}')
            bot.send_message(callback.message.chat.id, 'Вы зашли в девятый вариант!')
            user_data[callback.message.chat.id]['var'] = 9
            new(callback.message)

            user_data[callback.message.chat.id]['nach'] = open(
                f'{callback.message.chat.first_name}_{callback.message.chat.last_name}.txt', 'a+', encoding="utf-8")
            user_data[callback.message.chat.id]['nach'].write(
                f"Начал {user_data[callback.message.chat.id]['dtime'].date()} в {user_data[callback.message.chat.id]['ndtime'].strftime("%H:%M:%S")} "  # 
                f"{callback.message.chat.first_name} {callback.message.chat.last_name}, "
                f"(вариант {user_data[callback.message.chat.id]['var']})\n")
            user_data[callback.message.chat.id]['nach'].close()

        elif callback.data == 'Вариант 10':
            user_data[callback.message.chat.id]['ndtime'] = datetime.datetime.now()
            bot.send_message(callback.message.chat.id, f'Время начала {user_data[callback.message.chat.id]['ndtime'].strftime("%H:%M:%S")}')
            bot.send_message(callback.message.chat.id, 'Вы зашли в десятый вариант!')
            user_data[callback.message.chat.id]['var'] = 10
            new(callback.message)

            user_data[callback.message.chat.id]['nach'] = open(
                f'{callback.message.chat.first_name}_{callback.message.chat.last_name}.txt', 'a+', encoding="utf-8")
            user_data[callback.message.chat.id]['nach'].write(
                f"Начал {user_data[callback.message.chat.id]['dtime'].date()} в {user_data[callback.message.chat.id]['ndtime'].strftime("%H:%M:%S")} "  # 
                f"{callback.message.chat.first_name} {callback.message.chat.last_name}, "
                f"(вариант {user_data[callback.message.chat.id]['var']})\n")
            user_data[callback.message.chat.id]['nach'].close()

        elif callback.data == 'Следующий номер':
            bot.send_message(callback.message.chat.id,f'{callback.message.chat.first_name}, вы перешли на следующий номер!')
            user_data[callback.message.chat.id]['cnt'] += 1
            new(callback.message)

        elif callback.data == 'Сначала':
            bot.send_message(callback.message.chat.id, f'Вот это да, вы начали сначала!')
            start(callback.message)


        bot.delete_message(callback.message.chat.id, callback.message.message_id)

except UnboundLocalError:
    @bot.message_handler()
    def err(message):
        print('Отработала ошибка UnboundLocalError 2')
        bot.send_message(message.chat.id, f'Введите команду /start')

except KeyError:
    @bot.message_handler()
    def err2(message):
        print('Отработала ошибка KeyError 2')
        bot.send_message(message.chat.id, f'Введите команду /start')


bot.polling(none_stop=True)