# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *
from Histogram import Histogram
from ImageProcessingOperations import ImageProcessingOperations
from Intensity import Intensity
from Morphology import Morphology
from SpaceTransformation import SpaceTransformation

# creates a Tk() object
master = Tk()

# sets the geometry of
# main root window
master.geometry("1280x720")

label = Label(master, text="Görüntü İşleme Projemize Hoşgeldiniz")
label.pack(side=TOP, pady=10)

# a button widget which will
# open a new window on button click
btn1 = Button(master, text="Görüntü İyileştirme İşlemleri")
btn1.bind("<Button>", lambda e: ImageProcessingOperations(master))
btn1.pack(pady=30)

btn2 = Button(master, text="Histogram Görüntüleme ve Eşikleme")
btn2.bind("<Button>", lambda e: Histogram(master))
btn2.pack(pady=30)

btn3 = Button(master, text="Uzaysal Dönüşüm İşlemleri")
btn3.bind("<Button>", lambda e: SpaceTransformation(master))
btn3.pack(pady=30)

btn4 = Button(master, text="Yoğunluk Dönüşümü İşlemleri")
btn4.bind("<Button>", lambda e: Intensity(master))
btn4.pack(pady=30)

btn5 = Button(master, text="Morfolojik İşlemler")
btn5.bind("<Button>", lambda e: Morphology(master))
btn5.pack(pady=30)

btn6 = Button(master, text="Video İşleme")
btn6.bind("<Button>", lambda e: Histogram(master))
btn6.pack(pady=30)

# mainloop, runs infinitely
mainloop()
