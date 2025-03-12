import sqlite3


class Database:
    def __init__(self):
        self.Connect_bd()
        self.Tables()
        self.TablesProducts()
        self.TablesBalance()

    def Connect_bd(self):
        self.conn = sqlite3.connect("Sistem.bd")
        self.cursor = self.conn.cursor()

    def Tables(self):
        self.Connect_bd()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Clientes (
            Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            Username TEXT NOT NULL,
            Password TEXT NOT NULL,
            Saldo FLOAT DEFAULT 0.0
        )""")
        self.conn.commit()

    def TablesProducts(self):
        self.Connect_bd()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Produtos (
            Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Price FLOAT NOT NULL
        )""")
        self.conn.commit()

    def TablesBalance(self):
        self.Connect_bd()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Saldos (
            Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            ClienteId INTEGER NOT NULL,
            Saldo FLOAT DEFAULT 0.0,
            FOREIGN KEY (ClienteId) REFERENCES Clientes(Id)
        )""")
        self.conn.commit()

    def ProductsNames(self):
        self.Connect_bd()
        self.cursor.execute("SELECT Name FROM Produtos")
        products = self.cursor.fetchall()
        return [product[0] for product in products]

    def ProductPrice(self, product_name):
        self.Connect_bd()
        self.cursor.execute("SELECT Price FROM Produtos WHERE Name = ?", (product_name,))
        price = self.cursor.fetchone()
        if price:
            return price[0]
        else:
            print(f"Product not found: {product_name}")
            return 0.0

    def DeleteProduct(self, product_name):
        self.Connect_bd()
        self.cursor.execute("DELETE FROM Produtos WHERE Name = ?", (product_name,))
        self.conn.commit()

    def DeleteClient(self, client_name):
        self.Connect_bd()
        self.cursor.execute("DELETE FROM Clientes WHERE Username = ?", (client_name,))
        self.conn.commit()

    def AddBalance(self, username, valor):
        current_balance = self.GetBalance(username)
        new_balance = current_balance + valor
        self.Connect_bd()
        self.cursor.execute("UPDATE Clientes SET Saldo = ? WHERE Username = ?", (new_balance, username))
        self.conn.commit()

    def GetBalance(self, username):
        self.Connect_bd()
        self.cursor.execute("SELECT Saldo FROM Clientes WHERE Username = ?", (username,))
        balance = self.cursor.fetchone()
        if balance:
            return balance[0]
        else:
            print(f"User not found: {username}")
            return 0.0

    def VerifyPassword(self, username, password):
        self.Connect_bd()
        self.cursor.execute("SELECT Password FROM Clientes WHERE Username = ?", (username,))
        senha = self.cursor.fetchone()
        if senha and senha[0] == password:
            return True
        else:
            return False

    def EnoughBalance(self, username, total):
        balance = self.GetBalance(username)
        return balance >= total

    def BalanceDebt(self, username, total):
        current_balance = self.GetBalance(username)
        new_balance = current_balance - total
        self.Connect_bd()
        self.cursor.execute("UPDATE Clientes SET Saldo = ? WHERE Username = ?", (new_balance, username))
        self.conn.commit()

