from tkinter import *
from tkinter import messagebox as MessageBox

# mensage = MessageBox.showinfo(title="Show info", message="Mi primera ventana de información", icon="info")

# alerta = MessageBox.showwarning(title="Alerta", message="Operación no autorizada")
# alerta = MessageBox.showerror(title="Alerta", message="Ha ocurrido un error")

# ventana =Tk()
# ventana.title("AskYesNo")
# ventana.geometry("300x150+400+300")

# def cerrar():
#     resultado = MessageBox.askyesno("Salir", 
#     "¿Está seguro que desea salir sin guardar?")
    
#     if resultado == True:
#       ventana.destroy()  

# boton = Button(ventana, text="Salir", command=cerrar)   
# boton.pack(anchor="center",pady=60) 

# ventana.mainloop()
 
# resultado = MessageBox.askretrycancel("Ha ocurrido un error", 
#     "¿Reintentar?")

# # if resultado == True:
# #     # Hacer algo
# #     pass

# print(resultado)

# from tkinter import colorchooser as ColorChooser

# def seleccionar():
#     color = ColorChooser.askcolor(title="Elige un color")
#     marco.config(bg=color[1])
#     print(color)

# ventana = Tk()
# ventana.title("Color chooser")
# ventana.geometry("300x200+400+300") 

# marco = Frame(ventana, background="#3498DB", width=250,height=150)
# marco.pack()

# boton = Button(marco, text="Elegir color", command=seleccionar)
# boton.pack()
# ventana.mainloop()
 
from tkinter import *
from tkinter import colorchooser as ColorChooser

def seleccionar():
    color = ColorChooser.askcolor(title="Elige un color")
    print("El color seleccionado es:", color) 
    if color is not None:
      marco.config(bg=color[1])

ventana = Tk()
ventana.title("Color chooser")
ventana.geometry("300x200+400+300")

color_inicial = "#3498DB"

marco = Frame(ventana, bg=color_inicial, width=150, height=150)
marco.pack(pady=20)
marco.pack_propagate(False)  # Evita que el frame cambie de tamaño

boton = Button(marco, text="Elegir color", command=seleccionar)
boton.pack(expand=True) # Centrar el boton

ventana.mainloop()

