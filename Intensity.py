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
        self.imageArray = None
        self.inputImage = None
        self.saveButton = None
        self.title("Intensity")
        self.geometry("1280x720")

        self.inputImageFrame = Frame(self)
        self.inputImageFrame.pack(side=LEFT)

        openImage = Button(self.inputImageFrame, text="Select Image", command=self.buttonClick)
        openImage.pack(padx=250, pady=100)

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

        rescaleButton = Button(self.buttonFrame, text="Rescale Intensity", command=self.filterClick)
        rescaleButton.pack(pady=20)

        self.outputImageFrame = Frame(self)
        self.outputImageFrame.pack(side=LEFT)

    def buttonClick(self):
        path = fd.askopenfilename(parent=self, filetypes=[("Image File", '.jpg'), ("Image File", '.png')])
        self.selectedImage = io.imread(path)
        tkImage = ImageTk.PhotoImage(Image.fromarray(self.selectedImage).resize(size=(400, 400)))

        if self.inputImage is not None:
            self.inputImage.destroy()
        self.inputImage = Label(self.inputImageFrame, image=tkImage)
        self.inputImage.pack()
        self.mainloop()

    def save(self):
        if self.imageArray is not None:
            filename = fd.asksaveasfile(parent=self, mode='w', defaultextension=".jpg")
            if not filename:
                return
            self.imageArray.save(filename)

    def filterClick(self):
        if self.selectedImage is not None:
            reshapedImage = np.array(self.selectedImage, dtype=np.uint8)

            replacedInput = self.inputLabel.get().replace('(', '').replace(')', '')
            inputTuple = (int(replacedInput.split(',')[0].strip()), int(replacedInput.split(',')[1].strip()))
            replacedOutput = self.outputLabel.get().replace('(', '').replace(')', '')
            outputTuple = (int(replacedOutput.split(',')[0].strip()), int(replacedOutput.split(',')[1].strip()))

            img = skimage.exposure.rescale_intensity(reshapedImage, in_range=inputTuple, out_range=outputTuple)
            print(inputTuple)
            self.imageArray = Image.fromarray(img.astype(np.uint8))
            tkImage = ImageTk.PhotoImage(self.imageArray.resize(size=(400, 400)))

            if self.saveButton is None:
                self.saveButton = Button(self.outputImageFrame, text="Kaydet", command=self.save)
                self.saveButton.pack(pady=100, padx=200)

            if self.outputImage is not None:
                self.outputImage.destroy()
            self.outputImage = Label(self.outputImageFrame,
                                     image=tkImage)
            self.outputImage.pack(padx=100)

            self.mainloop()
