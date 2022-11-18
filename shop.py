# import tkinter
from tkinter import *

# Creamos una ventana para las ventas
def ShopWindow():
    root = Tk(className='ShopWindow')
    # root = tkinter.Tk()
    root.title("Login")

    # Tamaño de la ventana
    # Hacer que la pantalla principal sea pantalla completa
    width = round(root.winfo_screenwidth())
    height = round(root.winfo_screenwidth())
    root.geometry(f"{width}x{height}")
    root.resizable(False, False)  # No se puede redimensionar

    # Label
    Label(root, text='Username').place(x=10, y=10)
    # tools.label(root, [50, 50], "Ingrese su nombre")

    root.mainloop()


if __name__ == "__main__":
    ShopWindow()
