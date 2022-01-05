class Client:
    def __init__(self):
        self.cart = []

    def showCart(self):
        if len(self.cart) == 0:
            return "Наразі ваша корзина пуста 😕"
        else:
            return self.cart