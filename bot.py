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

def printCatalog(call):
        askMessage = "Оберіть категорію товару, яка вас цікавить."
        keyboard = types.InlineKeyboardMarkup()

        keyProcessors = types.InlineKeyboardButton(text='Процессори', callback_data='cpu')
        keyboard.add(keyProcessors)

        keyGraphicCards = types.InlineKeyboardButton(text='Відеокарти', callback_data='gpu')
        keyboard.add(keyGraphicCards)

        keyMotherboards = types.InlineKeyboardButton(text='Материнські плати', callback_data='motherboars')
        keyboard.add(keyMotherboards)

        keyRam = types.InlineKeyboardButton(text="Оперативна пам'ять", callback_data='ram')
        keyboard.add(keyRam)

        keySsd = types.InlineKeyboardButton(text='SSD накопичувачі', callback_data='ssd')
        keyboard.add(keySsd)

        keyCases = types.InlineKeyboardButton(text = "Комп'ютерні корупси", callback_data='cases')
        keyboard.add(keyCases)

        bot.send_message(call.message.chat.id, text=askMessage, reply_markup= keyboard)

def showProcessors(call):
    goodKeyboard = types.InlineKeyboardMarkup()

    keyBack = types.InlineKeyboardButton(text= '🔙', callback_data = 'back')
    keyPrevious = types.InlineKeyboardButton(text = '◀️', callback_data = 'previous')
    keyNext = types.InlineKeyboardButton(text = '➡️', callback_data = 'next')
    keyAddToTheCart = types.InlineKeyboardButton(text = '🛒', callback_data = 'addtothecart')
    goodKeyboard.add(keyBack, keyPrevious, keyNext, keyAddToTheCart)


    cur.execute("SELECT * FROM goods where good_category='CPU'")
    row = cur.fetchone()
    goodDesription = f"Процесор: {row[2]} {row[3]} \nЦіна: {row[4]} ₴\n"
    goodImg = row[5]

    bot.send_photo(call.message.chat.id, photo = goodImg)
    bot.send_message(call.message.chat.id, text=goodDesription, reply_markup = goodKeyboard)

    
        


cart = []

@bot.message_handler(commands=['start'])
def handle_command(message):
    userId = message.from_user.id
    userFname = message.from_user.first_name
    userLname = message.from_user.last_name
    username = message.from_user.username

    addNewClient(user_id = userId,user_name = userFname, user_surname = userLname, username= username)

    helloMessage = "Вітаємо вас у магазині КікоКубіу! \nУ нас Ви знайдете найновіші та найпотужніші моделі комплектуючих для вашого комп'ютера. \nНатисніть кнопку нижче, щоби переглянкти асортимент\n "

    firstKeyboard = types.InlineKeyboardMarkup()

    keyOpenCatalog = types.InlineKeyboardButton(text='Перейти до каталогу 📃', callback_data='catalog')
    keyViewCart = types.InlineKeyboardButton(text='Переглянути корзину 🛒', callback_data='cart')
    firstKeyboard.add(keyOpenCatalog, keyViewCart) 
    bot.send_message(message.from_user.id, text = helloMessage, reply_markup = firstKeyboard)

@bot.callback_query_handler(func = lambda call: True)
def callback_worker(call):
    if call.data == "catalog":
        printCatalog(call)
    elif call.data == "cart":
        global cart

        if len(cart) == 0:
            bot.send_message(call.message.chat.id, "Наразі ваша корзина пуста 😕")

    elif call.data == "cpu":
        showProcessors(call)

    elif call.data == "🔙":
        printCatalog(call)

    elif call.data == "➡️":
        showProcessors(call)
bot.polling()