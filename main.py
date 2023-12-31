from customtkinter import *
from tkinter import messagebox
from pytube import YouTube
from PIL import Image
import threading


class GUI:
    def __init__(self):
        self.window = CTk()
        self.window.geometry('350x500')
        self.window.resizable(False, False)

        img = Image.open('youtube-logo-icon-png-11.png')
        self.image = CTkImage(img, size=(250, 250))
        self.imageLabel = CTkLabel(self.window, image=self.image, text="", height=100, width=100)
        self.t2 = threading.Thread(target=self.threadFun, args=())

        self.urlEntry = CTkEntry(self.window, width=300)
        self.downloadButton = CTkButton(self.window, text="Download", corner_radius=10, command=self.download, fg_color='black')
        self.progressBar = CTkProgressBar(self.window, width=300, height=10, fg_color='black', progress_color="green")
        self.progressBar._determinate_speed = 0.13
        self.progressBar.set(0)

        self.url = ""
        self.directory = ""

    def start(self):
        self.imageLabel.pack()
        self.urlEntry.pack()
        self.downloadButton.pack(pady=50)
        self.progressBar.pack()
        self.window.mainloop()

    def threadFun(self):
        self.progressBar.start()
        YouTube(self.url).streams.filter(progressive=True, file_extension='mp4').desc().first().download(self.directory,
                                                                                                         "Downloaded.mp4")
        self.progressBar.stop()
        messagebox.showinfo("Done!", "File has been downloaded!")
        self.progressBar.set(0)
        self.t2.should_abort_immediately = True

    def download(self):
        self.directory = filedialog.askdirectory()
        self.url = self.urlEntry.get()
        self.t2.start()


def main():
    gui = GUI()
    gui.start()


if __name__ == '__main__':
    main()
