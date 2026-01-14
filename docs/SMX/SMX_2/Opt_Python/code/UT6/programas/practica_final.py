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
# class Calculadora:
#   def __init__(self, ventana):
#     self.ventana=ventana
#     self.ventana.title("Calculadora")


# ventana=Tk()
# calculadora=Calculadora(ventana)
# ventana.mainloop()  

#### version 2 ####
# class Calculadora:
#   def __init__(self):
#     self.ventana=Tk()
#     self.ventana.title("Calculadora")
#     self.ventana.mainloop()

# Calculadora()

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

# class Calculadora:
#   def __init__(self,):
#     self.ventana=Tk()
#     self.ventana.title("Calculadora")
#     # etapa 4
#     self.pantalla = Label(self.ventana, text='0', width=26, height=2, background="black", 
#                           foreground="white", font=("Helvetica", 20), anchor="e", padx=10)

#     self.ventana.mainloop()

# Calculadora()
  

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
#   def __init__(self):
#     self.ventana=Tk()
#     self.ventana.title("Calculadora")
#     # etapa 4
#     self.pantalla = Label(self.ventana, text='0', width=26, height=2, background="black", 
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
#         botones[contador].grid(row=fila,column=columna, padx=2, pady=2 )
#         contador+=1
  
#     # Etapa 7
#     # Ubicar la pantalla en la ventana
#     self.pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="we")

#     self.ventana.mainloop()
#   # Etapa 5
#   def crear_boton(self, valor):
#     print(f"Boton {valor}, creado")
#     return Button(self.ventana, text=valor, width=9, height=1, font=("Helvetica",15))

# Calculadora()
  


# ###############
# #etapa 9
# ###############
# class Calculadora:
#   def __init__(self):
#     self.ventana=Tk()
#     self.ventana.title("Calculadora")
    
#     ########### 
#     ########### 
#     # etapa 9 #
#     self.texto_pantalla = StringVar(value="")    
#     ########### 
#     ########### 

#     ########### 
#     # etapa 9 #
#     self.pantalla = Label(self.ventana, textvariable=self.texto_pantalla, width=26, height=2, background="black", 
#                           foreground="white", font=("Helvetica", 20), anchor="e", padx=10)
#     ########### 
    
#     ########### 
#     # etapa 9 #
#     boton1=self.crear_boton(7)
#     boton2=self.crear_boton(8)
#     boton3=self.crear_boton(9)
#     boton4=self.crear_boton("\u00F7",False)
#     boton5=self.crear_boton(4)
#     boton6=self.crear_boton(5)
#     boton7=self.crear_boton(6)
#     boton8=self.crear_boton("\u002A",False)
#     boton9=self.crear_boton(1)
#     boton10=self.crear_boton(2)
#     boton11=self.crear_boton(3)
#     boton12=self.crear_boton("-",False)
#     boton13=self.crear_boton(0)
#     boton14=self.crear_boton(".")
#     boton15=self.crear_boton("=",False)
#     boton16=self.crear_boton("+",False)
#     ########### 

  
#     botones=[boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9, boton10, boton11, boton12, boton13, boton14, boton15, boton16]
#     contador=0
#     for fila in range(1,5):
#       for columna in range(4):
#         botones[contador].grid(row=fila,column=columna, padx=2, pady=2 )
#         contador+=1
  
  
#     self.pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="we")

#     self.ventana.mainloop()
  
#   def crear_boton(self, valor, operando=True):
#     print(f"Boton {valor}, creado")
#     ########### 
#     # etapa 9 #
#     return Button(self.ventana, text=valor, width=9, height=1, font=("Helvetica",15), command=lambda:self.escribir(valor,operando) )
#     ########### 
  
#   ########### 
#   # Etapa 9
#   def escribir(self,valor,operando):
#     self.texto_pantalla.set(self.texto_pantalla.get()+valor)
#   ########### 
   

# Calculadora()

###############
#etapa 10
###############
class Calculadora:
  def __init__(self):
    self.ventana=Tk()
    self.ventana.title("Calculadora")
    self.texto_pantalla = StringVar(value="")    
    self.pantalla = Label(self.ventana, textvariable=self.texto_pantalla, width=26, height=2, background="black", 
                          foreground="white", font=("Helvetica", 20), anchor="e", padx=10)
    
    boton1=self.crear_boton("7")
    boton2=self.crear_boton("8")
    boton3=self.crear_boton("9")
    boton4=self.crear_boton("/",True)
    boton5=self.crear_boton("4")
    boton6=self.crear_boton("5")
    boton7=self.crear_boton("6")
    boton8=self.crear_boton("*",True)
    boton9=self.crear_boton("1")
    boton10=self.crear_boton("2")
    boton11=self.crear_boton("3")
    boton12=self.crear_boton("-",True)
    boton13=self.crear_boton("0")
    boton14=self.crear_boton(".")
    boton15=self.crear_boton("=",True)
    boton16=self.crear_boton("+",True)
      
    botones=[boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9, boton10, boton11, boton12, boton13, boton14, boton15, boton16]
    contador=0
    for fila in range(1,5):
      for columna in range(4):
        botones[contador].grid(row=fila,column=columna, padx=2, pady=2 )
        contador+=1
    
    self.pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="we")
    
    self.ventana.mainloop()
  
  #######################
  ## Metodos de clase  ##
  #######################  
  def crear_boton(self, valor, operando=False):
    # print(f"Boton {valor}, creado")
    return Button(self.ventana, text=valor, width=9, height=1, font=("Helvetica",15), command=lambda:self.escribir(valor,operando))
    
    
  def escribir(self,valor,operando):
    # self.pantalla.configure(foreground="white", background="black")
    valor_actual = self.texto_pantalla.get()
    if operando==False:
      self.texto_pantalla.set(self.texto_pantalla.get()+valor)

    else:
      if valor in ["+", "-", "*", "/"]:
        self.primer_numero = float(valor_actual)
        self.operacion_a_realizar = valor
        self.texto_pantalla.set("")        

      else: # pulsado '='
        segundo_numero = float(valor_actual)
     
        if self.operacion_a_realizar == "+":
          resultado = self.primer_numero + segundo_numero
        elif self.operacion_a_realizar == "-":
          resultado = self.primer_numero - segundo_numero
        elif self.operacion_a_realizar == "*":
          resultado = self.primer_numero * segundo_numero
        elif self.operacion_a_realizar == "/":
          if self.segundo_numero != 0:
            resultado = self.primer_numero / segundo_numero
          else:
            resultado = "Error: Division/0"
            # self.pantalla.configure(foreground="red", background="yellow")

        self.texto_pantalla.set(resultado)    

         

    
   
Calculadora()

    #     else:
    #         # Si es un operador (+, -, *, /)
    #         if valor in ["+", "-", "*", "/"]:
    #             try:
    #                 self.primer_numero = float(valor_actual)
    #                 self.operacion_pendiente = valor
    #                 self.texto_pantalla.set("") # Limpiamos para el segundo número
    #             except ValueError:
    #                 self.texto_pantalla.set("Error")

    #         # Si es el botón "="
    #         elif valor == "=":
    #             try:
    #                 segundo_numero = float(valor_actual)
    #                 resultado = 0

    #                 if self.operacion_pendiente == "+":
    #                     resultado = self.primer_numero + segundo_numero
    #                 elif self.operacion_pendiente == "-":
    #                     resultado = self.primer_numero - segundo_numero
    #                 elif self.operacion_pendiente == "*":
    #                     resultado = self.primer_numero * segundo_numero
    #                 elif self.operacion_pendiente == "/":
    #                     if segundo_numero != 0:
    #                         resultado = self.primer_numero / segundo_numero
    #                     else:
    #                         resultado = "Error: Div/0"

    #                 # Mostramos el resultado y reseteamos la operación
    #                 self.texto_pantalla.set(resultado)
    #                 self.operacion_pendiente = "" 
    #             except:
    #                 self.texto_pantalla.set("Error")

 


# from tkinter import *

# class Calculadora:
#     def __init__(self):
#         self.ventana = Tk()
#         self.ventana.title("Calculadora")
#         self.texto_pantalla = StringVar(value="")
        
#         # Pantalla
#         self.pantalla = Label(self.ventana, textvariable=self.texto_pantalla, width=26, height=2, 
#                               background="black", foreground="white", font=("Helvetica", 20), 
#                               anchor="e", padx=10)
#         self.pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="we")

#         # Variables de estado
#         self.operacion_pendiente = "" # Almacena si es +, -, *, /
#         self.primer_numero = 0.0      # Almacena el primer valor de la operación

#         # Creación de botones
#         boton1=self.crear_boton("7")
#         boton2=self.crear_boton("8")
#         boton3=self.crear_boton("9")
#         boton4=self.crear_boton("/", False)
#         boton5=self.crear_boton("4")
#         boton6=self.crear_boton("5")
#         boton7=self.crear_boton("6")
#         boton8=self.crear_boton("*", False)
#         boton9=self.crear_boton("1")
#         boton10=self.crear_boton("2")
#         boton11=self.crear_boton("3")
#         boton12=self.crear_boton("-", False)
#         boton13=self.crear_boton("0")
#         boton14=self.crear_boton(".")
#         boton15=self.crear_boton("=", False)
#         boton16=self.crear_boton("+", False)
          
#         botones=[boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, 
#                  boton9, boton10, boton11, boton12, boton13, boton14, boton15, boton16]
        
#         contador=0
#         for fila in range(1,5):
#             for columna in range(4):
#                 botones[contador].grid(row=fila, column=columna, padx=2, pady=2)
#                 contador+=1

#         self.ventana.mainloop()
  
#     def crear_boton(self, valor, operando=True):
#         return Button(self.ventana, text=valor, width=9, height=1, font=("Helvetica", 15), 
#                       command=lambda: self.escribir(valor, operando))
    
#     def escribir(self, valor, operando):
#         valor_actual = self.texto_pantalla.get()

#         if operando:
#             # Si es un número o punto, lo añadimos a la pantalla
#             self.texto_pantalla.set(valor_actual + str(valor))

#         else:
#             # Si es un operador (+, -, *, /)
#             if valor in ["+", "-", "*", "/"]:
#                 try:
#                     self.primer_numero = float(valor_actual)
#                     self.operacion_pendiente = valor
#                     self.texto_pantalla.set("") # Limpiamos para el segundo número
#                 except ValueError:
#                     self.texto_pantalla.set("Error")

#             # Si es el botón "="
#             elif valor == "=":
#                 try:
#                     segundo_numero = float(valor_actual)
#                     resultado = 0

#                     if self.operacion_pendiente == "+":
#                         resultado = self.primer_numero + segundo_numero
#                     elif self.operacion_pendiente == "-":
#                         resultado = self.primer_numero - segundo_numero
#                     elif self.operacion_pendiente == "*":
#                         resultado = self.primer_numero * segundo_numero
#                     elif self.operacion_pendiente == "/":
#                         if segundo_numero != 0:
#                             resultado = self.primer_numero / segundo_numero
#                         else:
#                             resultado = "Error: Div/0"

#                     # Mostramos el resultado y reseteamos la operación
#                     self.texto_pantalla.set(resultado)
#                     self.operacion_pendiente = "" 
#                 except:
#                     self.texto_pantalla.set("Error")

# Calculadora()