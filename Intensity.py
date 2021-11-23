import skimage.exposure
from tkinter import *
from tkinter.ttk import *
from tkinter import Label
from PIL import Image, ImageTk
from skimage import color, io
import tkinter.filedialog as fd
import numpy as np


class Intensity(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.selectedImage = None
        self.outputImage = None
        self.grayScaledImage = None
        self.title("Intensity")
        self.geometry("1280x720")

        self.inputImageFrame = Frame(self)
        self.inputImageFrame.pack(side=LEFT)

        openImage = Button(self.inputImageFrame, text="Select Image", command=self.buttonClick)
        openImage.pack(padx=200, pady=100)

        self.buttonFrame = Frame(self)
        self.buttonFrame.pack(side=LEFT)

        inputText = Label(self.buttonFrame, text="İnput Intensity")
        inputText.pack(pady=10)
        self.inputLabel = Entry(self.buttonFrame)
        self.inputLabel.insert(END, '(0,127)')
        self.inputLabel.pack(pady=10)
        outputText = Label(self.buttonFrame, text="Output Intensity")
        outputText.pack(pady=10)
        self.outputLabel = Entry(self.buttonFrame)
        self.outputLabel.insert(END, '(0,255)')
        self.outputLabel.pack(pady=10)
        self.createFilter("Rescale Intensity")

        self.outputImageFrame = Frame(self)
        self.outputImageFrame.pack(side=LEFT)
        invisText = Label(self.outputImageFrame, text=" ")
        invisText.pack(pady=100, padx=200)

    def createFilter(self, text):
        filter = Button(self.buttonFrame, text=text, command=self.filterClick)
        filter.pack(pady=20)

    def buttonClick(self):
        path = fd.askopenfilename(parent=self, filetypes=[("Image File", '.jpg'), ("Image File", '.png')])
        self.selectedImage = io.imread(path)
        self.grayScaledImage = color.rgb2gray(self.selectedImage)
        tkImage = ImageTk.PhotoImage(Image.fromarray(self.selectedImage).resize(size=(400, 400)))
        myvar = Label(self.inputImageFrame, image=tkImage)
        myvar.pack()
        self.mainloop()

    def filterClick(self):
        if self.selectedImage is not None:
            reshapedImage = np.array(self.grayScaledImage, dtype=np.uint8)
            replacedInput = self.inputLabel.get().replace('(', '').replace(')', '')
            inputTuple = ((int)(replacedInput.split(',')[0].strip()), (int)(replacedInput.split(',')[1].strip()))
            replacedOutput = self.outputLabel.get().replace('(', '').replace(')', '')
            outputTuple = ((int)(replacedOutput.split(',')[0].strip()), (int)(replacedOutput.split(',')[1].strip()))
            img = skimage.exposure.rescale_intensity(reshapedImage, in_range=inputTuple, out_range=outputTuple)
            imageArray = Image.fromarray(img.astype(np.uint8)).resize(size=(400, 400))
            tkImage = ImageTk.PhotoImage(imageArray)
            if self.outputImage is not None:
                self.outputImage.destroy()
            self.outputImage = Label(self.outputImageFrame,
                                     image=tkImage)
            self.outputImage.pack()
            self.mainloop()
