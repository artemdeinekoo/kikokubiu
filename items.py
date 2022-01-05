import sqlite3
from telebot import types


class Item:
    def __init__(self, db_file = 'database.db', id = 1, category = 'CPU', brand = 'Intel', name = 'Intel Core i9 11900K', price = 16799, img ='https://hotline.ua/img/tx/272/2727385495.jpg', ua_category = 'Процесори', itemId = 0):
        """Ініціалізація з'єднання з БД + атрибути товару"""
        self.conn = sqlite3.connect(db_file, check_same_thread = False)
        self.cursor = self.conn.cursor()
        self.id = id
        self.category = category 
        self.brand = brand
        self.name = name
        self.price = price 
        self.img = img
        self.itemId = itemId

    def addItemArr(self, whichItemCategory):
        self.cursor.execute("SELECT * FROM items WHERE  good_category = ?", (whichItemCategory,))
        stock = self.cursor.fetchall()

        return stock

    def showItem(self, stock):
        self.category = stock[self.itemId][1]
        self.brand = stock[self.itemId][2]
        self.name = stock[self.itemId][3]
        self.price = stock[self.itemId][4] 
        self.ua_category = stock[self.itemId][6]

        return f"{self.ua_category}: {self.brand} {self.name} \nЦіна: {self.price} ₴"

    def showItemPhoto(self, stock):
        self.img = stock[self.itemId][5]
        return self.img

    def itemKeyboard(self):
        itemKeyboard = types.InlineKeyboardMarkup()

        keyBackToCatalog = types.InlineKeyboardButton(text='🔙', callback_data='backToCatalog')
        keyPrevious = types.InlineKeyboardButton(text='⬅️', callback_data='previous')
        keyNext = types.InlineKeyboardButton(text='➡️', callback_data='next')
        keyAddToCart = types.InlineKeyboardButton(text='🛒', callback_data='addToCart')

        itemKeyboard.add(keyBackToCatalog, keyPrevious, keyNext, keyAddToCart)

        return itemKeyboard
    
    def previousItem(self, stock):
        if self.itemId <= 0:
            self.itemId = len(stock) - 1
        else:
            self.itemId -= 1

    def nextItem(self, stock):
        if self.itemId >= len(stock) - 1:
            self.itemId = 0
        else:
            self.itemId += 1
    






