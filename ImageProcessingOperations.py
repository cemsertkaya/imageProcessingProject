# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *
from tkinter import Label, Tk
from PIL import Image, ImageTk
from skimage import filters, color, img_as_float, io
import tkinter.filedialog as fd
import numpy as np
import color


class ImageProcessingOperations(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.selectedImage = None
        self.title("Image Processing Operations")
        self.geometry("1000x1000")

        self.inputImageFrame = Frame(self)
        self.inputImageFrame.pack(side=LEFT)

        openImage = Button(self.inputImageFrame, text="Select Image", command=self.buttonClick)
        openImage.pack(padx=200, pady=100)

        self.buttonFrame = Frame(self)
        self.buttonFrame.pack(side=LEFT)

        self.createFilter("Filter1")
        self.createFilter("Filter2")
        self.createFilter("Filter3")
        self.createFilter("Filter4")
        self.createFilter("Filter5")

        self.createFilter("Filter6")
        self.createFilter("Filter7")
        self.createFilter("Filter8")
        self.createFilter("Filter9")
        self.createFilter("Filter10")

        self.outputImageFrame = Frame(self)
        self.outputImageFrame.pack(side=LEFT)
        invisText = Label(self.outputImageFrame, text=" ")
        invisText.pack(pady=100, padx=200)

    def createFilter(self, text):
        filter = Button(self.buttonFrame, text=text, command=lambda: self.filterClick(text))
        filter.pack(pady=20)

    def buttonClick(self):
        path = fd.askopenfilename(parent=self, filetypes=[("Image File", '.jpg'), ("Image File", '.png')])
        self.selectedImage = io.imread(path)
        tkImage = ImageTk.PhotoImage(Image.fromarray(self.selectedImage))
        myvar = Label(self.inputImageFrame, image=tkImage)
        myvar.pack()
        self.mainloop()

    def filterClick(self, text):
        if text == "Filter1":
            blurredImage = filters.gaussian(self.selectedImage)
            imageArr = Image.fromarray((blurredImage * 255).astype(np.uint8))
            tkImage = ImageTk.PhotoImage(imageArr)
            outputImage = Label(self.outputImageFrame, image=tkImage)
            outputImage.pack()
            self.mainloop()
        elif text == "Filter2":
            pass
        elif text == "Filter3":
            pass
        elif text == "Filter4":
            pass
        elif text == "Filter5":
            pass
        elif text == "Filter6":
            pass
        elif text == "Filter7":
            pass
        elif text == "Filter8":
            pass
        elif text == "Filter9":
            pass
        elif text == "Filter10":
            pass
