# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *
from tkinter import Label, Tk

import skimage.morphology
from PIL import Image, ImageTk
from skimage import filters, color, img_as_float, io
from skimage.filters import gabor
import tkinter.filedialog as fd
import numpy as np
import cv2

from ViewUtil import ViewUtil
class Morphology(Toplevel):

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

        self.createFilter("Erosion")  # Morphological erosion removes islands and small objects so that only substantive objects remain.
        self.createFilter("Dilation")
        self.createFilter("Closing")
        self.createFilter("Opening")
        self.createFilter("Reconstruction")
        self.createFilter("Area Opening")

        self.outputImageFrame = Frame(self)
        self.outputImageFrame.pack(side=LEFT)
        invisText = Label(self.outputImageFrame, text=" ")
        invisText.pack(pady=100, padx=200)

    def createFilter(self, text):
        filter = Button(self.buttonFrame, text=text, command=lambda: self.morphClick(text))
        filter.pack(pady=20)

    def buttonClick(self):
        path = fd.askopenfilename(parent=self, filetypes=[("Image File", '.jpg'), ("Image File", '.png')])
        self.selectedImage = io.imread(path)
        tkImage = ImageTk.PhotoImage(Image.fromarray(self.selectedImage))
        myvar = Label(self.inputImageFrame, image=tkImage)
        myvar.pack()
        self.mainloop()

    def morphClick(self, text):
        if text == "Erosion":
            kernel = np.ones((5, 5), np.uint8)
            result = skimage.morphology.erosion(self.selectedImage)
            imageArr = Image.fromarray((result * 255).astype(np.uint8))
            tkImage = ImageTk.PhotoImage(imageArr)
            outputImage = Label(self.outputImageFrame, image=tkImage)
            outputImage.pack()
            self.mainloop()
        elif text == "Dilation":
            kernel = np.ones((5, 5), np.uint8)
            result = skimage.morphology.dilate(self.selectedImage)
            imageArr = Image.fromarray((result * 255).astype(np.uint8))
            tkImage = ImageTk.PhotoImage(imageArr)
            outputImage = Label(self.outputImageFrame, image=tkImage)
            outputImage.pack()
            self.mainloop()
        elif text == "Closing":
            kernel = np.ones((5, 5), np.uint8)
            result = skimage.morphology.closing(self.selectedImage)
            imageArr = Image.fromarray((result * 255).astype(np.uint8))
            tkImage = ImageTk.PhotoImage(imageArr)
            outputImage = Label(self.outputImageFrame, image=tkImage)
            outputImage.pack()
            self.mainloop()
        elif text == "Opening":
            kernel = np.ones((5, 5), np.uint8)
            result = skimage.morphology.opening(self.selectedImage)
            imageArr = Image.fromarray((result * 255).astype(np.uint8))
            tkImage = ImageTk.PhotoImage(imageArr)
            outputImage = Label(self.outputImageFrame, image=tkImage)
            outputImage.pack()
            self.mainloop()
        elif text == "Reconstruction":
            kernel = np.ones((5, 5), np.uint8)
            result = skimage.morphology.reconstruction(self.selectedImage)
            imageArr = Image.fromarray((result * 255).astype(np.uint8))
            tkImage = ImageTk.PhotoImage(imageArr)
            outputImage = Label(self.outputImageFrame, image=tkImage)
            outputImage.pack()
            self.mainloop()
        elif text == "Area Opening":
            kernel = np.ones((5, 5), np.uint8)
            result = skimage.morphology.area_opening(self.selectedImage) #trashhold can be added.
            imageArr = Image.fromarray((result * 255).astype(np.uint8))
            tkImage = ImageTk.PhotoImage(imageArr)
            outputImage = Label(self.outputImageFrame, image=tkImage)
            outputImage.pack()
            self.mainloop()
