from tkinter import *
from tkinter.ttk import *
from tkinter import Label
from PIL import Image, ImageTk
from skimage import io, morphology, color
from skimage.morphology import square
import tkinter.filedialog as fd
import numpy as np


class Morphology(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.selectedImage = None
        self.outputImage = None
        self.grayScaledImage = None
        self.saveButton = None
        self.imageArr = None
        self.inputImage = None
        self.title("Image Processing Operations")
        self.geometry("1280x720")

        self.inputImageFrame = Frame(self)
        self.inputImageFrame.pack(side=LEFT)

        openImage = Button(self.inputImageFrame, text="Select Image", command=self.buttonClick)
        openImage.pack(padx=250, pady=100)

        self.buttonFrame = Frame(self)
        self.buttonFrame.pack(side=LEFT)

        self.createFilter(
            "Erosion")  # Morphological erosion removes islands and small objects so that only substantive objects remain.
        self.createFilter("Dilation")
        self.createFilter("Closing")
        self.createFilter("Opening")
        self.createFilter("White Tophat")
        self.createFilter("Area Opening")
        self.createFilter("Area Closing")
        self.createFilter("Thin")
        self.createFilter("Skeletonize")
        self.createFilter("Max Tree")

        self.outputImageFrame = Frame(self)
        self.outputImageFrame.pack(side=LEFT)

    def createFilter(self, text):
        filter = Button(self.buttonFrame, text=text, command=lambda: self.morphClick(text))
        filter.pack(pady=20)

    def buttonClick(self):
        path = fd.askopenfilename(parent=self, filetypes=[("Image File", '.jpg'), ("Image File", '.png')])
        self.selectedImage = io.imread(path)
        self.grayScaledImage = color.rgb2gray(self.selectedImage)
        tkImage = ImageTk.PhotoImage(Image.fromarray(self.selectedImage).resize(size=(400, 400)))

        if self.inputImage is not None:
            self.inputImage.destroy()
        self.inputImage = Label(self.inputImageFrame, image=tkImage)
        self.inputImage.pack()
        self.mainloop()

    def printOutput(self, tkImage):
        if self.saveButton is None:
            self.saveButton = Button(self.outputImageFrame, text="Kaydet", command=self.save)
            self.saveButton.pack(pady=100, padx=200)

        if self.outputImage is not None:
            self.outputImage.destroy()
        self.outputImage = Label(self.outputImageFrame, image=tkImage)
        self.outputImage.pack(padx=100)
        self.mainloop()

    def save(self):
        if self.imageArr is not None:
            filename = fd.asksaveasfile(parent=self, mode='w', defaultextension=".jpg")
            if not filename:
                return
            self.imageArr.save(filename)

    def morphClick(self, text):
        if self.selectedImage is not None:
            if text == "Erosion":
                result = morphology.erosion(self.grayScaledImage)
                self.imageArr = Image.fromarray((result * 255).astype(np.uint8))
                tkImage = ImageTk.PhotoImage(self.imageArr.resize(size=(400, 400)))
                self.printOutput(tkImage)
            elif text == "Dilation":
                result = morphology.dilation(self.grayScaledImage)
                self.imageArr = Image.fromarray((result * 255).astype(np.uint8))
                tkImage = ImageTk.PhotoImage(self.imageArr.resize(size=(400, 400)))
                self.printOutput(tkImage)
            elif text == "Closing":
                result = morphology.closing(self.grayScaledImage)
                self.imageArr = Image.fromarray((result * 255).astype(np.uint8))
                tkImage = ImageTk.PhotoImage(self.imageArr.resize(size=(400, 400)))
                self.printOutput(tkImage)
            elif text == "Opening":
                result = morphology.opening(self.grayScaledImage)
                self.imageArr = Image.fromarray((result * 255).astype(np.uint8))
                tkImage = ImageTk.PhotoImage(self.imageArr.resize(size=(400, 400)))
                self.printOutput(tkImage)
            elif text == "White Tophat":
                result = morphology.white_tophat(self.grayScaledImage, square(5))
                self.imageArr = Image.fromarray((result * 255).astype(np.uint8))
                tkImage = ImageTk.PhotoImage(self.imageArr.resize(size=(400, 400)))
                self.printOutput(tkImage)
            elif text == "Area Opening":
                result = morphology.area_opening(self.grayScaledImage)
                self.imageArr = Image.fromarray((result * 255).astype(np.uint8))
                tkImage = ImageTk.PhotoImage(self.imageArr.resize(size=(400, 400)))
                self.printOutput(tkImage)
            elif text == "Area Closing":
                result = morphology.area_closing(self.grayScaledImage)
                self.imageArr = Image.fromarray((result * 255).astype(np.uint8))
                tkImage = ImageTk.PhotoImage(self.imageArr.resize(size=(400, 400)))
                self.printOutput(tkImage)
            elif text == "Thin":
                result = morphology.thin(self.grayScaledImage)
                self.imageArr = Image.fromarray(result)
                tkImage = ImageTk.PhotoImage(self.imageArr.resize(size=(400, 400)))
                self.printOutput(tkImage)
            elif text == "Skeletonize":
                result = morphology.skeletonize(self.grayScaledImage, method='lee')
                self.imageArr = Image.fromarray(result)
                tkImage = ImageTk.PhotoImage(self.imageArr.resize(size=(400, 400)))
                self.printOutput(tkImage)
            elif text == "Max Tree":
                result = morphology.max_tree(self.grayScaledImage)
                self.imageArr = Image.fromarray((result[0] * 255).astype(np.uint8))
                tkImage = ImageTk.PhotoImage(self.imageArr.resize(size=(400, 400)))
                self.printOutput(tkImage)
