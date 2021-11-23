from tkinter import *
from tkinter.ttk import *
from tkinter import Label
from PIL import Image, ImageTk
from skimage import io, morphology, color
import tkinter.filedialog as fd
import numpy as np


class Morphology(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.selectedImage = None
        self.outputImage = None
        self.grayScaledImage = None
        self.title("Image Processing Operations")
        self.geometry("1280x720")

        self.inputImageFrame = Frame(self)
        self.inputImageFrame.pack(side=LEFT)

        openImage = Button(self.inputImageFrame, text="Select Image", command=self.buttonClick)
        openImage.pack(padx=200, pady=100)

        self.buttonFrame = Frame(self)
        self.buttonFrame.pack(side=LEFT)

        self.createFilter(
            "Erosion")  # Morphological erosion removes islands and small objects so that only substantive objects remain.
        self.createFilter("Dilation")
        self.createFilter("Closing")
        self.createFilter("Opening")
        self.createFilter("Reconstruction")
        self.createFilter("Area Opening")
        self.createFilter("Area Closing")
        self.createFilter("Thin")

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
        self.grayScaledImage = color.rgb2gray(self.selectedImage)
        tkImage = ImageTk.PhotoImage(Image.fromarray(self.selectedImage).resize(size=(400, 400)))
        myvar = Label(self.inputImageFrame, image=tkImage)
        myvar.pack()
        self.mainloop()

    def printOutput(self, tkImage):
        if self.outputImage is not None:
            self.outputImage.destroy()
        self.outputImage = Label(self.outputImageFrame, image=tkImage)
        self.outputImage.pack()
        self.mainloop()

    def morphClick(self, text):
        if self.selectedImage is not None:
            if text == "Erosion":
                result = morphology.erosion(self.grayScaledImage)
                imageArr = Image.fromarray((result * 255).astype(np.uint8)).resize(size=(400, 400))
                tkImage = ImageTk.PhotoImage(imageArr)
                self.printOutput(tkImage)
            elif text == "Dilation":
                result = morphology.dilation(self.grayScaledImage)
                imageArr = Image.fromarray((result * 255).astype(np.uint8)).resize(size=(400, 400))
                tkImage = ImageTk.PhotoImage(imageArr)
                self.printOutput(tkImage)
            elif text == "Closing":
                result = morphology.closing(self.grayScaledImage)
                imageArr = Image.fromarray((result * 255).astype(np.uint8)).resize(size=(400, 400))
                tkImage = ImageTk.PhotoImage(imageArr)
                self.printOutput(tkImage)
            elif text == "Opening":
                result = morphology.opening(self.grayScaledImage)
                imageArr = Image.fromarray((result * 255).astype(np.uint8)).resize(size=(400, 400))
                tkImage = ImageTk.PhotoImage(imageArr)
                self.printOutput(tkImage)
            elif text == "Reconstruction":
                result = morphology.reconstruction(self.grayScaledImage)
                imageArr = Image.fromarray((result * 255).astype(np.uint8)).resize(size=(400, 400))
                tkImage = ImageTk.PhotoImage(imageArr)
                self.printOutput(tkImage)
            elif text == "Area Opening":
                result = morphology.area_opening(self.grayScaledImage)  # trashhold can be added.
                imageArr = Image.fromarray((result * 255).astype(np.uint8)).resize(size=(400, 400))
                tkImage = ImageTk.PhotoImage(imageArr)
                self.printOutput(tkImage)
            elif text == "Area Closing":
                result = morphology.area_closing(self.grayScaledImage)  # trashhold can be added.
                imageArr = Image.fromarray((result * 255).astype(np.uint8)).resize(size=(400, 400))
                tkImage = ImageTk.PhotoImage(imageArr)
                self.printOutput(tkImage)
            elif text == "Thin":
                result = morphology.thin(self.grayScaledImage)  # trashhold can be added.
                imageArr = Image.fromarray(result).resize(size=(400, 400))
                tkImage = ImageTk.PhotoImage(imageArr)
                self.printOutput(tkImage)
