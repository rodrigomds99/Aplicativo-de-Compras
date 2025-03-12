from customtkinter import *
from screen import Screen
from tkinter import messagebox
from database import Database


class RegisterProduct(Screen):
    def __init__(self):
        super().__init__()
        self.Labels()
        self.Entrys()
        self.Buttons()

        self.sql = Database()
        self.screensize = "800x600"
        self.size()
        self.run()

    def Labels(self):
        self.nameLabel = CTkLabel(master=self.screen, text="Produto", font=self.text)
        self.nameLabel.place(x=250, y=170)

        self.priceLabel = CTkLabel(master=self.screen, text="Preço", font=self.text)
        self.priceLabel.place(x=250, y=250)

    def Entrys(self):
        self.name = CTkEntry(master=self.screen, width=300, placeholder_text="Digite o nome do produto...", font=self.text)
        self.name.place(x=250, y=200)

        self.price = CTkEntry(master=self.screen, width=300, placeholder_text="Digite o preço do produto...", font=self.text)
        self.price.place(x=250, y=280)

    def Buttons(self):
        self.register = CTkButton(master=self.screen, text="Cadastrar Produto", width=300, font=self.text, command=self.Register)
        self.register.place(x=250, y=400)

        self.back = CTkButton(master=self.screen, text="Voltar", width=300, font=self.text, fg_color="green", command=self.Back)
        self.back.place(x=250, y=450)

    def Back(self):
        self.screen.destroy()
        from appmanager import AppManager
        AppManager()

    def Register(self):
        self.nameP = self.name.get()
        self.priceP = self.price.get()

        try:
            # Verifica se algum campo está vazio
            if self.nameP == "" or self.priceP == "":
                messagebox.showerror(title="Estado do Cadastro", message="Por favor preencha todos os campos.")
            else:
                # Verifica se o nome de usuário já existe no banco de dados
                self.sql.cursor.execute("SELECT * FROM Produtos WHERE Name = ?", (self.nameP,))
                self.verify = self.sql.cursor.fetchone()

                if self.verify:
                    messagebox.showerror(title="Estado do Cadastro", message="Produto já existe.")
                else:
                    # Insere o novo usuário no banco de dados
                    self.sql.cursor.execute("""
                                            INSERT INTO Produtos (Name, Price) VALUES (?, ?)""",
                                            (self.nameP, self.priceP))
                    self.sql.conn.commit()  # Confirma a inserção no banco de dados
                    messagebox.showinfo(title="Estado do Cadastro", message="Produto Cadastrado com Sucesso!!")
        except Exception as e:
            # Exibe uma mensagem de erro caso ocorra uma exceção
            messagebox.showerror(title="Estado do Cadastro", message=f"Erro, por favor tente novamente.\n{str(e)}")


if __name__ == "__main__":
    RegisterProduct()
