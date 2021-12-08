import telebot
from telebot import types
import sqlite3



bot = telebot.TeleBot("2127112849:AAG2ggv9sZVvABd3E9uvXjBL0jL9YiOnPrM")

class BotDB:

    def __init__(self, db_file):
        """Ініціалізація з'єднання з БД"""
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id):
        """Перевіряємо чи є користувач в БД"""
        result = self.cursor.execute("SELECT id FROM users WHERE user_id = ?", (user_id,))
        return bool(len(result.fetchall()))

    def get_user_id(self, user_id):
        """Дістаємо id клієнта в базі по його user_id"""
        result = self.cursor.execute("SELECT id FROM users WHERE user_id = ?", (user_id,))
        return result.fetchone()

    def add_user(self, user_id, user_name, user_surname, username):
        self.cursor.execute("""INSERT INTO users(user_id, user_name, user_surname, username) 
        VALUES(?, ?, ?, ?);""", (user_id, user_name, user_surname, username))
        
        self.conn.commit()

    def close(self):
        """Закриваємо з'єднання з БД"""
        self.conn.close()


class Item:
    def __init__(self, db_file = 'database.db', id = 1, category = 'CPU', brand = 'Intel', name = 'Intel Core i9 11900K', price = 16799, img ='https://hotline.ua/img/tx/272/2727385495.jpg', ua_category = 'Процесори'):
        """Ініціалізація з'єднання з БД + атрибути товару"""
        self.conn = sqlite3.connect(db_file, check_same_thread = False)
        self.cursor = self.conn.cursor()
        self.id = id
        self.category = category
        self.brand = brand
        self.name = name
        self.price = price 
        self.img = img
        self.ua_category = ua_category

    

    # def __str__(self):
    #     return f"{self.ua_category}: {self.brand} {self.name} \nЦіна: {self.price} ₴"


class Processor(Item):
    def showProcessors(self):
        self.cursor.execute("SELECT * FROM processors WHERE  good_id = ?", (self.id,))
        row = self.cursor.fetchone()
        self.category = row[1]
        self.brand = row[2]
        self.name = row[3]
        self.price = row[4] 
        self.ua_category = row[6]

        return f"{self.ua_category}: {self.brand} {self.name} \nЦіна: {self.price} ₴"

    def showProcessorPhoto(self):
        self.cursor.execute("SELECT * FROM processors WHERE  good_id = ?", (self.id,))
        row = self.cursor.fetchone()
        self.img = row[5]
        return self.img


class GraphicCards(Item):
    def showGraphicCards(self):
        self.cursor.execute("SELECT * FROM gpu WHERE  good_id = ?", (self.id,))
        row = self.cursor.fetchone()
        self.category = row[1]
        self.brand = row[2]
        self.name = row[3]
        self.price = row[4] 
        self.ua_category = row[6]

        return f"{self.ua_category}: {self.brand} {self.name} \nЦіна: {self.price} ₴"

    def showGPUPhoto(self):
        self.cursor.execute("SELECT * FROM gpu WHERE  good_id = ?", (self.id,))
        row = self.cursor.fetchone()
        self.img = row[5]
        return self.img



class Motherboards(Item):
    def showMotherBoards(self):
        self.cursor.execute("SELECT * FROM motherboards WHERE  good_id = ?", (self.id,))
        row = self.cursor.fetchone()
        self.category = row[1]
        self.brand = row[2]
        self.name = row[3]
        self.price = row[4] 
        self.ua_category = row[6]

        return f"{self.ua_category}: {self.brand} {self.name} \nЦіна: {self.price} ₴"

    def showMotherBoardPhoto(self):
        self.cursor.execute("SELECT * FROM motherboards WHERE  good_id = ?", (self.id,))
        row = self.cursor.fetchone()
        self.img = row[5]
        return self.img
        

class Ram(Item):
    def showRAM(self):
        self.cursor.execute("SELECT * FROM ram WHERE  good_id = ?", (self.id,))
        row = self.cursor.fetchone()
        self.category = row[1]
        self.brand = row[2]
        self.name = row[3]
        self.price = row[4] 
        self.ua_category = row[6]

        return f"{self.ua_category}: {self.brand} {self.name} \nЦіна: {self.price} ₴"

    def showRAMPhoto(self):
        self.cursor.execute("SELECT * FROM ram WHERE  good_id = ?", (self.id,))
        row = self.cursor.fetchone()
        self.img = row[5]
        return self.img

class SsdDisk(Item):
    def showSsdDisks(self):
        self.cursor.execute("SELECT * FROM ssd WHERE  good_id = ?", (self.id,))
        row = self.cursor.fetchone()
        self.category = row[1]
        self.brand = row[2]
        self.name = row[3]
        self.price = row[4] 
        self.ua_category = row[6]

        return f"{self.ua_category}: {self.brand} {self.name} \nЦіна: {self.price} ₴"

    def showSsdDiskPhoto(self):
        self.cursor.execute("SELECT * FROM ssd WHERE  good_id = ?", (self.id,))
        row = self.cursor.fetchone()
        self.img = row[5]
        return self.img


class Case(Item):
    def showCases(self):
        self.cursor.execute("SELECT * FROM case WHERE  good_id = ?", (self.id,))
        row = self.cursor.fetchone()
        self.category = row[1]
        self.brand = row[2]
        self.name = row[3]
        self.price = row[4] 
        self.ua_category = row[6]

        return f"{self.ua_category}: {self.brand} {self.name} \nЦіна: {self.price} ₴"

    def showCasePhoto(self):
        self.cursor.execute("SELECT * FROM case WHERE  good_id = ?", (self.id,))
        row = self.cursor.fetchone()
        self.img = row[5]
        return self.img

class Client:
    def __init__(self):
        self.cart = []

    def showCart(self):
        if len(self.cart) == 0:
            return "Наразі ваша корзина пуста 😕"
        else:
            return self.cart

def welcomeMessage():
        helloMessage = "Вітаємо вас у магазині КікоКубіу! \nУ нас Ви знайдете найновіші та найпотужніші моделі комплектуючих для вашого комп'ютера. \nНатисніть кнопку нижче, щоби переглянкти асортимент\n "
        
        return helloMessage

def startKeyboard():
    firstKeyboard = types.InlineKeyboardMarkup()
    keyOpenCatalog = types.InlineKeyboardButton(text='Перейти до каталогу 📃', callback_data='catalog')
    keyViewCart = types.InlineKeyboardButton(text='Переглянути корзину 🛒', callback_data='cart')
    firstKeyboard.add(keyOpenCatalog, keyViewCart) 
    
    return firstKeyboard

def catalogMessage():
    askMessage = "Оберіть категорію товару, яка вас цікавить."

    return askMessage

def printCatalog():
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

def cpuKeyboard():
    cpuKeyboard = types.InlineKeyboardMarkup()

    keyBackToCat = types.InlineKeyboardButton(text='🔙', callback_data='backToCat')
    cpuKeyboard.add(keyBackToCat)
    
    keyPrevious = types.InlineKeyboardButton(text='◀️', callback_data='previousCpu')
    cpuKeyboard.add(keyPrevious)

    keyNext = types.InlineKeyboardButton(text='▶️', callback_data='nextCpu')
    cpuKeyboard.add(keyNext)

    keyAddCpuToCart = types.InlineKeyboardButton(text='🛒', callback_data='addCpuToCart')
    cpuKeyboard.add(keyAddCpuToCart)

    return cpuKeyboard

def printCPU(call):
    bot.send_photo(call.message.chat.id, photo = processor.showProcessorPhoto())
    bot.send_message(call.message.chat.id, text = processor.showProcessors(), reply_markup = cpuKeyboard())

def gpuKeyboard():
    gpuKeyboard = types.InlineKeyboardMarkup()

    keyBackToCat = types.InlineKeyboardButton(text='🔙', callback_data='backToCat')
    gpuKeyboard.add(keyBackToCat)
    
    keyPrevious = types.InlineKeyboardButton(text='◀️', callback_data='previousGpu')
    gpuKeyboard.add(keyPrevious)

    keyNext = types.InlineKeyboardButton(text='▶️', callback_data='nextGpu')
    gpuKeyboard.add(keyNext)

    keyAddGpuToCart = types.InlineKeyboardButton(text='🛒', callback_data='addGpuToCart')
    gpuKeyboard.add(keyAddGpuToCart)

    return gpuKeyboard


def printGPU(call):
    bot.send_photo(call.message.chat.id, photo = gpu.showGPUPhoto())
    bot.send_message(call.message.chat.id, text = gpu.showGraphicCards(), reply_markup = gpuKeyboard())

def motherboardKeyboard():
    motherboardKeyboard = types.InlineKeyboardMarkup()

    keyBackToCat = types.InlineKeyboardButton(text='🔙', callback_data='backToCat')
    motherboardKeyboard.add(keyBackToCat)
    
    keyPrevious = types.InlineKeyboardButton(text='◀️', callback_data='previousMotherboard')
    motherboardKeyboard.add(keyPrevious)

    keyNext = types.InlineKeyboardButton(text='▶️', callback_data='nextMotherboard')
    motherboardKeyboard.add(keyNext)

    keyAddMotherboardToCart = types.InlineKeyboardButton(text='🛒', callback_data='addMotherboardToCart')
    motherboardKeyboard.add(keyAddMotherboardToCart)

    return motherboardKeyboard

def printMotherboard(call):
    bot.send_photo(call.message.chat.id, photo = motherboard.showMotherBoardPhoto())
    bot.send_message(call.message.chat.id, text = motherboard.showMotherBoards(), reply_markup = motherboardKeyboard())

def ramKeyboard():
    ramKeyboard = types.InlineKeyboardMarkup()

    keyBackToCat = types.InlineKeyboardButton(text='🔙', callback_data='backToCat')
    ramKeyboard.add(keyBackToCat)
    
    keyPrevious = types.InlineKeyboardButton(text='◀️', callback_data='previousRam')
    ramKeyboard.add(keyPrevious)

    keyNext = types.InlineKeyboardButton(text='▶️', callback_data='nextRam')
    ramKeyboard.add(keyNext)

    keyAddRamToCart = types.InlineKeyboardButton(text='🛒', callback_data='addRamToCart')
    ramKeyboard.add(keyAddRamToCart)

    return ramKeyboard

def printRAM(call):
    bot.send_photo(call.message.chat.id, photo = ram.showRAM())
    bot.send_message(call.message.chat.id, text = ram.showRAM(), reply_markup = ramKeyboard())

def ssdKeyboard():
    ssdKeyboard = types.InlineKeyboardMarkup()

    keyBackToCat = types.InlineKeyboardButton(text='🔙', callback_data='backToCat')
    ssdKeyboard.add(keyBackToCat)
    
    keyPrevious = types.InlineKeyboardButton(text='◀️', callback_data='previousSsd')
    ssdKeyboard.add(keyPrevious)

    keyNext = types.InlineKeyboardButton(text='▶️', callback_data='nextSsd')
    ssdKeyboard.add(keyNext)

    keyAddSsdToCart = types.InlineKeyboardButton(text='🛒', callback_data='addSsdToCart')
    ssdKeyboard.add(keyAddSsdToCart)

    return ssdKeyboard

def printSSD(call):
    bot.send_photo(call.message.chat.id, photo = ssd.showSsdDiskPhoto())
    bot.send_message(call.message.chat.id, text = ssd.showSsdDisks(), reply_markup = ramKeyboard())



############################Задаємо об'єкти###################################
botDB = BotDB("database.db")

client = Client()

processor = Processor()
gpu = GraphicCards()
motherboard = Motherboards()
ram = Ram()
ssd = SsdDisk()



#############################Бот виконує команди#############################
@bot.message_handler(commands = ['start'])
def handle_command(message):
     
    if botDB.user_exists(message.from_user.id) == True:

            bot.send_message(message.from_user.id, text = welcomeMessage(), reply_markup = startKeyboard())

    elif botDB.user_exists(message.from_user.id) == False:

            botDB.add_user(message.from_user.id, message.from_user.first_name, message.from_user.last_name, username = message.from_user.username)
            bot.send_message(message.from_user.id, text = welcomeMessage(), reply_markup = startKeyboard())

@bot.callback_query_handler(func = lambda call: True)

def callback_worker(call):
    if call.data == "catalog":
         bot.send_message(call.message.chat.id, text = catalogMessage(), reply_markup=  printCatalog())
    elif call.data == "cart":
        bot.send_message(call.message.chat.id, text = client.showCart())



    elif call.data == "cpu":
        printCPU(call)
    elif call.data == "backToCat":
        bot.send_message(call.message.chat.id, text = catalogMessage(), reply_markup = printCatalog())
    elif call.data == "previousCpu":
        processor.id -= 1
        printCPU(call)
    elif call.data == "nextCpu":
        processor.id += 1
        printCPU(call)
    elif call.data == "addCpuToCart":
        client.cart.append(processor.showProcessors())
        bot.send_message(call.message.chat.id, "Товар додано до вашої корзини🥳")

    elif call.data == "gpu":
        printGPU(call)
    elif call.data == "previousGpu":
        gpu.id -= 1
        printGPU(call)
    elif call.data == "nextGpu":
        gpu.id += 1
        printGPU(call)
    elif call.data == "addGpuToCart":
        client.cart.append(gpu.showGraphicCards())
        bot.send_message(call.message.chat.id, "Товар додано до вашої корзини🥳")

    elif call.data == "motherboards":
        printMotherboard(call)
    elif call.data == "previousMotherboard":
        motherboard.id -= 1
        printMotherboard(call)
    elif call.data == "nextMotherboard":
        motherboard.id += 1
        printMotherboard(call)
    elif call.data == "addMotherboardToCart":
        client.cart.append(motherboard.showMotherBoards())
        bot.send_message(call.message.chat.id, "Товар додано до вашої корзини🥳")

    elif call.data == "ram":
        printRAM(call)
    elif call.data == "previousRam":
        ram.id -= 1
        printRAM(call)
    elif call.data == "nextRam":
        ram.id += 1
        printRAM(call)
    elif call.data == "addRamToCart":
        client.cart.append(ram.showRAM())
        bot.send_message(call.message.chat.id, "Товар додано до вашої корзини🥳")

    elif call.data == "ssd":
        printSSD(call)
    elif call.data == "previousSsd":
        ssd.id -= 1
        printSSD(call)
    elif call.data == "nextSsd":
        ssd.id += 1
        printSSD(call)
    elif call.data == "addSsdtoCart":
        client.cart.append(ssd.showSSD())
        bot.send_message(call.message.chat.id, "Товар додано до вашої корзини🥳")

    
    

    



bot.polling()
