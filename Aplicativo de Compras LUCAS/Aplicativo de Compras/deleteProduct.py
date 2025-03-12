from customtkinter import *
from screen import Screen
from database import Database
from tkinter import messagebox


class DeleteProduct(Screen):
    def __init__(self):
        super().__init__()
        self.sql = Database()
        self.Labels()
        self.ComboBox()
        self.Buttons()

        self.screensize = "800x600"
        self.size()
        self.run()

    def Labels(self):
        self.label = CTkLabel(master=self.screen, text="Escolha o Produto",font=self.text)
        self.label.place(x=250, y=170)
    def ComboBox(self):
        self.productName = self.sql.ProductsNames()
        self.combo = CTkComboBox(master=self.screen, values=self.productName, width=300, dropdown_font=self.text, font=self.text)
        self.combo.place(x=250, y=200)

    def Buttons(self):
        self.delete = CTkButton(master=self.screen, text="Remover Produto", width=300, font=self.text, fg_color="red", command=self.DeleteSelectedProduct)
        self.delete.place(x=250, y=400)

        self.back = CTkButton(master=self.screen, text="Voltar", width=300, font=self.text, fg_color="green", command=self.Back)
        self.back.place(x=250, y=450)

    def DeleteSelectedProduct(self):
        self.product = self.combo.get()
        if self.product:
            self.sql.DeleteProduct(self.product)
            self.combo.set('')
            self.productName = self.sql.ProductsNames()
            self.combo.configure(values=self.productName)
            messagebox.showinfo(title="Produto Deletado", message="Produto Deletado com sucesso!!")

    def Back(self):
        self.screen.destroy()
        from appmanager import AppManager
        AppManager()


if __name__ == "__main__":
    DeleteProduct()
