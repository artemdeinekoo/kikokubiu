import sqlite3


class Client:
    def __init__(self):
        self.cart = []
        self.sum = 0

    def showSubtotal(self):
        return f"Разом: {self.sum} ₴"

    def clearCart(self):
        self.cart.clear()
        self.sum = 0

    def getCart(self):
        for i in range(len(self.cart)):
                a = self.cart[i]

        return a

    def acceptOrder(self, client_id, client_name, db_file = 'database.db'):
        for i in range(len(self.cart)):
            self.conn = sqlite3.connect(db_file, check_same_thread = False)
            self.cursor = self.conn.cursor()
            self.cursor.execute("""INSERT INTO orders(client, client_name, cart, sum) 
            VALUES(?, ?, ?, ?);""", (client_id, client_name, self.cart[i], self.sum))
        
            self.conn.commit()