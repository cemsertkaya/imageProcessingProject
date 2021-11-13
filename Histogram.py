from tkinter import *
from tkinter.ttk import *


class Histogram(Toplevel):
     
    def __init__(self, master = None):
         
        super().__init__(master = master)
        self.title("New Window")
        self.geometry("300x1000")
        label = Label(self, text ="This is a new Window")
        label.pack()