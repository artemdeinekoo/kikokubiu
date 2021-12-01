import telebot
from telebot import types


bot = telebot.TeleBot("2127112849:AAG2ggv9sZVvABd3E9uvXjBL0jL9YiOnPrM")

@bot.message_handler(commands=['start'])
def handle_command(message):
    helloMessage = "Добрий день, вітаємо вас у інтернет магазині КікоКубіу! \nОберіть категорію товару, яка вас цікавить."
    keyboard = types.InlineKeyboardMarkup()
    keyProcessors = types.InlineKeyboardButton(text='Процессори', callback_data='/processors')
    keyboard.add(keyProcessors)
    keyGraphicCards = types.InlineKeyboardButton(text='Відеокарти', callback_data='/graphic-cards')
    keyboard.add(keyGraphicCards)
    bot.send_message(message.from_user.id, text=helloMessage, reply_markup= keyboard)

bot.polling()