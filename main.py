import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Uzbek", callback_data='uzb')
    item2 = types.InlineKeyboardButton("Русский", callback_data='ru')

    markup.add(item1, item2)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.\n<b>Выберите язык.</b>".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['lang'])
def lang(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Uzbek", callback_data='uzb')
    item2 = types.InlineKeyboardButton("Русский", callback_data='ru')

    markup.add(item1, item2)

    bot.send_message(message.chat.id,
                     "<b>Выберите язык.</b>".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['help'])
def lang(message):
    bot.send_message(message.chat.id, "<b>Помощь.</b>".format(
        message.from_user, bot.get_me()),
                     parse_mode='html')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):

    #keyboard
    mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu1ru = types.KeyboardButton("1")
    menu2ru = types.KeyboardButton("2")
    menu3ru = types.KeyboardButton("3")
    menu1uz = types.KeyboardButton("11")
    menu2uz = types.KeyboardButton("22")
    menu3uz = types.KeyboardButton("33")

    try:
        if call.message:
            if call.data == 'uzb':
                from uzb import qwer
                bot.send_message(call.message.chat.id, text=qwer, reply_markup=mark.add(menu1uz, menu2uz, menu3uz))

            elif call.data == 'ru':
                bot.send_message(call.message.chat.id, 'Вы выбрали русский язык', reply_markup=mark.add(menu1ru, menu2ru, menu3ru))

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='<b>Добро пожаловать | Hush kelibsiz</b>',
                     parse_mode='html', reply_markup=None)


    except Exception as e:
        print(repr(e))



@bot.message_handler(content_types=['text'])
def welcome(message):
    if message.chat.type == 'private':
        if message.text == '1':
            bot.send_message(message.chat.id, '1 кнопка меню')
        elif message.text == '2':
            bot.send_message(message.chat.id, '2 кнопка меню')
        elif message.text == '3':
            bot.send_message(message.chat.id, '3 кнопка меню')
        elif message.text == '11':
            bot.send_message(message.chat.id, '1 кнопка менюuz')
        elif message.text == '22':
            bot.send_message(message.chat.id, '2 кнопка менюuz')
        elif message.text == '33':
            bot.send_message(message.chat.id, '3 кнопка менюuz')
        else:
            bot.send_message(message.chat.id, 'Я не знаю как ответить')







# RUN
bot.polling(none_stop=True)
