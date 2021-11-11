from tkinter import *
from tkinter.ttk import *

from ViewUtil import ViewUtil
class SpaceTransformation(Toplevel):
     
    def __init__(self, master = None):
         
        super().__init__(master = master)
        self.title("New Window")
        self.geometry(ViewUtil.pageSizes)
        label = Label(self, text ="This is a new Window")
        label.pack()