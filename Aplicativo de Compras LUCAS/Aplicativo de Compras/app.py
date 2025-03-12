from customtkinter import *
from screen import Screen
from login import Login
from database import Database
from tkinter import messagebox


class App(Screen):
    def __init__(self, username):
        super().__init__()
        self.sql = Database()

        self.username = username
        self.orders = {}
        self.nomeprod = None
        self.screensize = "800x600"
        self.combobox()
        self.labels()
        self.entrys()
        self.buttons()
        self.size()
        self.run()

    def labels(self):
        balance = self.sql.GetBalance(self.username)
        self.balance_label = CTkLabel(master=self.screen, text=f'Saldo Atual: R${balance:.2f}', font=self.text)
        self.balance_label.place(x=250, y=50)

        self.combo_label = CTkLabel(master=self.screen, text="Escolha o Produto", font=self.text)
        self.combo_label.place(x=250, y=100)

        self.amount_label = CTkLabel(master=self.screen, text="Quantidade", font=self.text)
        self.amount_label.place(x=250, y=170)

        self.valor_unidade_label = CTkLabel(master=self.screen, text="Preço da unidade: R$0.00", font=self.text)
        self.valor_unidade_label.place(x=250, y=250)

        self.valor_total_label = CTkLabel(master=self.screen, text="Valor total: R$0.00", font=self.text)
        self.valor_total_label.place(x=250, y=300)

        self.bag_value_label = CTkLabel(master=self.screen, text="Valor no Carrinho: R$0.00", font=self.text)
        self.bag_value_label.place(x=250, y=350)

    def combobox(self):
        self.productName = self.sql.ProductsNames()
        self.combo = CTkComboBox(master=self.screen, values=self.productName, width=300, dropdown_font=self.text, font=self.text, command=self.update_price)
        self.combo.place(x=250, y=130)

    def entrys(self):
        self.amount = CTkEntry(master=self.screen, width=50, font=self.text)
        self.amount.place(x=250, y=200)
        self.amount.bind("<KeyRelease>", self.update_total_price)

    def buttons(self):
        self.add = CTkButton(master=self.screen, text="Adicionar ao Carrinho", width=300, font=self.text, command=self.add_bag)
        self.add.place(x=250, y=400)

        self.finalizar = CTkButton(master=self.screen, text="Finalizar Pedido", width=300, font=self.text, command=self.end_order)
        self.finalizar.place(x=250, y=450)
        self.back = CTkButton(master=self.screen, text="Voltar", width=300, font=self.text, command=self.back, fg_color="green")
        self.back.place(x=250, y=500)

    def update_price(self, event=None):
        self.nomeprod = self.combo.get()
        price = self.sql.ProductPrice(self.nomeprod)
        self.valor_unidade_label.configure(text=f"Preço da unidade: R${price:.2f}")
        self.update_total_price()

    def update_total_price(self, event=None):
        self.quantidade = self.amount.get()
        if self.quantidade.isdigit():
            self.quantidade = int(self.quantidade)
            preco_unidade = self.sql.ProductPrice(self.nomeprod)
            valor_total = self.quantidade * preco_unidade
            self.valor_total_label.configure(text=f"Valor total: R${valor_total:.2f}")
        else:
            self.valor_total_label.configure(text="Valor total: R$0.00")

    def add_bag(self):
        self.orders[self.nomeprod] = self.quantidade
        self.update_bag()
        messagebox.showinfo('Produto Adicionado ao Carrinho', f'{self.quantidade} Unidade(s) do Produto "{self.nomeprod}" foram adicionadas ao carrinho.')

    def update_bag(self, event=None):
        self.bag = 0
        for product, quantity in self.orders.items():
            unit_price = self.sql.ProductPrice(product)
            self.bag += unit_price * quantity
        self.bag_value_label.configure(text=f"Valor no Carrinho: R${self.bag:.2f}")

    def end_order(self):
        from order import Order
        self.screen.destroy()
        Order(self.orders, self.username)

    def back(self):
        self.screen.destroy()
        Login()


if __name__ == "__main__":
    login_screen = Login()
    login_screen.run()

    if login_screen.usernameCad:
        username = login_screen.usernameCad
        app = App(username)
