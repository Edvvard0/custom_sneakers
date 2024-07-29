# -*- coding: utf-8 -*-
from telebot import types, TeleBot
from sklad import comment_list, photo_list, ready_models

bot = TeleBot("7382523397:AAE9bCchn84A4ndqpUEME-A6YkmDAR4_V38")

#Служебные переменные для вывода информации о компании

vopr = ('Какой у вас размер обуви?', 'На каких кросовках Вы хотике сделать кастом?', 'Введите ваш адресс',
        'Оставте комментарий к кастому', 'Номер вашего кастома?', 'Ваш номер телефона?')

list_commands = '''Бот может:
/menu  -  меню
/info - информация о компании
/comments - отзывы
/models - готовые модели 
/individual_castom - индивидуальный заказ
/care - уход за обувью
/order - заказ
/make_order - сделать заказ'''

start_message = f'''Вас приветствует команда Castom night.
Мы занимаемся кастомом кросовок.
В этом боте вы можете сделать предзаказ.
По всем вопросам вы можете обратиться по номеру телефона 
+7 978 00 00 000

{list_commands}
'''

info = '''Мы молодая компания , которая только начинает свою деятельность в маленьком городе.
Наша цель заслужить ваше доверие путём качественной работы и ответственного отношения к каждому клиенту.
Мы стремимся к постоянному совершенствованию и развитию, чтобы обеспечить нашим клиентам только лучший сервис и продукцию.'''

individual_castom = '''Индивидуальные заказы согласуются с менеджером
тг: @Edward0076
номер телефона +7 978 00 00 000 '''

clear = '''Уход!!!!'''


name = '''Для того чтобы сделать заказ заполнити следующие поля:
/size - размер обуви
/mod - модель кросовок
/adress - ваш адресс
/com - комментарий к заказу
/number_castom - номер кастома'''


user_states = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, start_message)


@bot.message_handler(commands=['menu'])
def menu(message):
    bot.send_message(message.chat.id, list_commands)


@bot.message_handler(commands=['info'])
def menu(message):
    bot.send_message(message.chat.id, info)


@bot.message_handler(commands=['care'])
def start(message):
    bot.send_message(message.chat.id, clear)


@bot.message_handler(commands=['individual_castom'])
def comments(message):
    bot.send_message(message.chat.id, individual_castom)


@bot.message_handler(commands=['models'])
def send_models(message):
    user_id = message.from_user.id
    user_states[user_id] = {'index': 0}  # Инициализируем индекс для пользователя
    send_photo(message, user_id)


def send_photo(message, user_id):
    index = user_states[user_id]['index']
    if index < len(photo_list):
        with open(photo_list[index], 'rb') as photo:
            bot.send_photo(message.chat.id, photo, reply_markup=next_button())
            bot.send_photo(message.chat.id, comment_list[index], reply_markup=next_button())
    else:
        bot.send_message(message.chat.id, "Это все модели кроссовок!")


@bot.callback_query_handler(func=lambda call: call.data == 'next')
def next_model(call):
    user_id = call.from_user.id
    if user_id in user_states:
        user_states[user_id]['index'] += 1  # Увеличиваем индекс
        send_photo(call.message, user_id)


def next_button():
    markup = types.InlineKeyboardMarkup()
    next_button = types.InlineKeyboardButton("Next", callback_data='next')
    markup.add(next_button)
    return markup



bot.polling(none_stop=True)