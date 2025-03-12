from customtkinter import *
from screen import Screen


class AppManager(Screen):
    def __init__(self):
        super().__init__()
        self.Labels()
        self.Buttons()

        self.screensize = "450x400"
        self.size()
        self.run()

    def Labels(self):
        self.title = CTkLabel(master=self.screen, text="Selecione uma das Opções", font=("Arial", 24))
        self.title.pack(padx=20, pady=100)
    def Buttons(self):
        self.register = CTkButton(master=self.screen, text="Cadastrar Produtos", width=300, font=self.text, command=self.RegisterProducts)
        self.register.place(x=75, y=150)

        self.deleteProduct = CTkButton(master=self.screen, text="Remover Produtos", width=300, font=self.text, command=self.DeleteProducts)
        self.deleteProduct.place(x=75, y=200)

        self.deleteClient = CTkButton(master=self.screen, text="Remover Clientes", width=300, font=self.text, command=self.DeleteClients)
        self.deleteClient.place(x=75, y=250)

        self.back = CTkButton(master=self.screen, text="Voltar", width=300, font=self.text, fg_color="green", command=self.Back)
        self.back.place(x=75, y=300)

    def Back(self):
        self.screen.destroy()
        from login import Login
        Login()

    def DeleteProducts(self):
        self.screen.destroy()
        from deleteProduct import DeleteProduct
        DeleteProduct()

    def DeleteClients(self):
        self.screen.destroy()
        from deleteClient import DeleteClient
        DeleteClient()

    def RegisterProducts(self):
        self.screen.destroy()
        from registerProduct import RegisterProduct
        RegisterProduct()


if __name__ == "__main__":
    AppManager()