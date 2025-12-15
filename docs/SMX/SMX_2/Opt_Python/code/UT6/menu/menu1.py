# from tkinter import *

# ventana = Tk()
# ventana.title("Barra de menús")
# ventana.geometry("300x100+300+400")

# def salir():
#     ventana.destroy()

# barra_menu = Menu(ventana)
# ventana.config(menu=barra_menu)

# menu_archivo = Menu(barra_menu, tearoff=0)
# barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

# menu_archivo.add_command(label="Nuevo")
# menu_archivo.add_command(label="Abrir")
# menu_archivo.add_separator()
# menu_archivo.add_command(label="Salir", command=salir)

# ventana.mainloop()


from tkinter import *

def nuevo():
    print("Nuevo archivo")

def abrir():
    print("Abrir archivo")

def salir():
    ventana.destroy()

def copiar():
    print("Copiar")

def pegar():
    print("Pegar")

ventana = Tk()
ventana.title("Ejemplo de barra de menús")
ventana.geometry("400x200")

# Barra de menú principal
barra_menu = Menu(ventana)
ventana.config(menu=barra_menu)

# ===== MENÚ ARCHIVO =====
menu_archivo = Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

menu_archivo.add_command(label="Nuevo", command=nuevo)
menu_archivo.add_command(label="Abrir", command=abrir)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)

# ===== MENÚ EDITAR =====
menu_editar = Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Editar", menu=menu_editar)

# Submenú Portapapeles dentro de Editar
menu_portapapeles = Menu(menu_editar, tearoff=0)
menu_editar.add_cascade(label="Portapapeles", menu=menu_portapapeles)

menu_portapapeles.add_command(label="Copiar", command=copiar)
menu_portapapeles.add_command(label="Pegar", command=pegar)

# Submenú Formato dentro de Editar
menu_formato = Menu(menu_editar, tearoff=0)
menu_editar.add_cascade(label="Formato", menu=menu_formato)

menu_formato.add_command(label="Mayúsculas")
menu_formato.add_command(label="Minúsculas")

ventana.mainloop()
