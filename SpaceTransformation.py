from tkinter import *
from tkinter.ttk import *
from tkinter import Label
from PIL import Image, ImageTk
from skimage import color, io, transform
import tkinter.filedialog as fd
import numpy as np

from ViewUtil import ViewUtil


class SpaceTransformation(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Space Transformation")
        self.geometry(ViewUtil.pageSizes)
        self.selectedImage = None
        self.outputImage = None
        self.grayScaledImage = None
        self.geometry("1280x720")

        self.inputImageFrame = Frame(self)
        self.inputImageFrame.pack(side=LEFT)

        openImage = Button(self.inputImageFrame, text="Select Image", command=self.buttonClick)
        openImage.pack(padx=200, pady=100)

        self.buttonFrame = Frame(self)
        self.buttonFrame.pack(side=LEFT)

        self.createFilter("Downscale Local Mean")
        self.createFilter("Swirl")
        self.createFilter("Rotate")
        self.createFilter("Resize")
        self.createFilter("Rescale")

        self.outputImageFrame = Frame(self)
        self.outputImageFrame.pack(side=LEFT)
        invisText = Label(self.outputImageFrame, text=" ")
        invisText.pack(pady=100, padx=200)

    def buttonClick(self):
        path = fd.askopenfilename(parent=self, filetypes=[("Image File", '.jpg'), ("Image File", '.png')])
        self.selectedImage = io.imread(path)
        self.grayScaledImage = color.rgb2gray(self.selectedImage)
        tkImage = ImageTk.PhotoImage(Image.fromarray(self.selectedImage).resize(size=(400, 400)))
        myvar = Label(self.inputImageFrame, image=tkImage)
        myvar.pack()
        self.mainloop()

    def createFilter(self, text):
        filter = Button(self.buttonFrame, text=text, command=lambda: self.filterClick(text))
        filter.pack(pady=20)

    def printOutput(self, tkImage):
        if self.outputImage is not None:
            self.outputImage.destroy()
        self.outputImage = Label(self.outputImageFrame, image=tkImage)
        self.outputImage.pack()
        self.mainloop()

    def filterClick(self, text):
        if self.selectedImage is not None:
            if text == "Downscale Local Mean":
                filteredImage = transform.downscale_local_mean(self.grayScaledImage, (4, 3))
                imageArr = Image.fromarray((filteredImage * 255).astype(np.uint8))
                tkImage = ImageTk.PhotoImage(imageArr)
                self.printOutput(tkImage)
            elif text == "Swirl":
                filteredImage = transform.swirl(self.grayScaledImage, rotation=0, strength=60, radius=120)
                imageArr = Image.fromarray((filteredImage * 255).astype(np.uint8)).resize(size=(400, 400))
                tkImage = ImageTk.PhotoImage(imageArr)
                self.printOutput(tkImage)
            elif text == "Rotate":
                filteredImage = transform.rotate(self.grayScaledImage, angle=45)
                imageArr = Image.fromarray((filteredImage * 255).astype(np.uint8)).resize(size=(400, 400))
                tkImage = ImageTk.PhotoImage(imageArr)
                self.printOutput(tkImage)
            elif text == "Resize":
                filteredImage = transform.resize(self.grayScaledImage,
                                                 (self.grayScaledImage.shape[0] // 2, self.grayScaledImage.shape[1] // 2))
                imageArr = Image.fromarray((filteredImage * 255).astype(np.uint8))
                tkImage = ImageTk.PhotoImage(imageArr)
                self.printOutput(tkImage)
            elif text == "Rescale":
                filteredImage = transform.rescale(self.grayScaledImage, 0.25)
                imageArr = Image.fromarray((filteredImage * 255).astype(np.uint8)).resize(size=(400, 400))
                tkImage = ImageTk.PhotoImage(imageArr)
                self.printOutput(tkImage)
