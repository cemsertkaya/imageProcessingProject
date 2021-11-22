from tkinter import *
from tkinter.ttk import *

import skimage.exposure

from ViewUtil import ViewUtil
from tkinter import *
from tkinter.ttk import *
from tkinter import Label, Tk
from PIL import Image, ImageTk
from skimage import filters, color, img_as_float, io
import tkinter.filedialog as fd
import numpy as np

class Intensity(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.selectedImage = None
        self.title("Intensity")
        self.geometry("1000x1000")

        self.inputImageFrame = Frame(self)
        self.inputImageFrame.pack(side=LEFT)

        openImage = Button(self.inputImageFrame, text="Select Image", command=self.buttonClick)
        openImage.pack(padx=200, pady=100)

        self.buttonFrame = Frame(self)
        self.buttonFrame.pack(side=LEFT)

        self.createFilter("Rescale Intensity")  # multi-dimensional Gaussian filter.


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
        img = img_as_float(self.selectedImage)
        outputImage = Label(self.outputImageFrame, image= skimage.exposure.rescale_intensity(img))
        outputImage.pack()
        self.mainloop()

