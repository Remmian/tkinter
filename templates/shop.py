from tkinter import *
# from tkinter import messagebox
from tkinter import ttk
from src.model.clothes import clothesAvailable, sizesAvailable
from src.plugins.widgets import Widgets

# Variables necesarias
count = 0


def display_selection():
    global count
    # Obtenemos los datos de los combobox y scale
    ropa = typeOfClothing.get()
    size = sizeOfClothing.get()
    cantidad = quantity.get()

    tree.insert(parent='', index='end', iid=count,
                text=f'{count}', values=(ropa, size, cantidad))

    count += 1
    # tree.insert(parent='', index=0, iid=0, text='',
    #             values=(ropa, size, cantidad))


# Creamos una ventana para las ventas
def shopWindow():
    # Variables globales
    global typeOfClothing
    global sizeOfClothing
    global quantity
    global tree

    root = Tk(className='shopWindow')
    # Creamos un objeto de la clase Widgets
    widgets = Widgets(root)
    root.title("Ventas")

    # Agregamos un background image
    imagen = PhotoImage(file=f"{widgets.home}/src/img/sales.png")
    background = Label(image=imagen)
    background.place(x=0, y=0, relwidth=1, relheight=1)

    # Tamaño de la ventana
    root.geometry("950x650")
    root.resizable(False, False)  # No se puede redimensionar

    # Creamos un combobox para las prendas
    typeOfClothing = widgets.comboBox(clothesAvailable)
    typeOfClothing.place(x=137, y=233)

    # Creamos un combobox para el tamaño de prendas
    sizeOfClothing = widgets.comboBox(sizesAvailable)
    sizeOfClothing.place(x=137, y=325)

    # widget para seleccionar la cantidad
    # quantity = Scale(root, from_=1, to=10,
    #                  orient=HORIZONTAL)

    quantity = widgets.scale(1, 20, HORIZONTAL)
    quantity.place(x=137, y=423, width=200, height=40)

    tree = ttk.Treeview(root)
    tree['columns'] = ('Ropa', 'Talla', 'Cantidad')
    tree.column('#0', width=0, stretch=NO)
    tree.column('Ropa', anchor=CENTER, width=80)
    tree.column('Talla', anchor=CENTER, width=80)
    tree.column('Cantidad', anchor=CENTER, width=80)

    tree.heading('#0', text='', anchor=CENTER)
    tree.heading('Ropa', text='Ropa', anchor=CENTER)
    tree.heading('Talla', text='Talla', anchor=CENTER)
    tree.heading('Cantidad', text='Cantidad', anchor=CENTER)
    tree.place(x=459, y=121, width=450, height=480)

    button = widgets.button("Agregar Producto", display_selection)
    button.place(x=93, y=535)

    root.mainloop()


if __name__ == "__main__":
    shopWindow()
