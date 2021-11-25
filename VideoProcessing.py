from tkinter import *
from tkinter.ttk import *
import cv2
import tkinter.filedialog as fd
import PIL


class VideoProcessing(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.saveLocation = None
        self.title("Image Processing Operations")
        self.geometry("1280x720")

        self.inputImageFrame = Frame(self)
        self.inputImageFrame.pack(side=LEFT)

        self.openImage = Button(self.inputImageFrame, text="Select Video", command=self.buttonClick)
        self.openImage.pack(padx=200, pady=100)

        self.buttonFrame = Frame(self)
        self.buttonFrame.pack(side=LEFT)

        self.outputImageFrame = Frame(self)
        self.outputImageFrame.pack(side=LEFT)

    def buttonClick(self):
        path = fd.askopenfilename(parent=self, filetypes=[("Video File", '.mp4'), ("Video File", '.mkv')])
        self.video = cv2.VideoCapture(path)

        self.width = self.video.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)

        self.canvas = Canvas(self.inputImageFrame, width=640, height=360)
        self.canvas.pack(padx=50)

        self.outputCanvas = Canvas(self.outputImageFrame, width=640, height=360)
        self.outputCanvas.pack(padx=50)

        self.pickSaveLocation()

        self.delay = 5
        self.update()
        self.openImage.destroy()
        self.mainloop()

    def save(self, frame):
        self.out.write(frame)

    def pickSaveLocation(self):
        if self.saveLocation is None:
            self.saveLocation = fd.asksaveasfile(parent=self, filetypes=[('All Files', '.*'), ('AVI', '.avi')],
                                                 mode="w",
                                                 defaultextension='.avi',
                                                 title="Üretilen videonun nereye kaydedileceğini seçiniz.")

            self.out = cv2.VideoWriter(self.saveLocation.name, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                                       self.video.get(5),
                                       (int(self.width),
                                        int(self.height)), False)

    def update(self):
        ret, frame = self.getFrame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame).resize(size=(480, 270)))
            self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (5, 5), 0)
            canny = cv2.Canny(blur, 10, 70)
            ret, mask = cv2.threshold(canny, 70, 255, cv2.THRESH_BINARY)

            self.outputVideo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(mask).resize(size=(480, 270)))

            self.outputCanvas.create_image(0, 0, image=self.outputVideo, anchor=NW)

            self.save(mask)

            self.inputImageFrame.after(self.delay, self.update)

        else:
            self.out.release()

    def getFrame(self):
        if self.video.isOpened():
            ret, frame = self.video.read()
            if ret:
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
