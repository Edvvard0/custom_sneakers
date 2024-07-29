# -*- coding: utf-8 -*-

from telebot import types, TeleBot

from sklad import comment_list, photo_list,photo_models,ready_models,ord_list_photo

import sqlite3

bot = TeleBot("6312416281:AAFS1wIUyW4Ld9sy2-UenuXnumUES_kgiww")
user_data = {} #?????

vopr = ('Какой у вас размер обуви?','На каких кросовках Вы хотике сделать кастом?','Введите ваш адресс','Оставте комментарий к кастому','Номер вашего кастома?', 'Ваш номер телефона?')

count = 0

list_commands = '''Бот может:
/menu  -  меню
/info - информация о компании
/comments - отзывы
/models - готовые модели 
/individual_castom - индивидуальный заказ
/care - уход за обувью
/order - заказ
/make an order - сделать заказ'''

start = f'''Вас приветствует команда Castom night.
Мы занимаемся кастомом кросовок.
В этом боте вы можете сделать предзаказ.
По всем вопросам вы можете обратиться по номеру телефона 
+7 978 00 00 000

{list_commands}
'''



infoo = '''Мы молодая компания , которая только начинает свою деятельность в маленьком городе.
Наша цель заслужить ваше доверие путём качественной работы и ответственного отношения к каждому клиенту.
Мы стремимся к постоянному совершенствованию и развитию, чтобы обеспечить нашим клиентам только лучший сервис и продукцию.'''

individual_castom  = '''Индивидуальные заказы согласуются с менеджером
тг: @Edward0076
номер телефона +7 978 00 00 000 '''

clear = '''Уход!!!!'''

otv =[]
s = 0 #??????????

name = '''Для того чтобы сделать заказ заполнити следующие поля:
/size - размер обуви
/mod - модель кросовок
/adress - ваш адресс
/com - комментарий к заказу
/number_castom - номер кастома'''


@bot.message_handler(commands=['start'])
def start(messege):
    bot.send_message(messege.chat.id, start)


@bot.message_handler(commands=['menu'])
def menu(messege):
    bot.send_message(messege.chat.id, list_commands)

@bot.message_handler(commands=['info'])
def menu(messege):
    bot.send_message(messege.chat.id, infoo)

@bot.message_handler(commands=['care'])
def start(messege):
    bot.send_message(messege.chat.id, clear)

@bot.message_handler(commands=['ddd'])
def start(messege):
    bot.send_message(messege.chat.id,messege.from_user.username)


i = 0 #?????
o = 0
@bot.message_handler(commands=['individual_castom'])
def comments(message):
    bot.send_message(message.chat.id, individual_castom)

# Это работа с бд её надо либо удалить либо вынести в отдельный бот

# @bot.message_handler(commands=['all_user_ord'])
# def get_h(message):
#     # if len(user_data)!=0:
#         bot.send_message(message.chat.id, 'Hello')
#         conn = sqlite3.connect('user_all_order.sql')
#         cur = conn.cursor()
#
#         cur.execute(
#             'SELECT * FROM users')
#         client = cur.fetchall()
#         chel = ''
#         for el in client:
#             chel += f'name: {el[1]} ,\n siz: {el[2]} ,\n model: {el[3]} ,\n adress: {el[4]} ,\n comment: {el[5]} ,\n num: {el[6]}\n\n'
#
#         cur.close()
#         conn.close()
#         bot.send_message(message.chat.id, chel)
#     # else:
#     #     bot.send_message(message.chat.id, "Заказов нет")
# @bot.message_handler(commands=['all_clear'])
# def get_h(message):
#     conn = sqlite3.connect('user_all_order.sql')
#
#     cursor = conn.cursor()
#
#     # SQL-запрос для удаления всех таблиц
#     sql = "SELECT name FROM sqlite_master WHERE type='table';"
#     cursor.execute(sql)
#     tables = cursor.fetchall()
#
#     for table in tables:
#         cursor.execute(f"DROP TABLE {table[0]};")
#
#     # Подтверждение изменений и закрытие соединения
#     conn.commit()
#     conn.close()
#
#     print("База данных была очищена")

@bot.message_handler(commands=['models'])
def comments(message):
    o = 0

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Next2")
    markup.add(item1)

    phot = open(photo_models[0], 'rb')
    bot.send_photo(message.chat.id, phot)
    bot.send_message(message.chat.id, ready_models[o], reply_markup=markup)
    bot.register_next_step_handler(message, get_next2)

def get_next2(message):
        dd = message.text
        global o
        if dd == 'Next2':
            o+=1
            print()
        if ready_models[o] == 'модели закончились':
            bot.send_message(message.chat.id, 'модели закончились', reply_markup=types.ReplyKeyboardRemove())
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Next2")
            markup.add(item1)
            phot = open(photo_models[o], 'rb')
            bot.send_photo(message.chat.id, phot)
            bot.send_message(message.chat.id, ready_models[o], reply_markup=markup)
            bot.register_next_step_handler(message, get_next2)
        return o


j = 0
@bot.message_handler(commands=['comments'])
def comments(message):
    j = 0

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Next")
    markup.add(item1)
    phot = open(photo_list[0], 'rb')
    bot.send_photo(message.chat.id, phot)
    bot.send_message(message.chat.id, comment_list[j], reply_markup=markup)
    bot.register_next_step_handler(message, get_next)

def get_next(message):
        dd = message.text
        global j
        if dd == 'Next':
            j+=1

        if comment_list[j] == 'примеры закончились':
            bot.send_message(message.chat.id, 'примеры закончились', reply_markup=types.ReplyKeyboardRemove())
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Next")
            markup.add(item1)
            phot = open(photo_list[j], 'rb')
            bot.send_photo(message.chat.id, phot)
            bot.send_message(message.chat.id, comment_list[j], reply_markup=markup)
            bot.register_next_step_handler(message, get_next)
        return j


@bot.message_handler(commands=['order'])
def show_profile(message):
    if len(user_data)!=0:
        bot.send_message(message.chat.id, 'Ваш заказ:')
        us_d = user_data['num']
        nn = ord_list_photo[us_d]

        photo = open(nn, 'rb')
        bot.send_photo(message.chat.id, photo)
        profile = f"Размер: {user_data['size']}\nМодель кросовок: {user_data['model']}\nАдресс: {user_data['adress']}\nКоментарий: {user_data['comment']}\nНомер кастома: {user_data['num']}"
        bot.send_message(message.chat.id, profile, reply_markup=types.ReplyKeyboardRemove())
        # bot.send_message(message.chat.id, 'заказ закончен', reply_markup=types.ReplyKeyboardRemove())

    else:
        bot.send_message(message.chat.id,'Нет заказа')

ttt = 0





@bot.message_handler(commands=['make an order'])
def start_message(message):
    body = '{message}\n' \
           '--\n' \
           '{first}, {last}\n' \
           '{username}, {id}'.format(message=message.text, first=message.from_user.first_name,
                                     last=message.from_user.last_name, username=message.from_user.username,
                                     id=message.chat.id)
    user_data['name'] = body

    conn = sqlite3.connect('user_all_order.sql')
    cur = conn.cursor()


    cur.execute(
        'CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), size varchar(10), model varchar(50), address varchar(50), comment varchar(50), num varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, vopr[0])
    global ttt #?????
    ttt = 0
    return ttt

@bot.message_handler(func=lambda message: True)
def get_treners(message):
    global ttt
    if ttt == 0:
            user_data['size'] = message.text
            bot.send_message(message.chat.id, vopr[1])
            bot.register_next_step_handler(message, get_adress)
            print(ttt)

def get_adress(message):
        user_data['model'] = message.text
        bot.send_message(message.chat.id, vopr[2])
        bot.register_next_step_handler(message, get_comment)

def get_comment(message):
        user_data['adress'] = message.text
        bot.send_message(message.chat.id, vopr[3])
        bot.register_next_step_handler(message, get_number)

def get_number(message):
        user_data['comment'] = message.text
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("1 Model")

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("2 Model")

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item3 = types.KeyboardButton("3 Model")
        markup.row(item1, item2, item3)
        bot.send_message(message.chat.id, vopr[4], reply_markup=markup)
        bot.register_next_step_handler(message, get_photo)

def get_photo(message):
        user_data['num'] = message.text
        if message.text in ord_list_photo.keys():
            nn = ord_list_photo[message.text]
            photo = open(nn, 'rb')
            bot.send_photo(message.chat.id, photo)

            bot.send_message(message.chat.id, 'Подтвердите заказ', reply_markup=types.ReplyKeyboardRemove())
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("+")

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item2 = types.KeyboardButton("-")
            markup.row(item1, item2)
            bot.send_message(message.chat.id, 'Если все верно нажмите +\nЕсли вы хотите отчистить данные нажмите -',
                             reply_markup=markup)
            bot.register_next_step_handler(message, get_gotov)
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item2 = types.KeyboardButton("/hh")
            markup.row(item2)
            bot.send_message(message.chat.id, 'Модель выбранна не коректно',
                             reply_markup=markup)

def get_gotov(message):
        user_data['true'] = message.text
        if message.text == '+':
            bot.send_message(message.chat.id, 'В ближайшее врямя с вами свяжется наш менеджер для подтверждения заказа',
                             reply_markup=types.ReplyKeyboardRemove())
            sl = user_data
            conn = sqlite3.connect('user_all_order.sql')
            cur = conn.cursor()
            name = sl['name']
            size = sl['size']
            model = sl['model']
            adress = sl['adress']
            comment = sl['comment']
            num = sl['num']

            cur.execute(
                "INSERT INTO users(name, size,model,address,comment,num) VALUES ('%s','%s','%s','%s','%s','%s')" % (
                name, size, model, adress, comment, num))
            conn.commit()
            cur.close()
            conn.close()
        else:
            bot.send_message(message.chat.id, 'Вы отменили заказ', reply_markup=types.ReplyKeyboardRemove())
            user_data.clear()
        print(user_data)
        global ttt
        ttt = 1

        return ttt


bot.polling(none_stop=True)