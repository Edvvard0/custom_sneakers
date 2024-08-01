# Telegram Bot для продажи кастомных кроссовок

Добро пожаловать в проект Telegram-бота, предназначенного для компании, занимающейся продажей кастомных кроссовок. Этот бот поможет пользователям легко просматривать и заказывать уникальные кроссовки. Сейчас на GitHub только часть проекта остальной функционал будет доделываться.

## Описание

Этот бот предоставляет пользователям возможность:
- Просматривать доступные модели кроссовок с изображениями.
- Получать информацию о ценах и характеристиках.
- Заказывать кроссовки напрямую через Telegram.

## Стек технологий

Проект разработан с использованием следующих технологий:
- **Python**: основной язык программирования.
- **Telebot**: библиотека для работы с Telegram API.

## Структура 
в проекте 2 главные папки
 - Image (фото всех моделей)
 - Code (main.py, sklad.py, tg_token.py)

    + main.py -> содержит основной код бота
    + sklad.py -> совуржит 3 переменные: список комментариев, список моделей и список ссылок на фото
    + tg_token.py -> содержит 1 переменную с токеном бота
  + в проекте есть еще один файл library.txt со списком всех библиотек

## Установка

1. Клонируйте репозиторий:

```git clone https://github.com/Edvvard0/custom_sneakers.git```

2. Установите необходимые библиотеки
 (все библиотеки вынесенны в  отдельный файл library.txt):

```pip install -r library.txt```

3. Настройте бота:
   - Получите токен вашего бота от [BotFather](https://t.me/botfather).
   - Вставьте токен в соответствующее место в файле main.py.

Если у вас есть вопросы или предложения, не стесняйтесь обращаться:

- https://t.me/Edward0076 Telegram
