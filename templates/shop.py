from tkinter import *

# Creamos una ventana para las ventas
def shopWindow():
    root = Tk(className='shopWindow')
    root.title("Login")

    # Tamaño de la ventana
    # Hacer que la pantalla principal sea pantalla completa
    width = round(root.winfo_screenwidth())
    height = round(root.winfo_screenwidth())
    root.geometry(f"{width}x{height}")
    root.resizable(False, False)  # No se puede redimensionar

    # Label
    Label(root, text='Bienvenid@ a la página de ventas').place(x=10, y=10)

    root.mainloop()


if __name__ == "__main__":
    shopWindow()
