from tkinter import *
from tkinter import ttk
import os

class Widgets:
    def __init__(self, root):
        self.master = root
        # Ruta del proyecto
        self.home = os.getcwd()
        # Fuente de los widgets
        self.fontOptions = ('Helvetica', 14, 'normal')
        # ttk color theme
        # Define the style for combobox widget
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", fieldbackground="orange",
                        background="white")

    def label(self, text):
        label = Label(text=text)
        return label

    def comboBox(self, options):
        combo = ttk.Combobox(
            state="readonly",
            values=options,
        )
        combo.set("Seleccione una opción")
        return combo

    def button(self, text, callback):
        button = Button(self.master, text=text, font=self.fontOptions,
                        bg="black", fg="white", command=callback)
        return button

    def scale(self, min, max, orient):
        scale = Scale(self.master, from_=min, to=max,
                      bg="#fea75d", fg="black", orient=orient)
        return scale

    def createAMainMenu(self, windowName, windowFunct, closeFunct):
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label=windowName, command=windowFunct)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=closeFunct)
        menubar.add_cascade(label="Archivos", menu=filemenu)

        self.master.config(menu=menubar)

    # def setBackgroundImage(self, imageRoute):
    #     print(imageRoute)
    #     imagen = PhotoImage(file=imageRoute)
    #     background = Label(image=imagen)
    #     background.place(x=0, y=0, relwidth=1, relheight=1)
    #     return background
