# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *
from tkinter import Label
from PIL import Image, ImageTk
from skimage import filters, color, io
import tkinter.filedialog as fd
import numpy as np


class ImageProcessingOperations(Toplevel):

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

        self.createFilter("Gaussians")  # multi-dimensional Gaussian filter.
        self.createFilter("Laplace")  # detecting edges in a coin image
        self.createFilter("Hessian")
        self.createFilter("Median")
        self.createFilter("Sato")

        self.createFilter("Meijering")
        self.createFilter("Unsharp Masking")
        self.createFilter("Rank Order")
        self.createFilter("Gabor")
        self.createFilter("Farid")

        self.outputImageFrame = Frame(self)
        self.outputImageFrame.pack(side=LEFT)

    def createFilter(self, text):
        filter = Button(self.buttonFrame, text=text, command=lambda: self.filterClick(text))
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
            self.saveButton.pack(pady=100)

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

    def filterClick(self, text):
        if self.selectedImage is not None:
            if text == "Gaussians":
                filteredImage = filters.gaussian(self.grayScaledImage, multichannel=False)
                self.imageArr = Image.fromarray((filteredImage * 255).astype(np.uint8))
                tkImage = ImageTk.PhotoImage(self.imageArr.resize(size=(400, 400)))
                self.printOutput(tkImage)
            elif text == "Laplace":
                filteredImage = filters.laplace(self.grayScaledImage)
                self.imageArr = Image.fromarray((filteredImage * 255).astype(np.uint8))
                tkImage = ImageTk.PhotoImage(self.imageArr.resize(size=(400, 400)))
                self.printOutput(tkImage)
            elif text == "Hessian":
                filteredImage = filters.hessian(self.grayScaledImage, mode='constant')
                self.imageArr = Image.fromarray((filteredImage * 255).astype(np.uint8))
                tkImage = ImageTk.PhotoImage(self.imageArr.resize(size=(400, 400)))
                self.printOutput(tkImage)
            elif text == "Median":
                filteredImage = filters.median(self.grayScaledImage)
                self.imageArr = Image.fromarray((filteredImage * 255).astype(np.uint8))
                tkImage = ImageTk.PhotoImage(self.imageArr.resize(size=(400, 400)))
                self.printOutput(tkImage)
            elif text == "Sato":
                filteredImage = filters.sato(self.grayScaledImage, mode='constant')
                self.imageArr = Image.fromarray((filteredImage * 255).astype(np.uint8))
                tkImage = ImageTk.PhotoImage(self.imageArr.resize(size=(400, 400)))
                self.printOutput(tkImage)
            elif text == "Meijering":
                filteredImage = filters.meijering(self.grayScaledImage)
                self.imageArr = Image.fromarray((filteredImage * 255).astype(np.uint8))
                tkImage = ImageTk.PhotoImage(self.imageArr.resize(size=(400, 400)))
                self.printOutput(tkImage)
            elif text == "Unsharp Masking":
                filteredImage = filters.unsharp_mask(self.grayScaledImage)
                self.imageArr = Image.fromarray((filteredImage * 255).astype(np.uint8))
                tkImage = ImageTk.PhotoImage(self.imageArr.resize(size=(400, 400)))
                self.printOutput(tkImage)
            elif text == "Rank Order":
                filteredImage = filters.rank_order(self.grayScaledImage)
                self.imageArr = Image.fromarray((filteredImage[0] * 255).astype(np.uint8))
                tkImage = ImageTk.PhotoImage(self.imageArr.resize(size=(400, 400)))
                self.printOutput(tkImage)
            elif text == "Gabor":
                filteredImage = filters.gabor(self.grayScaledImage, frequency=2.0)
                self.imageArr = Image.fromarray((filteredImage[0] * 255).astype(np.uint8))
                tkImage = ImageTk.PhotoImage(self.imageArr.resize(size=(400, 400)))
                self.printOutput(tkImage)
            elif text == "Farid":
                filteredImage = filters.farid(self.grayScaledImage)
                self.imageArr = Image.fromarray((filteredImage * 255).astype(np.uint8))
                tkImage = ImageTk.PhotoImage(self.imageArr.resize(size=(400, 400)))
                self.printOutput(tkImage)
