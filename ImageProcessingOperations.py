# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *
from tkinter import Label,Tk
from tkinter import Image, ImageTk
from tkinter import tkFileDialog

class ImageProcessingOperations(Toplevel):
     
    
    
    

    def __init__(self, master = None):
         
        super().__init__(master = master)
        self.title("Image Processing Operations")
        self.geometry("1000x1000")
        label = Label(self, text ="This is a new Window")
        label.pack()


        self.createFilter("Filter1",master)
        self.createFilter("Filter2",master)
        self.createFilter("Filter3",master)
        self.createFilter("Filter4",master)
        self.createFilter("Filter5",master)


        self.createFilter("Filter6",master)
        self.createFilter("Filter7",master)
        self.createFilter("Filter8",master)
        self.createFilter("Filter9",master)
        self.createFilter("Filter10",master)
        
        

    def createFilter(self,text, master = None):
        filter1 = Button(self,text = text,command= self.buttonClick)
        filter1.pack(pady = 20)
        

    
    def buttonClick():
        path=tkFileDialog.askopenfilename(filetypes=[("Image File",'.jpg')])
        im = Image.open(path)
        tkimage = ImageTk.PhotoImage(im)
        myvar=Label(root,image = tkimage)
        myvar.image = tkimage
        myvar.pack()