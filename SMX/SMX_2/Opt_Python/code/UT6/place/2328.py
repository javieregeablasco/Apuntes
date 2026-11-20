# ejercicio 1
# from tkinter import *
# import os

# ruta_imagen = os.path.join(os.path.dirname(os.path.abspath(__file__)), "favicon.ico")

# root = Tk()
# root.title("Ejercicio 1")
# root.iconbitmap(ruta_imagen)
# root.config(width=400, height=300)

# frame1 = Frame(root, bg="blue", width=50, height=50)
# frame1.place(x=140, y=20)

# root.mainloop()

'''ejercicio 2'''
from tkinter import *
import os

ruta_imagen = os.path.join(os.path.dirname(os.path.abspath(__file__)), "favicon.ico")

root = Tk()
root.title("Ejercicio 1")
root.iconbitmap(ruta_imagen)
root.config(width=600, height=500)

# Crear los 7 frames, ver si se puede crear un bucle con append
frame_1 = Frame(root, bg="red", bd=4, relief="ridge")
frame_2 = Frame(root, bg="green", bd=4, relief="ridge")
frame_3 = Frame(root, bg="blue", bd=4, relief="ridge")
frame_4 = Frame(root, bg="yellow", bd=4, relief="ridge")
frame_5 = Frame(root, bg="orange", bd=4, relief="ridge")
frame_6 = Frame(root, bg="purple", bd=4, relief="ridge")
frame_7 = Frame(root, bg="gray", bd=4, relief="ridge")

# Tamaños relativos al contenedor
ancho_columna = 0.5
altura_fila = 0.25

# Fila 0
frame_1.place(relx=0,             rely=0 * altura_fila, relwidth=ancho_columna, relheight=altura_fila)
frame_2.place(relx=ancho_columna, rely=0 * altura_fila, relwidth=ancho_columna, relheight=altura_fila)

# Fila 1
frame_3.place(relx=0,             rely=1 * altura_fila, relwidth=ancho_columna, relheight=altura_fila)
frame_4.place(relx=ancho_columna, rely=1 * altura_fila, relwidth=ancho_columna, relheight=altura_fila)

# Fila 2
frame_5.place(relx=0,             rely=2 * altura_fila, relwidth=ancho_columna, relheight=altura_fila)
frame_6.place(relx=ancho_columna, rely=2 * altura_fila, relwidth=ancho_columna, relheight=altura_fila)

# Fila 3
frame_7.place(relx=0,             rely=3 * altura_fila, relwidth=1,            relheight=altura_fila)

root.mainloop()

