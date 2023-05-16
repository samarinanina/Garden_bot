from telebot import types
from scr.db import *
from scr.config import const


@bot.message_handler(commands=[const.start])
def main_functions(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    options = types.KeyboardButton(const.op)
    markup.add(options)
    bot.send_message(message.chat.id, const.welcome, reply_markup=markup)


@bot.message_handler(commands=[const.cont])
def main_functions(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    options = types.KeyboardButton(const.op)
    markup.add(options)
    bot.send_message(message.chat.id, const.cont_1, reply_markup=markup)


@bot.message_handler(content_types=[const.text])
def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    if (message.text == const.op):
        have = types.KeyboardButton(const.in_stock)
        buy = types.KeyboardButton(const.to_buy)
        markup.add(have, buy)
        bot.send_message(message.chat.id, const.next_move, reply_markup=markup)
    elif (message.text == const.to_buy):
        check = types.KeyboardButton(const.look)
        add = types.KeyboardButton(const.new)
        back = types.KeyboardButton(const.f_return)
        markup.add(check, add, back)
        bot.send_message(message.chat.id, text=const.wish, reply_markup=markup)
    elif (message.text == const.in_stock):
        check = types.KeyboardButton(const.have)
        add = types.KeyboardButton(const.add_new)
        back = types.KeyboardButton(const.f_return)
        markup.add(check, add, back)
        bot.send_message(message.chat.id, text=const.wish, reply_markup=markup)

    elif (message.text == const.f_return):
        options = types.KeyboardButton(const.op)
        markup.add(options)
        bot.send_message(message.chat.id, const.t_return, reply_markup=markup)
    elif (message.text == const.new):
        del_one = types.KeyboardButton(const.delete)
        add = types.KeyboardButton(const.add)
        change = types.KeyboardButton(const.change_to_have)
        markup.add(del_one, add, change)
        bot.send_message(message.chat.id, const.change, reply_markup=markup)
    elif (message.text == const.add_new):
        data_base(message, 1)
    elif (message.text == const.look):
        watch(message, 0)
    elif (message.text == const.have):
        watch(message, 1)
    elif (message.text == const.delete):
        watch(message, 0)
        bot.send_message(message.chat.id, const.name_delete)
        bot.register_next_step_handler(message, delete)
    elif (message.text == const.add):
        data_base(message, 0)
    elif (message.text == const.change_to_have):
        watch(message, 0)
        bot.send_message(message.chat.id, const.name_change)
        bot.register_next_step_handler(message, changement)
    else:
        bot.send_message(message.chat.id, const.wrong_message)


bot.polling(none_stop=True)
