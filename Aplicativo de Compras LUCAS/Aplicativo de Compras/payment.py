from customtkinter import *
from screen import Screen
from database import Database
from tkinter import messagebox
from app import App
from order import Order


class Payment(Screen):
    def __init__(self, total, username, orders):
        super().__init__()

        self.sql = Database()
        self.total = total
        self.username = username
        self.orders = orders

        self.screensize = "450x500"
        self.size()
        self.Labels()
        self.Buttons()
        self.run()

    def Labels(self):
        balance = self.sql.GetBalance(self.username)
        self.balance_label = CTkLabel(master=self.screen, text=f'Saldo Atual: R${balance:.2f}', font=self.text)
        self.balance_label.place(x=75, y=50)

        total_label = CTkLabel(master=self.screen, text=f'Total da Compra: R${self.total:.2f}', font=self.text)
        total_label.place(x=75, y=100)


    def TogglePassword(self):
        if self.check.get():
            self.password_entry.configure(show="")  # Mostra a senha
        else:
            self.password_entry.configure(show="*")  # Oculta a senha

    def Buttons(self):
        self.confirm = CTkButton(master=self.screen, text="Confirmar Pagamento", width=300, font=self.text,
                                   command=self.confirm_payment)
        self.confirm.place(x=75, y=150)

        self.cancel = CTkButton(master=self.screen, text="Cancelar", width=300, font=self.text, fg_color="red",
                                  command=self.cancel)
        self.cancel.place(x=75, y=250)

        self.add_balance = CTkButton(master=self.screen, text="Adicionar Saldo", width=300, font=self.text,
                                         command=self.add_balance, fg_color="green")
        self.add_balance.place(x=75, y=200)

    def update_balance_label(self):
        new_balance = self.sql.GetBalance(self.username)
        self.balance_label.configure(text=f'Saldo Atual: R${new_balance:.2f}')

    def add_balance(self):
        self.add_balance.configure(state=DISABLED)
        self.value_entry = CTkEntry(master=self.screen, width=300, placeholder_text="Digite o valor a adicionar...",
                                    font=self.text)
        self.value_entry.place(x=75, y=300)

        self.password_entry = CTkEntry(master=self.screen, width=300, placeholder_text="Digite sua senha...", font=self.text, show="*")
        self.password_entry.place(x=75, y=350)

        self.check = CTkCheckBox(master=self.screen, text="Mostrar Senha", font=self.text, command=self.TogglePassword)
        self.check.place(x=75, y=400)

        self.confirm_button = CTkButton(master=self.screen, text="Confirmar", width=300, font=self.text,
                                          command=self.confirm_new_balance)
        self.confirm_button.place(x=75, y=450)

    def confirm_new_balance(self):
        self.password = self.password_entry.get()
        if self.sql.VerifyPassword(self.username, self.password):
            self.update_balance_label()
            messagebox.showinfo('Sucesso', 'Saldo adicionado com sucesso')
            valor_adicionar = float(self.value_entry.get())
            self.sql.AddBalance(self.username, valor_adicionar)
            self.update_balance_label()
            self.value_entry.destroy()
            self.password_entry.destroy()
            self.add_balance.configure(state=NORMAL)
            self.confirm_button.destroy()

        else:
            messagebox.showerror('Erro', 'Senha incorreta!')

    def confirm_payment(self):
        current_balance = self.sql.GetBalance(self.username)
        if current_balance >= self.total:
            self.sql.BalanceDebt(self.username, self.total)
            self.update_balance_label()
            self.register_order()
            messagebox.showinfo('Sucesso', 'Pagamento realizado com sucesso!')
            self.screen.destroy()

        else:
            messagebox.showerror('Erro', 'Saldo insuficiente!')

    def register_order(self):
        desktop_path = os.path.join(os.path.expanduser("~"), "Área de Trabalho", "Arquivos - Trabalho Final")
        if not os.path.exists(desktop_path):
            os.makedirs(desktop_path)

        arc = os.path.join(desktop_path, f"{self.username}_pedidos.txt")

        with open(arc, 'a') as arquivo:
            arquivo.write(f"Pedido realizado:\n")
            for product, quantity in self.orders.items():
                price = self.sql.ProductPrice(product)
                arquivo.write(f"Produto: {product}\nQuantidade: {quantity}\nValor por unidade: R${price:.2f}\n\n")
            arquivo.write(f"Total da compra: R${self.total:.2f}\n")
            arquivo.write("-" * 20 + "\n")

    def cancel(self):
        self.screen.destroy()
        App(self.username)


if __name__ == "__main__":
    pedidos_exemplo = {"Produto A": 2, "Produto B": 1}
    username_exemplo = "usuario_teste"
    Order(pedidos_exemplo, username_exemplo)
