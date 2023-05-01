import telebot
from telebot import types

bot = telebot.TeleBot('5661322452:AAG1JA7O3Du2MZu_YUV_sAgC6MI_-GjdsyI')


@bot.message_handler(commands=['start'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    options = types.KeyboardButton('посмотреть возможности')
    markup.add(options)
    bot.send_message(message.chat.id, 'Добро пожаловать', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    if (message.text == "посмотреть возможности"):
        have = types.KeyboardButton('растения в наличии')
        buy = types.KeyboardButton('собираюсь купить')
        markup.add(have, buy)
        bot.send_message(message.chat.id, 'ваши дальнейшие действия?', reply_markup=markup)
    elif (message.text == "собираюсь купить"):
        check = types.KeyboardButton("посмотреть каталог")
        add = types.KeyboardButton("обновить каталог")
        back = types.KeyboardButton("вернуться в главное меню")
        markup.add(check, add, back)
        bot.send_message(message.chat.id, text= "чего именно вы хотите?", reply_markup=markup)
    elif (message.text == "растения в наличии"):
        check = types.KeyboardButton("посмотреть имеющиеся")
        add = types.KeyboardButton("добавить новые")
        back = types.KeyboardButton("вернуться в главное меню")
        markup.add(check, add, back)
        bot.send_message(message.chat.id, text="чего именно вы хотите?", reply_markup=markup)

    elif(message.text == "вернуться в главное меню"):
        options = types.KeyboardButton('посмотреть возможности')
        markup.add(options)
        bot.send_message(message.chat.id, 'Вы вернулись в главное меню', reply_markup=markup)
    #elif (message.text == "в наличии"):

bot.polling(none_stop=True)
