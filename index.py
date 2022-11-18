from tkinter import *
from tkinter import messagebox
from shop import ShopWindow


def check_pass():
    username = user_entry.get()
    userPassword = pass_entry.get()

    routeFile = f"./src/users/{username}.txt"

    try:
        with open(routeFile, "r") as file:
            lines = file.readlines()
            password = lines[0]
            if userPassword == password:
                root.destroy()
                ShopWindow()
            else:
                messagebox.showwarning(
                    'Login Page', 'Contraseña incorrecta')
    except:
        messagebox.showwarning(
            'Login Page', 'Usuario o contraseña incorrectos')


def loginWindow():
    global user_entry
    global pass_entry
    global root

    root = Tk(className='Login')

    imagen = PhotoImage(file="./src/img/login.png")

    # Con Label y la opción image, puedes mostrar una imagen en el widget:
    background = Label(image=imagen)

    # Con place puedes organizar el widget de la imagen posicionandolo
    # donde lo necesites (relwidth y relheight son alto y ancho en píxeles):
    background.place(x=0, y=0, relwidth=1, relheight=1)

    # Tamaño de la ventana
    root.geometry("600x600")
    root.resizable(False, False)  # No se puede redimensionar

    # Entry username
    user_entry = Entry(root, font=fontOptions)
    user_entry.place(x=184, y=216, width=200, height=25)

    # Entry password
    pass_entry = Entry(root, font=fontOptions)
    pass_entry.place(x=184, y=316, width=200, height=25)

    # Button Enter
    buttonEnter = Button(root, text='Ingresar', font=fontOptions,
                         bg="black", fg="white", command=check_pass)

    buttonEnter.place(x=193, y=375, width=210, height=36)

    # Button Enter
    buttonRegister = Button(root, text='Registrarse', font=fontOptions,
                            bg="black", fg="white")

    buttonRegister.place(x=193, y=503, width=220, height=36)

    root.mainloop()


fontOptions = ('Helvetica', 14, 'normal')

if __name__ == "__main__":
    loginWindow()
