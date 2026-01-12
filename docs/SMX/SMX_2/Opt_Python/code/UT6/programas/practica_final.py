from tkinter import *
###############
#etapa 0
###############
# ventana=Tk()
# ventana.mainloop()    

###############
#etapa 1
###############
# class Calculadora:
#   def __init__(self, ventana):
#     self.ventana=ventana



# ventana=Tk()
# calculadora=Calculadora(ventana)
# ventana.mainloop()    
  
###############
#etapa 3
###############
class Calculadora:
  def __init__(self, ventana):
    self.ventana=ventana
    self.ventana.title("Calculadora")


ventana=Tk()
calculadora=Calculadora(ventana)
ventana.mainloop()  

###############
#etapa 4
###############
# class Calculadora:
#   def __init__(self, ventana):
#     self.ventana=ventana
#     self.ventana.title("Calculadora")
#     # etapa 4
#     self.pantalla = Label(ventana, text='0', width=26, height=2, background="black", 
#                           foreground="white", font=("Helvetica", 20), anchor="e", padx=10)

# ventana=Tk()
# calculadora=Calculadora(ventana)
# ventana.mainloop()  

###############
#etapa 5
###############
# class Calculadora:
#   def __init__(self, ventana):
#     self.ventana=ventana
#     self.ventana.title("Calculadora")
#     # etapa 4
#     self.pantalla = Label(ventana, text='0', width=26, height=2, background="black", 
#                           foreground="white", font=("Helvetica", 20), anchor="e", padx=10) 
  
#   # Etapa 5
#   def crear_boton(self, valor):
#     return Button(self.ventana, text=valor, width=9, height=1, font=("Helvetica",15))

# ventana=Tk()
# calculadora=Calculadora(ventana)
# ventana.mainloop()  

###############
#etapa 6
###############
# class Calculadora:
#   def __init__(self, ventana):
#     self.ventana=ventana
#     self.ventana.title("Calculadora")
#     # etapa 4
#     self.pantalla = Label(ventana, text='0', width=26, height=2, background="black", 
#                           foreground="white", font=("Helvetica", 20), anchor="e", padx=10)
#     # Etapa 6
#     # Crear los botones de la calculadora
#     # botonXX se crea y se utiliza dentro de __init__
#     # Luego no se vuelve a usar por eso no es necesario hacer self.botonXX (variable de clase).
#     boton1=self.crear_boton(7)
#     boton2=self.crear_boton(8)
#     boton3=self.crear_boton(9)
#     boton4=self.crear_boton("\u00F7")
#     boton5=self.crear_boton(4)
#     boton6=self.crear_boton(5)
#     boton7=self.crear_boton(6)
#     boton8=self.crear_boton("\u002A")
#     boton9=self.crear_boton(1)
#     boton10=self.crear_boton(2)
#     boton11=self.crear_boton(3)
#     boton12=self.crear_boton("-")
#     boton13=self.crear_boton(0)
#     boton14=self.crear_boton(".")
#     boton15=self.crear_boton("=")
#     boton16=self.crear_boton("+")
  
#   # Etapa 5
#   def crear_boton(self, valor):
#     return Button(self.ventana, text=valor, width=9, height=1, font=("Helvetica",15))

# ventana=Tk()
# calculadora=Calculadora(ventana)
# ventana.mainloop()  

###############
#etapa 7
###############
# class Calculadora:
#   def __init__(self, ventana):
#     self.ventana=ventana
#     self.ventana.title("Calculadora")
#     # etapa 4
#     self.pantalla = Label(ventana, text='0', width=26, height=2, background="black", 
#                           foreground="white", font=("Helvetica", 20), anchor="e", padx=10)
#     # Etapa 6
#     # Crear los botones de la calculadora
#     # botonXX se crea y se utiliza dentro de __init__
#     # Luego no se vuelve a usar por eso no es necesario hacer self.botonXX (variable de clase).
#     boton1=self.crear_boton(7)
#     boton2=self.crear_boton(8)
#     boton3=self.crear_boton(9)
#     boton4=self.crear_boton("\u00F7")
#     boton5=self.crear_boton(4)
#     boton6=self.crear_boton(5)
#     boton7=self.crear_boton(6)
#     boton8=self.crear_boton("\u002A")
#     boton9=self.crear_boton(1)
#     boton10=self.crear_boton(2)
#     boton11=self.crear_boton(3)
#     boton12=self.crear_boton("-")
#     boton13=self.crear_boton(0)
#     boton14=self.crear_boton(".")
#     boton15=self.crear_boton("=")
#     boton16=self.crear_boton("+")

#     # Etapa 8
#     #Ubicar los botones con el gestor grid
#     botones=[boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9, boton10, boton11, boton12, boton13, boton14, boton15, boton16]
#     contador=0
#     for fila in range(1,5):
#       for columna in range(4):
#         botones[contador].grid(row=fila,column=columna)
#         contador+=1
  
#     # Etapa 7
#     # Ubicar la pantalla en la ventana
#     self.pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="we")

#   # Etapa 5
#   def crear_boton(self, valor):
#     print(f"Boton {valor}, creado")
#     return Button(self.ventana, text=valor, width=9, height=1, font=("Helvetica",15))

# ventana=Tk()
# calculadora=Calculadora(ventana)
# ventana.mainloop()  


###############
#etapa 8
###############