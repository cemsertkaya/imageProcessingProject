# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *
from tkinter import Label, Tk
from PIL import Image, ImageTk
from skimage import filters, color, img_as_float, io
from skimage.filters import gabor
import tkinter.filedialog as fd
import numpy as np



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

        self.createFilter("Gaussians") #multi-dimensional Gaussian filter.
        self.createFilter("Inverse") #detecting edges in a coin image
        self.createFilter("Hessian")
        self.createFilter("Frangi")
        self.createFilter("Sato")

        self.createFilter("Meijering")
        self.createFilter("Unsharp Masking")
        self.createFilter("Filter8 (Eksik)")
        self.createFilter("Filter9 (Eksik")
        self.createFilter("Filter10 (Eksik)")

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
        if text == "Gaussians":
            blurredImage = filters.gaussian(self.selectedImage)
            imageArr = Image.fromarray((blurredImage * 255).astype(np.uint8))
            tkImage = ImageTk.PhotoImage(imageArr)
            outputImage = Label(self.outputImageFrame, image=tkImage)
            outputImage.pack()
            self.mainloop()
        elif text == "Inverse":
            blurredImage = filters.inverse(self.selectedImage)
            imageArr = Image.fromarray((blurredImage * 255).astype(np.uint8))
            tkImage = ImageTk.PhotoImage(imageArr)
            outputImage = Label(self.outputImageFrame, image=tkImage)
            outputImage.pack()
            self.mainloop()
        elif text == "Hessian":
            blurredImage = filters.hessian(self.selectedImage)
            imageArr = Image.fromarray((blurredImage * 255).astype(np.uint8))
            tkImage = ImageTk.PhotoImage(imageArr)
            outputImage = Label(self.outputImageFrame, image=tkImage)
            outputImage.pack()
            self.mainloop()
        elif text == "Frangi":
            blurredImage = filters.frangi(self.selectedImage)
            imageArr = Image.fromarray((blurredImage * 255).astype(np.uint8))
            tkImage = ImageTk.PhotoImage(imageArr)
            outputImage = Label(self.outputImageFrame, image=tkImage)
            outputImage.pack()
            self.mainloop()
        elif text == "Sato":
            blurredImage = filters.sato(self.selectedImage)
            imageArr = Image.fromarray((blurredImage * 255).astype(np.uint8))
            tkImage = ImageTk.PhotoImage(imageArr)
            outputImage = Label(self.outputImageFrame, image=tkImage)
            outputImage.pack()
            self.mainloop()
        elif text == "Meijering":
            blurredImage = filters.meijering(self.selectedImage)
            imageArr = Image.fromarray((blurredImage * 255).astype(np.uint8))
            tkImage = ImageTk.PhotoImage(imageArr)
            outputImage = Label(self.outputImageFrame, image=tkImage)
            outputImage.pack()
            self.mainloop()
            pass
        elif text == "Unsharp Masking":
            blurredImage = filters.unsharp_mask(self.selectedImage)
            imageArr = Image.fromarray((blurredImage * 255).astype(np.uint8))
            tkImage = ImageTk.PhotoImage(imageArr)
            outputImage = Label(self.outputImageFrame, image=tkImage)
            outputImage.pack()
            self.mainloop()
        elif text == "Filter8":
            pass
        elif text == "Filter9":
            pass
        elif text == "Filter10":
            pass
