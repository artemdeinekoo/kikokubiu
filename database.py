import sqlite3


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
