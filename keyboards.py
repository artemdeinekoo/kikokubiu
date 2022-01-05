from telebot import types


######################### Меню, яке отримує користувач після вводу команди start #######################################
def welcomeMessage():
        helloMessage = "Вітаємо вас у магазині КікоКубіу! \nУ нас Ви знайдете найновіші та найпотужніші моделі комплектуючих для вашого комп'ютера. \nНатисніть кнопку нижче, щоби переглянкти асортимент\n "
        
        return helloMessage

def startKeyboard():
    firstKeyboard = types.InlineKeyboardMarkup()
    keyOpenCatalog = types.InlineKeyboardButton(text='Перейти до каталогу 📃', callback_data='catalog')
    keyViewCart = types.InlineKeyboardButton(text='Переглянути корзину 🛒', callback_data='cart')
    firstKeyboard.add(keyOpenCatalog, keyViewCart) 
    
    return firstKeyboard

###########################  Меню, яке отримує користувач, якщо натиснув на кнопку "перейти до каталогу" ########################
def catalogMessage():
    askMessage = "Оберіть категорію товару, яка вас цікавить."

    return askMessage

def catalogKeyboard():
    keyboard = types.InlineKeyboardMarkup()

    keyProcessors = types.InlineKeyboardButton(text='Процессори', callback_data='cpu')
    keyboard.add(keyProcessors)

    keyGraphicCards = types.InlineKeyboardButton(text='Відеокарти', callback_data='gpu')
    keyboard.add(keyGraphicCards)

    keyMotherboards = types.InlineKeyboardButton(text='Материнські плати', callback_data='motherboards')
    keyboard.add(keyMotherboards)

    keyRam = types.InlineKeyboardButton(text="Оперативна пам'ять", callback_data='ram')
    keyboard.add(keyRam)

    keySsd = types.InlineKeyboardButton(text='SSD накопичувачі', callback_data='ssd')
    keyboard.add(keySsd)

    keyCases = types.InlineKeyboardButton(text = "Комп'ютерні корупси", callback_data='cases')
    keyboard.add(keyCases)

    keyBackToTheFirstMenu = types.InlineKeyboardButton(text = "🔙", callback_data='backToTheFirstMenu')
    keyboard.add(keyBackToTheFirstMenu)

    return keyboard
