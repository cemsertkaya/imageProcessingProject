# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *
from tkinter import Label
from PIL import Image, ImageTk
from skimage import color
import tkinter.filedialog as fd
import numpy as np
from matplotlib import pyplot as plt
from skimage.filters import threshold_otsu


class Histogram(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.selectedImage = None
        self.imageArray = None
        self.inputImage = None
        self.calculateButton = None
        self.title("Histogram")
        self.geometry("480x600")

        self.inputImageFrame = Frame(self)
        self.inputImageFrame.pack(side=LEFT)

        openImage = Button(self.inputImageFrame, text="Select Image", command=self.buttonClick)
        openImage.pack(padx=200)

    def buttonClick(self):
        path = fd.askopenfilename(parent=self, filetypes=[("Image File", '.jpg'), ("Image File", '.png')])
        self.selectedImage = Image.open(path).resize((400, 400))
        self.imageArray = np.array(self.selectedImage)
        tkImage = ImageTk.PhotoImage(self.selectedImage)

        if self.inputImage is not None:
            self.inputImage.destroy()
        self.inputImage = Label(self.inputImageFrame, image=tkImage)
        self.inputImage.pack(pady=50)

        if self.calculateButton is not None:
            self.calculateButton.destroy()
        self.calculateButton = Button(self.inputImageFrame, text="Calculate Histogram", command=self.showChartClick)
        self.calculateButton.pack()

        self.mainloop()

    def showChartClick(self):
        if self.selectedImage is not None:
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
