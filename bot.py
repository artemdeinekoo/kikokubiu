import telebot
from client import Client
from items import *
from database import *
from keyboards import *
category = 'Category' 


#########################  Токен бота ################################################
bot = telebot.TeleBot("2127112849:AAG2ggv9sZVvABd3E9uvXjBL0jL9YiOnPrM")

############################ Задаємо об'єкти ###################################
botDB = BotDB("database.db")

client = Client()

item = Item()
#################################################################################
def selectCategory(call, itemCategory):
    bot.send_photo(call.message.chat.id, photo = item.showItemPhoto(item.addItemArr(itemCategory)))
    bot.send_message(call.message.chat.id, text = item.showItem(item.addItemArr(itemCategory)), reply_markup =  item.itemKeyboard())
    global category
    category = itemCategory


############################# Бот виконує команди #############################
@bot.message_handler(commands = ['start'])
def handle_command(message):
     
    if botDB.user_exists(message.from_user.id) == True:

        bot.send_message(message.from_user.id, text = welcomeMessage(), reply_markup = startKeyboard())

    elif botDB.user_exists(message.from_user.id) == False:

        botDB.add_user(message.from_user.id, message.from_user.first_name, message.from_user.last_name, username = message.from_user.username)
        bot.send_message(message.from_user.id, text = welcomeMessage(), reply_markup = startKeyboard())

@bot.callback_query_handler(lambda call: True)

def handle(call):
    if call.data == 'catalog':
        bot.edit_message_text (chat_id=call.message.chat.id, 
        message_id=call.message.message_id, text = catalogMessage(), 
        reply_markup = catalogKeyboard())
    
    elif call.data == 'cpu':
        global category
        category = 'CPU'
        selectCategory(call, 'CPU')
        
    elif call.data == 'gpu':
        selectCategory(call, 'GPU')

    elif call.data == 'motherboards':
        selectCategory(call, 'Motherboard')
    
    elif call.data == 'ram':
        selectCategory(call, 'RAM')

    elif call.data == 'ssd':
        selectCategory(call, 'SSD')

    elif call.data == 'cases':
        selectCategory(call, 'Case')



    elif call.data == 'previous':
        item.previousItem(item.addItemArr(category))
        bot.send_photo(call.message.chat.id, photo = item.showItemPhoto(item.addItemArr(category)))
        bot.send_message(call.message.chat.id, text = item.showItem(item.addItemArr(category)), reply_markup =  item.itemKeyboard())

    elif call.data == 'next':
        item.nextItem(item.addItemArr(category))
        bot.send_photo(call.message.chat.id, photo = item.showItemPhoto(item.addItemArr(category)))
        bot.send_message(call.message.chat.id, text = item.showItem(item.addItemArr(category)), reply_markup =  item.itemKeyboard())

    elif call.data == 'backToCatalog':
        bot.send_message(call.message.chat.id, text = catalogMessage(), reply_markup=  catalogKeyboard())
        item.itemId = 0

    elif call.data == 'backToTheFirstMenu':
        bot.send_message(call.message.chat.id, text = welcomeMessage(), reply_markup = startKeyboard())
        item.itemId = 0

    elif call.data == 'cart':
        for i in range(len(client.cart)):
            bot.send_message(call.message.chat.id, text = client.cart[i])
        bot.send_message(call.message.chat.id, text = client.showSubtotal(), reply_markup = cartKeyboard())

    elif call.data == 'addToCart':
        client.cart.append(item.name)
        client.sum += int(item.price)
        bot.send_message(call.message.chat.id, text = 'Вітаємо, товар успішно додано в корзину!', reply_markup = startKeyboard())

    elif call.data == 'clearCart':
        client.clearCart()
        bot.send_message(call.message.chat.id, text = 'Корзину очищено!', reply_markup = startKeyboard())

    elif call.data == 'accept':
        sent = bot.send_message(call.message.chat.id, text = "Зараз вам потрібно буде вводити контактні дані, щоби наш менеджер із вами зв'язався. Якщо із вами не зв'язалися протягом 24 годин, оформіть замовлення ще раз. \n Введіть свій номер телефону:", reply_markup = nlyBackKey())
        bot.register_next_step_handler(sent, addOrderToDb)
        

def addOrderToDb(message):
    bot.send_message(message.chat.id, 'Дякуємо за замовлення!❤️')
    client.acceptOrder(client_id = message.from_user.id, client_name = message.text)



bot.polling()

