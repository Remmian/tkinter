from tkinter import *
from tkinter import messagebox
import os.path
from templates.shop import shopWindow


def saveUser():
    # Obtenemos el nombre de usuario y la contraseña
    username = user_entry.get().strip()
    userPassword = pass_entry.get()
    userDni = dni_entry.get().strip()

    # Creamos un archivo con el nombre del usuario
    routeFile = f"./src/users/{username}.txt"

    # Existe el archivo?
    existingUser = os.path.isfile(routeFile)

    # Si retorna True es porque el usuario ya existe
    if existingUser:
        messagebox.showwarning(
            'Registro', 'Usuario ya registrado')

    else:
        with open(routeFile, "w") as file:
            if len(userPassword) > 3:
                # Guardamos la contraseña en el archivo
                file.write(f"Constraseña : {userPassword} | DNI : {userDni}")
                file.close()

                # Re dirigimos a la ventana de Ventas
                root.destroy()
                shopWindow()
            else:
                messagebox.showwarning(
                    'Registro', 'La contraseña debe tener al menos 4 caracteres')


def RegisterWindow():
    global root
    global user_entry
    global pass_entry
    global dni_entry
    root = Tk(className='Login')

    # Agregamos un background image
    imagen = PhotoImage(file="./src/img/register.png")
    background = Label(image=imagen)
    background.place(x=0, y=0, relwidth=1, relheight=1)

    # Tamaño de la ventana
    root.geometry("600x600")
    root.resizable(False, False)  # No se puede redimensionar

    # Entry username
    user_entry = Entry(root, font=('Helvetica', 14, 'normal'))
    user_entry.focus_set()
    user_entry.place(x=170, y=228, width=200, height=25)

    # Entry DNI
    dni_entry = Entry(root, font=('Helvetica', 14, 'normal'))
    dni_entry.place(x=170, y=312, width=200, height=25)

    # Entry password
    pass_entry = Entry(root, font=('Helvetica', 14, 'normal'), show="*")
    pass_entry.place(x=170, y=396, width=200, height=25)

    # Button Register
    buttonRegister = Button(root, text='Registrarse', font=('Helvetica', 14, 'normal'),
                            bg="black", fg="white", command=saveUser)

    buttonRegister.place(x=210, y=460, width=220, height=36)

    root.mainloop()


if __name__ == "__main__":
    RegisterWindow()
