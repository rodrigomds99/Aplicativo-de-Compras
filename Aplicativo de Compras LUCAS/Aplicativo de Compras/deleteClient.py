from customtkinter import *
from screen import Screen
from tkinter import messagebox
from database import Database


class DeleteClient(Screen):
    def __init__(self):
        super().__init__()
        self.sql = Database()
        self.Labels()
        self.Entrys()
        self.Buttons()

        self.screensize = "800x600"
        self.size()
        self.run()

    def Labels(self):
        self.label = CTkLabel(master=self.screen, text="Digite o Nome do Cliente",font=self.text)
        self.label.place(x=250, y=170)

    def Entrys(self):
        self.client = CTkEntry(master=self.screen, placeholder_text="Digite o nome do cliente...", width=300, font=self.text)
        self.client.place(x=250, y=200)

    def Buttons(self):
        self.delete = CTkButton(master=self.screen, text="Remover Cliente", width=300, font=self.text, fg_color="red", command=self.DeleteClients)
        self.delete.place(x=250, y=400)

        self.back = CTkButton(master=self.screen, text="Voltar", width=300, font=self.text, fg_color="green", command=self.Back)
        self.back.place(x=250, y=450)

    def DeleteClients(self):
        self.name = self.client.get()

        self.sql.cursor.execute("SELECT * FROM Clientes WHERE Username = ?", (self.name,))
        self.verify = self.sql.cursor.fetchone()

        if self.name == "":
            messagebox.showerror(title="Estado da Operação", message="Por favor preencha o campo.")

        elif self.verify is not None:
            self.sql.DeleteClient(self.name)
            messagebox.showinfo(title="Estado da Operação", message="Usuário Removido com Sucesso!!")
        else:
            messagebox.showerror(title="Estado da Operação", message="Usuário não consta no sistema.")

    def Back(self):
        self.screen.destroy()
        from appmanager import AppManager
        AppManager()


if __name__ == "__main__":
    DeleteClient()