import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox, Canvas
from PIL import ImageTk, Image, UnidentifiedImageError


class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Ololo')
        self._frame = None
        self.switch_frame(HomePage)
        self.resizable(False, False)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class HomePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.uni_logo = Image.open('images/logo.png')
        self.uni_logo = ImageTk.PhotoImage(image=self.uni_logo)
        tk.Label(self, image=self.uni_logo, text="Ololo app").pack(pady=10, padx=20)
        tk.Label(self, text="Ololo app").pack()
        tk.Button(self, text='Click to start ->', command=lambda: master.switch_frame(WorkPage)).pack(pady=10)


class WorkPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.path = None
        self.image = None
        self.canvas = Canvas(self, width=350, height=350)
        self.config()

    def config(self):
        tk.Button(self, text="Open Image", command=self.open).pack(pady=10)
        tk.Button(self, text="Download").pack()
        self.canvas.pack(pady=20, padx=10)
        tk.Button(self, text='crop', command=self.crop).pack()
        tk.Button(self, text='filter', command=self.filter).pack()
        tk.Button(self, text='crop&filter', command=self.crop_filter).pack()

    def open(self):
        self.path = filedialog.askopenfilename()
        try:
            self.image = Image.open(self.path)
            self.image.thumbnail((350, 350))
            self.image = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 1, image=self.image, anchor='nw')
        except UnidentifiedImageError:
            messagebox.showerror(
                "Error", "Image not defined"
            )

    def crop(self):
        if not self.path:
            error_message()
        else:
            self.image = Image.open(self.path)

            w = self.image.width
            h = self.image.height
            n_w = 1080
            n_h = 1080

            l = (w - n_w) / 2
            t = (h - n_h) / 2
            r = (w + n_w) / 2
            b = (h + n_h) / 2

            self.image = self.image.crop((l, t, r, b))
            self.image.thumbnail((350, 350))
            self.image = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(1, 1, image=self.image, anchor='nw')

    def filter(self):
        if not self.path:
            error_message()
        else:
            self.image = Image.open(self.path)
            self.image = self.image.convert(mode='L')
            self.image.thumbnail((350, 350))
            self.image = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 1, image=self.image, anchor='nw')

    def crop_filter(self):
        if not self.path:
            error_message()
        else:
            self.image = Image.open(self.path)

            w = self.image.width
            h = self.image.height
            n_w = 1080
            n_h = 1080

            l = (w - n_w) / 2
            t = (h - n_h) / 2
            r = (w + n_w) / 2
            b = (h + n_h) / 2

            self.image = self.image.crop((l, t, r, b)).convert(mode="L")
            self.image.thumbnail((350, 350))
            self.image = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(1, 1, image=self.image, anchor='nw')


def error_message():
    messagebox.showerror("Error", "Please open Image")


if __name__ == "__main__":
    app = Main()
    app.mainloop()
