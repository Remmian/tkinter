# import tkinter
from tkinter import *
from templates.shop import shopWindow
from tkinter import messagebox


def saveUser():
    username = user_entry.get().strip()
    userPassword = pass_entry.get()

    routeFile = f"./src/users/{username}.txt"
    # Guardamos la contraseña en el archivo
    with open(routeFile, "w") as file:
        if len(userPassword) > 3:
            file.write(userPassword)
            file.close()

            # Re dirigimos a la ventana de Ventas
            root.destroy()
            shopWindow()
        else:
            messagebox.showwarning(
                'Login Page', 'La contraseña debe tener al menos 4 caracteres')


def RegisterWindow():
    global root
    global user_entry
    global pass_entry
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
    user_entry.place(x=160, y=248, width=200, height=25)

    # Entry password
    pass_entry = Entry(root, font=('Helvetica', 14, 'normal'), show="*")
    pass_entry.place(x=160, y=345, width=200, height=25)

    # Button Register
    buttonRegister = Button(root, text='Registrarse', font=('Helvetica', 14, 'normal'),
                            bg="black", fg="white", command=saveUser)

    buttonRegister.place(x=195, y=428, width=220, height=36)

    root.mainloop()


if __name__ == "__main__":
    RegisterWindow()
