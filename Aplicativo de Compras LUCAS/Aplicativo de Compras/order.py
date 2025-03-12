from customtkinter import *
from screen import Screen
from database import Database
from app import App


class Order(Screen):
    def __init__(self, orders, username):
        super().__init__()
        self.sql = Database()

        self.username = username
        self.orders = orders
        self.size()
        self.total_bag()
        self.Labels()
        self.Buttons()
        self.run()

    def Labels(self):
        frame = CTkFrame(master=self.screen, height=400, width=500)
        frame.place(x=250, y=100)

        scrollbar = CTkScrollbar(master=frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        canvas = CTkCanvas(master=frame, yscrollcommand=scrollbar.set, bg='#222222', highlightthickness=0)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        scrollbar.configure(command=canvas.yview)

        inner_frame = CTkFrame(master=canvas, bg_color="#222222")
        canvas.create_window((0, 0), window=inner_frame, anchor=NW)

        for product, quantity in self.orders.items():
            price = self.sql.ProductPrice(product)
            label_text = (
                f"Produto: {product}\n"
                f"Quantidade: {quantity}\n"
                f"Preço por unidade: R${price:.2f}\n"
                "\n"
            )
            label = CTkLabel(master=inner_frame, text=label_text, font=self.text, justify=LEFT)
            label.pack(pady=5)

        inner_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox(ALL))

        order_text = CTkLabel(master=self.screen, text='Pedido:', font=self.text)
        order_text.place(x=250, y=50)
        total_carrinho = CTkLabel(master=self.screen, text=f'Total do Carrinho: R${self.total:.2f}', font=self.text)
        total_carrinho.place(x=250, y=350)

    def Buttons(self):
        self.buy = CTkButton(master=self.screen, text="Comprar", width=300, font=self.text, command=self.pay)
        self.buy.place(x=250, y=400)

        self.cancel = CTkButton(master=self.screen, text="Cancelar", width=300, font=self.text, fg_color="red", command=self.cancel)
        self.cancel.place(x=250, y=450)

    def total_bag(self):
        self.total = 0
        for product, quantity in self.orders.items():
            value = self.sql.ProductPrice(product)
            self.total += value * quantity

        return self.total

    def cancel(self):
        self.screen.destroy()
        App(self.username)

    def pay(self):
        self.screen.destroy()
        from payment import Payment
        Payment(self.total, self.username, self.orders)


if __name__ == "__main__":
    Order({}, '')
