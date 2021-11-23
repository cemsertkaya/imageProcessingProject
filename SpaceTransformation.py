from tkinter import *
from tkinter.ttk import *

from ViewUtil import ViewUtil
class SpaceTransformation(Toplevel):
     
    def __init__(self, master = None):
         
        super().__init__(master = master)
        self.title("Space Transformation")
        self.geometry(ViewUtil.pageSizes)
        self.selectedImage = None
        self.geometry("1000x1000")
        label.pack()