from customtkinter import *


class Screen:
    def __init__(self):
        self.screen = CTk()
        self.theme()
        self.screensize = "800x600"
        self.size()
        self.text = ("Arial", 20)

    def theme(self):
        set_appearance_mode("dark")
        set_default_color_theme("dark-blue")

    def size(self):
        self.screen.geometry(self.screensize)
        self.screen.resizable(False, False)

    def run(self):
        self.screen.mainloop()
