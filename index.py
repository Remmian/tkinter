from tkinter import *
from tkinter import messagebox

from templates.shop import shopWindow
from templates.register import RegisterWindow

fontOptions = ('Helvetica', 14, 'normal')


def openRegister():
    root.destroy()
    RegisterWindow()


def check_pass():
    username = user_entry.get().strip()
    userPassword = pass_entry.get()

    routeFile = f"./src/users/{username}.txt"

    try:
        with open(routeFile, "r") as file:
            lines = file.readlines()
            fields = lines[0].split("|")
            fieldPassword = fields[0].split(":")[1].strip()

            if userPassword == fieldPassword:
                root.destroy()
                shopWindow()

            else:
                messagebox.showwarning(
                    'Login Page', 'Contraseña incorrecta')
    except FileNotFoundError:
        messagebox.showwarning(
            'Login Page', 'Usuario o contraseña incorrectos')


def loginWindow():
    global user_entry
    global pass_entry
    global root

    root = Tk(className='Login')

    # Agregamos un background image
    imagen = PhotoImage(file="./src/img/login.png")
    background = Label(image=imagen)
    background.place(x=0, y=0, relwidth=1, relheight=1)

    # Tamaño de la ventana
    root.geometry("600x600")
    root.resizable(False, False)  # No se puede redimensionar

    # Entry username
    user_entry = Entry(root, font=fontOptions)
    user_entry.focus_set()
    user_entry.place(x=184, y=216, width=200, height=25)

    # Entry password
    pass_entry = Entry(root, font=fontOptions, show="*")
    pass_entry.place(x=184, y=316, width=200, height=25)

    # Button Enter
    buttonEnter = Button(root, text='Ingresar', font=fontOptions,
                         bg="black", fg="white", command=check_pass)

    buttonEnter.place(x=193, y=375, width=210, height=36)

    # Button Register
    buttonRegister = Button(root, text='Registrarse', font=fontOptions,
                            bg="black", fg="white", command=openRegister)

    buttonRegister.place(x=193, y=503, width=220, height=36)

    root.mainloop()


if __name__ == "__main__":
    loginWindow()
