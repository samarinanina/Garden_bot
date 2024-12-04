import telebot
import sqlite3
from scr.config import const

bot = telebot.TeleBot('YOUR TOKEN')


def data_base(message, have_it):
    conn = sqlite3.connect(const.table)
    cur = conn.cursor()
    cur.execute(const.create)
    conn.commit()
    cur.close()
    conn.close()
    nom = bot.send_message(message.chat.id, const.write_name)
    bot.register_next_step_handler(nom, name, have_it)


def name(message, have_it):
    global nm
    nm = (message.text.strip()).upper()
    nom = bot.send_message(message.chat.id, const.desc)
    bot.register_next_step_handler(nom, desc, have_it)


def desc(message, have_it):
    description = message.text.strip()
    conn = sqlite3.connect(const.table)
    cur = conn.cursor()
    cur.execute(const.insert % (nm, description, have_it))
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, const.ready)


def watch(message, have_it):
    conn = sqlite3.connect(const.table)
    cur = conn.cursor()
    for value in cur.execute(f"SELECT * FROM buy WHERE have_it = {have_it}"): #не в config из-за форматирования
        bot.send_message(message.chat.id, f'[название]:{value[0]}  [описание]:{value[1]}')


def delete(message):
    nm = message.text.strip()
    conn = sqlite3.connect(const.table)
    cur = conn.cursor()
    cur.execute(const.delete_table % (nm))
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, f'{nm} больше нет в каталоге')


def changement(message):
    nm = message.text.strip()
    conn = sqlite3.connect(const.table)
    cur = conn.cursor()
    cur.execute(const.select % (nm))
    cur.execute(const.update % (nm))
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, f'{nm} перенесено в имеющиеся')
