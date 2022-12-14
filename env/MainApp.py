# Start by making a visual MainMenu class in env\MainMenu.py

import tkinter as tk


class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Main Menu")
        self.geometry("500x500")
        self.resizable(True, True)
        self.configure(background="black")
        self.mainloop()
        self.frame = tk.Frame(self)
        self.frame.pack()
