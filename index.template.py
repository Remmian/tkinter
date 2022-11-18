import tkinter
from tkinter  import messagebox, ttk
#Realizaremos una ventana de usuario para el ´peprsonal de la tienda autorizado pueda entrar al programa
class Validacion:
    listausuarios=["Maria", "Piero", "Bryan","Jesus"]
    listaclaves=[123, 1234, 12345, 123456 ]

    def BuscarUsuario(self, usuario, clave):
        estado = False
        for i in range(0, 3):
            if ((self.listausuarios[i]==usuario) and (self.listaclaves[i]==clave)):
                estado = True
                break;
        return estado

    def ventanaPrincipal(self):
        def borrar():
            areatexto.delete("1.0", "end")

        def calcular():

            prenda=comboprenda.get()
            talla=combotalla.get()
            cantcad=txtcantidad.get()
            #cuadro de texto mostrando error por si no entra cada punto pedido por teclado

            if (len(prenda) == 0):
                messagebox.showinfo(message="Seleccione el tipo prenda!!", title="Error")
            elif (len(talla) == 0):
                messagebox.showinfo(message="Seleccione la talla!!", title="Error")
            elif (len(cantcad) == 0):
                messagebox.showinfo(message="Ingrese ingrese la cantidad de prendas!!", title="Error")
            else:
                #Aqui empezamos a ejecutar los descuentos del enunciado conjunto con el precio de cada prenda
                cant=int(cantcad)
                i=0

                if ((prenda=="Jeans") and (talla=="S")):
                    precio=45.0
                    pagar=precio*cant
                    areatexto.insert(1.0, "\nLa compra por los jeans es : {}".format(pagar))
                elif ((prenda=="Jeans") and (talla=="M")):
                    precio=53.0
                    pagar=precio*cant
                    areatexto.insert(1.0, "\nLa compra por los jeans es : {}".format(pagar))
                elif ((prenda=="Jeans") and (talla=="L")):
                    precio=60.0
                    pagar=precio * cant
                    areatexto.insert(1.0, "\nLa compra por los jeans es : {}".format(pagar))
                elif ((prenda=="Jeans") and (talla=="XL")):
                    precio=70.0
                    pagar=precio * cant
                    areatexto.insert(1.0, "\nLa compra por los jeans es : {}".format(pagar))
                elif ((prenda=="Jeans") and (talla=="XXL")):
                    precio=85.0
                    compra=precio*cant
                    if cant>=3:
                        dscto=compra*0.08
                        pagar=compra-dscto
                        areatexto.insert(1.0, "\nEl descuento en esta compra es : {}".format(dscto))
                        areatexto.insert(1.0, "\nLa compra por los jeans es : {}".format(pagar))
                    elif cant<3:
                        areatexto.insert(1.0, "\nLa compra por los jeans es : {}".format(compra))

                if ((prenda=="Faldas") and (talla=="S")):
                    precio=30.0
                    compra=precio*cant
                    if cant>=3:
                        dscto=cant*3
                        pagar=compra-dscto
                        areatexto.insert(1.0, "\nLa compra por de faldas por mayor es : {}".format(pagar))
                    elif cant<3:
                        areatexto.insert(1.0, "\nEl importe a pagar de las faldas es : {}".format(compra))
                elif ((prenda=="Faldas") and (talla=="M")):
                    precio=35.0
                    compra=precio*cant
                    if cant>=3:
                        dscto=cant*3
                        pagar=compra-dscto
                        areatexto.insert(1.0, "\nLa compra por de faldas por mayor es : {}".format(pagar))
                    elif cant<3:
                        areatexto.insert(1.0, "\nLEl importe a pagar de las faldas es : {}".format(compra))
                elif ((prenda=="Faldas") and (talla=="L")):
                    precio=42.0
                    compra=precio*cant
                    if cant>=3:
                        dscto=cant*3
                        pagar=compra-dscto
                        areatexto.insert(1.0, "\nLa compra por de faldas por mayor es : {}".format(pagar))
                    elif cant<3:
                        areatexto.insert(1.0, "\nEl importe a pagar de las faldas es : {}".format(compra))
                elif ((prenda=="Faldas") and (talla=="XL")):
                    precio=48.0
                    compra=precio*cant
                    if cant>=3:
                        dscto=cant*3
                        pagar=compra-dscto
                        areatexto.insert(1.0, "\nLa compra por de faldas por mayor es : {}".format(pagar))
                    elif cant<3:
                        areatexto.insert(1.0, "\nEl importe a pagar de las faldas es : {}".format(compra))
                elif ((prenda=="Faldas") and (talla=="XXL")):
                    precio=53.0
                    compra=precio*cant
                    if cant>=3:
                        dscto=cant*3
                        pagar=compra-dscto
                        areatexto.insert(1.0, "\nLa compra por de faldas por mayor es : {}".format(pagar))
                    elif cant<3:
                        areatexto.insert(1.0, "\nEl importe a pagar de las faldas es : {}".format(compra))
                if ((prenda=="Shorts") and (talla=="S")):
                    precio=33.0
                    compra=precio*cant
                    if compra>150:
                        dscto=compra*0.06
                        pagar=compra-dscto
                        areatexto.insert(1.0, "\nEl importe a pagar por los shorts es : {}".format(pagar))
                    elif compra<=150:
                        areatexto.insert(1.0, "\nEl importe a pagar por los shorts es : {}".format(compra))
                elif ((prenda=="Shorts") and (talla=="M")):
                    precio=38.0
                    compra=precio*cant
                    areatexto.insert(1.0, "\nEl importe a pagar por los shorts es : {}".format(compra))
                elif ((prenda=="Shorts") and (talla=="L")):
                    precio=45.0
                    compra=precio*cant
                    areatexto.insert(1.0, "\nEl importe a pagar por los shorts es : {}".format(compra))
                elif ((prenda=="Shorts") and (talla=="XL")):
                    precio=55.0
                    compra=precio*cant
                    areatexto.insert(1.0, "\nEl importe a pagar por los shorts es : {}".format(compra))
                elif ((prenda=="Shorts") and (talla=="XXL")):
                    precio=60.0
                    compra=precio*cant
                    areatexto.insert(1.0, "\nEl importe a pagar por los shorts es : {}".format(compra))
                if ((prenda=="Tops") and (talla=="S")):
                    precio=25.0
                    compra=precio*cant
                    if cant/2==0:
                        canti=cant/2
                        compra=precio*canti
                        areatexto.insert(1.0, "\nEl importe a pagar por los shorts es : {}".format(compra))
                elif ((prenda=="Tops") and (talla=="M")):
                    precio=28.0
                    compra=precio*cant
                    areatexto.insert(1.0, "\nEl importe a pagar por los shorts es : {}".format(compra))
                elif ((prenda=="Tops") and (talla=="L")):
                    precio=33.0
                    compra=precio*cant
                    areatexto.insert(1.0, "\nEl importe a pagar por los shorts es : {}".format(compra))
                elif ((prenda=="Tops") and (talla=="XL")):
                    precio=38.0
                    compra=precio*cant
                    areatexto.insert(1.0, "\nEl importe a pagar por los shorts es : {}".format(compra))
                elif ((prenda=="Tops") and (talla=="XXL")):
                    precio=45.0
                    compra=precio*cant
                    areatexto.insert(1.0, "\nEl importe a pagar por los shorts es : {}".format(compra))
                if ((prenda=="Casacas") and (talla=="S")):
                    precio=68.0
                    compra=precio*cant
                    if cant>3:
                        dscto=compra*0.05
                        pagar=compra-dscto
                        areatexto.insert(1.0, "\nEl importe a pagar por los shorts es : {}".format(pagar))
                    elif cant<=3:
                        areatexto.insert(1.0, "\nEl importe a pagar por los shorts es : {}".format(compra))
                elif ((prenda=="Casacas") and (talla=="M")):
                    precio=73.0
                    compra=precio*cant
                    if cant>3:
                        dscto=compra*0.05
                        pagar=compra-dscto
                        areatexto.insert(1.0, "\nEl importe a pagar por los shorts es : {}".format(pagar))
                    elif cant<=3:
                        areatexto.insert(1.0, "\nEl importe a pagar por los shorts es : {}".format(compra))
                elif ((prenda=="Casacas") and (talla=="L")):
                    precio=80.0
                    compra=precio*cant
                    if cant>3:
                        dscto=compra*0.05
                        pagar=compra-dscto
                        areatexto.insert(1.0, "\nEl importe a pagar por los shorts es : {}".format(pagar))
                    elif cant<=3:
                        areatexto.insert(1.0, "\nEl importe a pagar por los shorts es : {}".format(compra))
                elif ((prenda=="Casacas") and (talla=="XL")):
                    precio=90.0
                    compra=precio*cant
                    if cant>3:
                        dscto=compra*0.05
                        pagar=compra-dscto
                        areatexto.insert(1.0, "\nEl importe a pagar por los shorts es : {}".format(pagar))
                    elif cant<=3:
                        areatexto.insert(1.0, "\nEl importe a pagar por los shorts es : {}".format(compra))
                elif ((prenda=="Casacas") and (talla=="XXL")):
                    precio=105.0
                    compra=precio*cant
                    if cant>3:
                        dscto=compra*0.05
                        pagar=compra-dscto
                        areatexto.insert(1.0, "\nEl importe a pagar por los shorts es : {}".format(pagar))
                    elif cant<=3:
                        areatexto.insert(1.0, "\nEl importe a pagar por los shorts es : {}".format(compra))
                if ((compra>400) and (pagar>400)):
                    areatexto.insert(1.0, "\nPor una compra mayor a S/.400 usted acaba de recibir un vale de descuento del 10% en su siguiente compra : {}")

        ventanaPrincipal=tkinter.Tk()
        ventanaPrincipal.title("Ventana Principal")
        ventanaPrincipal.geometry("600x500")
        ventanaPrincipal.configure(background='pink')

        lblnombre=tkinter.Label(ventanaPrincipal, text="Ingrese su nombre")
        lblnombre.place(x=50, y=50)
        lbldni=tkinter.Label(ventanaPrincipal,text="Ingrese el numero de DNI:")
        lbldni.place(x=50, y=80)
        lblcomboprenda=tkinter.Label(ventanaPrincipal, text="Elige el tipo de prenda:")
        lblcomboprenda.place(x=50, y=110)
        lblcombotalla=tkinter.Label(ventanaPrincipal,text="Elige la talla:")
        lblcombotalla.place(x=50,y=140)
        lblcantidad=tkinter.Label(ventanaPrincipal, text="Ingrese la cantidad de prendas:")
        lblcantidad.place(x=50, y=170)
        txtnombre=tkinter.Entry(ventanaPrincipal,width=20)
        txtnombre.place(x=230, y=50)
        txtdni=tkinter.Entry(ventanaPrincipal, width=20)
        txtdni.place(x=230,y=80)
        comboprenda=ttk.Combobox(state="readonly", values=["Jeans", "Faldas", "Shorts","Tops", "Casacas"])
        comboprenda.place(x=230, y=110)
        combotalla=ttk.Combobox(state="readonly", values=["S", "M", "L", "XL", "XXL"])
        combotalla.place(x=230, y=140)
        txtcantidad=tkinter.Entry(ventanaPrincipal, width=20)
        txtcantidad.place(x=230, y=170)
        btnprocesar = tkinter.Button(ventanaPrincipal, text="Ejecutar", command=calcular)
        btnprocesar.place(x=400, y=50)
        btnborrar = tkinter.Button(ventanaPrincipal, text="Borrar", command=borrar)
        btnborrar.place(x=400, y=80)
        areatexto = tkinter.Text(ventanaPrincipal)
        areatexto.config(width=40, height=10)
        areatexto.place(x=50, y=250)

        ventanaPrincipal.mainloop()

    def entrar(self):
        usuario = self.txtusuario.get()
        clave = self.txtclave.get()
        if (len(usuario) == 0):
            messagebox.showinfo(message="Ingrese el campo Usuario!!", title="Titulo")
            self.txtusuario.focus();
        elif (len(clave) == 0):
            messagebox.showinfo(message="Ingrese el campo Clave!!", title="Titulo")
            self.txtclave.focus();
        else:
            estado = self.BuscarUsuario(usuario, int(clave))

            if (estado):
                self.ventanaPrincipal()
            else:
                messagebox.showinfo(message="Usuario y clave incorrecta", title="Titulo")

    def VentanaInicio(self):
        ventanaInicio = tkinter.Tk()
        ventanaInicio.title("Ventana de Inicio")
        ventanaInicio.geometry("300x300")

        lblusuario = tkinter.Label(ventanaInicio, text="Usuario : ")
        lblusuario.place(x=50, y=50)

        lblclave = tkinter.Label(ventanaInicio, text="Clave : ")
        lblclave.place(x=50, y=90)

        self.txtusuario = tkinter.Entry(ventanaInicio, width=20)
        self.txtusuario.place(x=150, y=50)

        self.txtclave = tkinter.Entry(ventanaInicio, show="*")
        self.txtclave.place(x=150, y=90)

        btnEntrar = tkinter.Button(ventanaInicio, text="Entrar", command=self.entrar)
        btnEntrar.place(x=80, y=140)

        btncerrar = tkinter.Button(ventanaInicio, text="Cerrar", command=ventanaInicio.quit)
        btncerrar.place(x=150, y=140)
        ventanaInicio.mainloop()

objeto = Validacion()
objeto.VentanaInicio()
objeto.ventanaPrincipal()