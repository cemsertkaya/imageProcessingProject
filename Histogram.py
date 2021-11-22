# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *
from tkinter import Label, Tk
from PIL import Image, ImageTk
from skimage import filters, color, img_as_float, io
from skimage.filters import gabor
import tkinter.filedialog as fd
import numpy as np
from skimage import data, exposure, img_as_float
from matplotlib import pyplot as plt # import pylot
from skimage.util import img_as_ubyte
from skimage import data
from skimage.exposure import histogram
from skimage.filters import threshold_otsu

class Histogram(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.selectedImage = None
        self.title("Histogram")
        self.geometry("1000x1000")
        self.inputImageFrame = Frame(self)
        self.inputImageFrame.pack(side=LEFT)
        openImage = Button(self.inputImageFrame, text="Select Image", command=self.buttonClick)
        openImage.pack(padx=200, pady=100)
        self.buttonFrame = Frame(self)
        self.buttonFrame.pack(side=LEFT)
        self.createFilter("Calculate Histogram")  # multi-dimensional Gaussian filter.

        self.outputImageFrame = Frame(self)
        self.outputImageFrame.pack(side=LEFT)
        invisText = Label(self.outputImageFrame, text=" ")
        invisText.pack(pady=100, padx=200)

    def createFilter(self, text):
        filter = Button(self.buttonFrame, text=text, command=lambda: self.showChartClick(text))
        filter.pack(pady=20)

    def buttonClick(self):
        path = fd.askopenfilename(parent=self, filetypes=[("Image File", '.jpg'), ("Image File", '.png')])
        self.selectedImage = Image.open(path)
        self.imageArray = np.array(self.selectedImage)
        tkImage = ImageTk.PhotoImage(self.selectedImage)
        myvar = Label(self.inputImageFrame, image=tkImage)
        myvar.pack()
        self.mainloop()

    def showChartClick(self, text):
        image = color.rgb2gray(self.imageArray)
        thresh = threshold_otsu(image)
        binary = image > thresh

        fig, axes = plt.subplots(ncols=3, figsize=(8, 2.5))
        ax = axes.ravel()
        ax[0] = plt.subplot(1, 3, 1)
        ax[1] = plt.subplot(1, 3, 2)
        ax[2] = plt.subplot(1, 3, 3, sharex=ax[0], sharey=ax[0])

        ax[0].imshow(image, cmap=plt.cm.gray)
        ax[0].set_title('Original')
        ax[0].axis('off')

        ax[1].hist(image.ravel(), bins=256)
        ax[1].set_title('Histogram')
        ax[1].axvline(thresh, color='r')

        ax[2].imshow(binary, cmap=plt.cm.gray)
        ax[2].set_title('Thresholded')
        ax[2].axis('off')

        plt.show()
        '''
        noisy_image = img_as_ubyte(self.imageArray)

        hist, hist_centers = histogram(color.rgb2gray(noisy_image))

        fig, ax = plt.subplots(ncols=2, figsize=(10, 5))

        ax[0].imshow(noisy_image, cmap=plt.cm.gray)
        ax[0].axis('off')

        ax[1].plot(hist_centers, hist, lw=2)
        ax[1].set_title('Gray-level histogram')

        plt.tight_layout()
        plt.show()
        '''
        #Grafik Gösterildi Eşikleme Yapılması Lazım

