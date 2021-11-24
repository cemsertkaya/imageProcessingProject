from tkinter import *
from tkinter.ttk import *

from ViewUtil import ViewUtil
import cv2
import tkinter.filedialog as fd
import PIL


class VideoProcessing(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Image Processing Operations")
        self.geometry("1280x720")

        self.inputImageFrame = Frame(self)
        self.inputImageFrame.pack(side=LEFT)

        openImage = Button(self.inputImageFrame, text="Select Video", command=self.buttonClick)
        openImage.pack(padx=200, pady=100)

        self.buttonFrame = Frame(self)
        self.buttonFrame.pack(side=LEFT)

        self.outputImageFrame = Frame(self)
        self.outputImageFrame.pack(side=LEFT)
        invisText = Label(self.outputImageFrame, text=" ")
        invisText.pack(pady=100, padx=200)

    def buttonClick(self):
        path = fd.askopenfilename(parent=self, filetypes=[("Video File", '.mp4'), ("Video File", '.mkv')])
        self.video = cv2.VideoCapture(path)

        self.canvas = Canvas(self.inputImageFrame, width=640, height=360)
        self.canvas.pack()

        self.outputCanvas = Canvas(self.outputImageFrame, width=640, height=360)
        self.outputCanvas.pack()

        self.delay = 5
        self.update()
        self.mainloop()

    def update(self):
        ret, frame = self.getFrame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame).resize(size=(640, 360)))
            self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (5, 5), 0)
            canny = cv2.Canny(blur, 10, 70)
            ret, mask = cv2.threshold(canny, 70, 255, cv2.THRESH_BINARY)

            self.outputVideo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(mask).resize(size=(640, 360)))

            self.outputCanvas.create_image(0, 0, image=self.outputVideo, anchor=NW)

            self.inputImageFrame.after(self.delay, self.update)

    def getFrame(self):
        if self.video.isOpened():
            ret, frame = self.video.read()
            if ret:
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
