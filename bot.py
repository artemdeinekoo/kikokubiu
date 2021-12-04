import telebot
from telebot import types
import sqlite3


conn = sqlite3.connect("database.db", check_same_thread=False)
cur = conn.cursor()
def addNewClient(user_id, user_name, user_surname, username):
    cur.execute("""INSERT INTO users(user_id, user_name, user_surname, username) 
    VALUES(?, ?, ?, ?);""", (user_id, user_name, user_surname, username))
    conn.commit()

bot = telebot.TeleBot("2127112849:AAG2ggv9sZVvABd3E9uvXjBL0jL9YiOnPrM")

@bot.message_handler(commands=['start'])
def handle_command(message):
    userId = message.from_user.id
    userFname = message.from_user.first_name
    userLname = message.from_user.last_name
    username = message.from_user.username

    addNewClient(userId, userFname, user_surname = userLname, username= username)


    helloMessage = "Добрий день, вітаємо вас у інтернет магазині КікоКубіу! \nОберіть категорію товару, яка вас цікавить."
    keyboard = types.InlineKeyboardMarkup()
    keyProcessors = types.InlineKeyboardButton(text='Процессори', callback_data='/processors')
    keyboard.add(keyProcessors)
    keyGraphicCards = types.InlineKeyboardButton(text='Відеокарти', callback_data='/graphic-cards')
    keyboard.add(keyGraphicCards)
    bot.send_message(message.from_user.id, text=helloMessage, reply_markup= keyboard)

bot.polling()