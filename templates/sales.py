from tkinter import *
from tkinter import ttk
from tkinter import messagebox, ttk

from src.plugins.widgets import Widgets
from src.plugins.MainMenuFunction import MainFunctions

# PDF
import os.path
from src.plugins.PdfCreator import main


def borrar():
    areatexto.delete("1.0", "end")


def calcular():
    prenda = comboprenda.get()
    talla = combotalla.get()
    cantcad = txtcantidad.get()
    # cuadro de texto mostrando error por si no entra cada punto pedido por teclado

    if (len(prenda) == 0):
        messagebox.showinfo(
            message="Seleccione el tipo prenda!!", title="Error")
    elif (len(talla) == 0):
        messagebox.showinfo(message="Seleccione la talla!!", title="Error")
    elif (len(cantcad) == 0):
        messagebox.showinfo(
            message="Ingrese ingrese la cantidad de prendas!!", title="Error")
    else:
        # Aqui empezamos a ejecutar los descuentos del enunciado conjunto con el precio de cada prenda
        cant = int(cantcad)
        i = 0

        if ((prenda == "Jeans") and (talla == "S")):
            precio = 45.0
            pagar = precio*cant
            areatexto.insert(
                1.0, "\nLa compra por los jeans es : {}".format(pagar))
        elif ((prenda == "Jeans") and (talla == "M")):
            precio = 53.0
            pagar = precio*cant
            areatexto.insert(
                1.0, "\nLa compra por los jeans es : {}".format(pagar))
        elif ((prenda == "Jeans") and (talla == "L")):
            precio = 60.0
            pagar = precio * cant
            areatexto.insert(
                1.0, "\nLa compra por los jeans es : {}".format(pagar))
        elif ((prenda == "Jeans") and (talla == "XL")):
            precio = 70.0
            pagar = precio * cant
            areatexto.insert(
                1.0, "\nLa compra por los jeans es : {}".format(pagar))
        elif ((prenda == "Jeans") and (talla == "XXL")):
            precio = 85.0
            compra = precio*cant
            if cant >= 3:
                dscto = compra*0.08
                pagar = compra-dscto
                areatexto.insert(
                    1.0, "\nEl descuento en esta compra es : {}".format(dscto))
                areatexto.insert(
                    1.0, "\nLa compra por los jeans es : {}".format(pagar))
            elif cant < 3:
                areatexto.insert(
                    1.0, "\nLa compra por los jeans es : {}".format(compra))

        if ((prenda == "Faldas") and (talla == "S")):
            precio = 30.0
            compra = precio*cant
            if cant >= 3:
                dscto = cant*3
                pagar = compra-dscto
                areatexto.insert(
                    1.0, "\nLa compra por de faldas por mayor es : {}".format(pagar))
            elif cant < 3:
                areatexto.insert(
                    1.0, "\nEl importe a pagar de las faldas es : {}".format(compra))
        elif ((prenda == "Faldas") and (talla == "M")):
            precio = 35.0
            compra = precio*cant
            if cant >= 3:
                dscto = cant*3
                pagar = compra-dscto
                areatexto.insert(
                    1.0, "\nLa compra por de faldas por mayor es : {}".format(pagar))
            elif cant < 3:
                areatexto.insert(
                    1.0, "\nLEl importe a pagar de las faldas es : {}".format(compra))
        elif ((prenda == "Faldas") and (talla == "L")):
            precio = 42.0
            compra = precio*cant
            if cant >= 3:
                dscto = cant*3
                pagar = compra-dscto
                areatexto.insert(
                    1.0, "\nLa compra por de faldas por mayor es : {}".format(pagar))
            elif cant < 3:
                areatexto.insert(
                    1.0, "\nEl importe a pagar de las faldas es : {}".format(compra))
        elif ((prenda == "Faldas") and (talla == "XL")):
            precio = 48.0
            compra = precio*cant
            if cant >= 3:
                dscto = cant*3
                pagar = compra-dscto
                areatexto.insert(
                    1.0, "\nLa compra por de faldas por mayor es : {}".format(pagar))
            elif cant < 3:
                areatexto.insert(
                    1.0, "\nEl importe a pagar de las faldas es : {}".format(compra))
        elif ((prenda == "Faldas") and (talla == "XXL")):
            precio = 53.0
            compra = precio*cant
            if cant >= 3:
                dscto = cant*3
                pagar = compra-dscto
                areatexto.insert(
                    1.0, "\nLa compra por de faldas por mayor es : {}".format(pagar))
            elif cant < 3:
                areatexto.insert(
                    1.0, "\nEl importe a pagar de las faldas es : {}".format(compra))
        if ((prenda == "Shorts") and (talla == "S")):
            precio = 33.0
            compra = precio*cant
            if compra > 150:
                dscto = compra*0.06
                pagar = compra-dscto
                areatexto.insert(
                    1.0, "\nEl importe a pagar por los shorts es : {}".format(pagar))
            elif compra <= 150:
                areatexto.insert(
                    1.0, "\nEl importe a pagar por los shorts es : {}".format(compra))
        elif ((prenda == "Shorts") and (talla == "M")):
            precio = 38.0
            compra = precio*cant
            areatexto.insert(
                1.0, "\nEl importe a pagar por los shorts es : {}".format(compra))
        elif ((prenda == "Shorts") and (talla == "L")):
            precio = 45.0
            compra = precio*cant
            areatexto.insert(
                1.0, "\nEl importe a pagar por los shorts es : {}".format(compra))
        elif ((prenda == "Shorts") and (talla == "XL")):
            precio = 55.0
            compra = precio*cant
            areatexto.insert(
                1.0, "\nEl importe a pagar por los shorts es : {}".format(compra))
        elif ((prenda == "Shorts") and (talla == "XXL")):
            precio = 60.0
            compra = precio*cant
            areatexto.insert(
                1.0, "\nEl importe a pagar por los shorts es : {}".format(compra))
        if ((prenda == "Tops") and (talla == "S")):
            precio = 25.0
            compra = precio*cant
            if cant/2 == 0:
                canti = cant/2
                compra = precio*canti
                areatexto.insert(
                    1.0, "\nEl importe a pagar por los shorts es : {}".format(compra))
        elif ((prenda == "Tops") and (talla == "M")):
            precio = 28.0
            compra = precio*cant
            areatexto.insert(
                1.0, "\nEl importe a pagar por los shorts es : {}".format(compra))
        elif ((prenda == "Tops") and (talla == "L")):
            precio = 33.0
            compra = precio*cant
            areatexto.insert(
                1.0, "\nEl importe a pagar por los shorts es : {}".format(compra))
        elif ((prenda == "Tops") and (talla == "XL")):
            precio = 38.0
            compra = precio*cant
            areatexto.insert(
                1.0, "\nEl importe a pagar por los shorts es : {}".format(compra))
        elif ((prenda == "Tops") and (talla == "XXL")):
            precio = 45.0
            compra = precio*cant
            areatexto.insert(
                1.0, "\nEl importe a pagar por los shorts es : {}".format(compra))
        if ((prenda == "Casacas") and (talla == "S")):
            precio = 68.0
            compra = precio*cant
            if cant > 3:
                dscto = compra*0.05
                pagar = compra-dscto
                areatexto.insert(
                    1.0, "\nEl importe a pagar por los shorts es : {}".format(pagar))
            elif cant <= 3:
                areatexto.insert(
                    1.0, "\nEl importe a pagar por los shorts es : {}".format(compra))
        elif ((prenda == "Casacas") and (talla == "M")):
            precio = 73.0
            compra = precio*cant
            if cant > 3:
                dscto = compra*0.05
                pagar = compra-dscto
                areatexto.insert(
                    1.0, "\nEl importe a pagar por los shorts es : {}".format(pagar))
            elif cant <= 3:
                areatexto.insert(
                    1.0, "\nEl importe a pagar por los shorts es : {}".format(compra))
        elif ((prenda == "Casacas") and (talla == "L")):
            precio = 80.0
            compra = precio*cant
            if cant > 3:
                dscto = compra*0.05
                pagar = compra-dscto
                areatexto.insert(
                    1.0, "\nEl importe a pagar por los shorts es : {}".format(pagar))
            elif cant <= 3:
                areatexto.insert(
                    1.0, "\nEl importe a pagar por los shorts es : {}".format(compra))
        elif ((prenda == "Casacas") and (talla == "XL")):
            precio = 90.0
            compra = precio*cant
            if cant > 3:
                dscto = compra*0.05
                pagar = compra-dscto
                areatexto.insert(
                    1.0, "\nEl importe a pagar por los shorts es : {}".format(pagar))
            elif cant <= 3:
                areatexto.insert(
                    1.0, "\nEl importe a pagar por los shorts es : {}".format(compra))
        elif ((prenda == "Casacas") and (talla == "XXL")):
            precio = 105.0
            compra = precio*cant
            if cant > 3:
                dscto = compra*0.05
                pagar = compra-dscto
                areatexto.insert(
                    1.0, "\nEl importe a pagar por los shorts es : {}".format(pagar))
            elif cant <= 3:
                areatexto.insert(
                    1.0, "\nEl importe a pagar por los shorts es : {}".format(compra))
        if ((compra > 400) and (pagar > 400)):
            areatexto.insert(
                1.0, "\nPor una compra mayor a S/.400 usted acaba de recibir un vale de descuento del 10% en su siguiente compra : {}")
    generarProductos()


def generarProductos():
    name = txtnombre.get()
    prenda = comboprenda.get()
    prenda = comboprenda.get()
    talla = combotalla.get()
    cantidad = txtcantidad.get()
    textArea = areatexto.get("1.0", "end-1c")

    home = os.getcwd()
    routeFile = f"{home}/src/products/venta.txt"
    with open(routeFile, "w") as file:
        # Guardamos la contraseña en el archivo
        file.write(f"{name}|{prenda}|{talla}|{cantidad}|{textArea}")
        file.close()


def salesWindow():
    # Global variables
    global comboprenda
    global areatexto
    global combotalla
    global txtcantidad
    global txtnombre

    root = Tk(className='salesWindow')
    # Creamos un objeto de la clase Widgets
    widgets = Widgets(root)
    functions = MainFunctions(root)
    root.title("Ventas Forma 2")

    # Tamaño de la ventana
    root.geometry("950x650")
    root.resizable(False, False)  # No se puede redimensionar

    root.configure(background='pink')

    lblnombre = Label(root, text="Ingrese su nombre")
    lblnombre.place(x=50, y=50)
    lbldni = Label(root, text="Ingrese el numero de DNI:")
    lbldni.place(x=50, y=80)
    lblcomboprenda = Label(root, text="Elige el tipo de prenda:")
    lblcomboprenda.place(x=50, y=110)
    lblcombotalla = Label(root, text="Elige la talla:")
    lblcombotalla.place(x=50, y=140)
    lblcantidad = Label(root, text="Ingrese la cantidad de prendas:")
    lblcantidad.place(x=50, y=170)
    txtnombre = Entry(root, width=20)
    txtnombre.place(x=230, y=50)
    txtdni = Entry(root, width=20)
    txtdni.place(x=230, y=80)
    comboprenda = ttk.Combobox(state="readonly", values=[
                               "Jeans", "Faldas", "Shorts", "Tops", "Casacas"])
    comboprenda.place(x=230, y=110)
    combotalla = ttk.Combobox(state="readonly", values=[
                              "S", "M", "L", "XL", "XXL"])
    combotalla.place(x=230, y=140)
    txtcantidad = Entry(root, width=20)
    txtcantidad.place(x=230, y=170)

    areatexto = Text(root)
    areatexto.config(width=40, height=10)
    areatexto.place(x=50, y=250)

    btnprocesar = Button(root, text="Ejecutar", command=calcular)
    btnprocesar.place(x=400, y=50)

    btnborrar = Button(root, text="Borrar", command=borrar)
    btnborrar.place(x=400, y=80)

    btnborrar = Button(root, text="Crear PDF", command=main)
    btnborrar.place(x=500, y=180)

    root.mainloop()


if __name__ == "__main__":
    salesWindow()
