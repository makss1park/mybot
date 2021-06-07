import telebot
import config
bot = telebot.Telebot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message)
sti = open('sticker.webp','rb')
bot.send_sticker(message.chat.id, sti)
bot.send_message(message.chat.id, "Добропоожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный мною.".format(message.from_user, bot.get_me()),
		parse_mode='html')

@bot.message_handler(content_types=['text'])
def hello(message)
	bot.send_message(message.chat.id, message.text)

	# RUN
	bot.polling(none_stop=True)
