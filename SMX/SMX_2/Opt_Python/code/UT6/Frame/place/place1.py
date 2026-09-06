from tkinter import *

root = Tk()
root.title("Ejemplo con place")
root.geometry("600x400+500+200")

# Marco amarillo (mitad izquierda superior)
ventana1 = Frame(root, bg="yellow")
ventana1.place(relx=0, rely=0, relwidth=0.5, relheight=0.5)

# Marco rojo (mitad derecha superior)
ventana2 = Frame(root, bg="red")
ventana2.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.5)

# Marco azul (fila inferior ocupando todo el ancho)
ventana3 = Frame(root, bg="blue")
ventana3.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

root.mainloop()


# from tkinter import *
# root = Tk()
# root.title("Ejemplo con place")
# root.geometry("600x400+500+200")

# ventana1 = Frame(root, bg="yellow")
# ventana1.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5)
# # ventana1.place(x=25, y=25, width=50, height=25)

# ventana2 = Frame(root, bg="red")
# ventana2.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5)

# ventana3 = Frame(root, bg="blue",)
# ventana3.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

# root.mainloop()


# from tkinter import *

# root = Tk()
# root.title("Ejemplo con place")
# root.geometry("600x400+500+200")

# # Marco amarillo (mitad izquierda superior)
# ventana1 = Frame(root, bg="yellow")
# ventana1.place(relx=0, rely=0, relwidth=0.5, relheight=0.5)

# # Marco rojo (mitad derecha superior)
# ventana2 = Frame(root, bg="red")
# ventana2.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.5)

# # Marco azul (fila inferior ocupando todo el ancho)
# ventana3 = Frame(root, bg="blue")
# ventana3.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

# root.mainloop()