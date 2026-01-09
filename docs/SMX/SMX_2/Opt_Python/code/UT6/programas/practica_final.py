from tkinter import *

#fase 1
# class Calculadora:
#   def __init__(self, ventana):
#     self.ventana=ventana
#     self.ventana.title("Calculadora")


# ventana=Tk()
# calculadora=Calculadora(ventana)
# ventana.mainloop()    
  
#'''

#fase 2
class Calculadora:
  def __init__(self, ventana):
    self.ventana=ventana
    self.ventana.title("Calculadora")

    #Agregar una caja de texto para que sea la pantalla de la calculadora
    self.pantalla=Text(ventana, state="disabled", width=40, height=2, background="black", foreground="white", font=("Helvetica",15))

    #Ubicar la pantalla en la ventana
    self.pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

    #Inicializar la operación mostrada en pantalla como string vacío
    self.operacion=""

    #Crear los botones de la calculadora
    boton1=self.crear_boton(7)
    boton2=self.crear_boton(8)
    boton3=self.crear_boton(9)
    boton4=self.crear_boton("\u00F7")
    boton5=self.crear_boton(4)
    boton6=self.crear_boton(5)
    boton7=self.crear_boton(6)
    boton8=self.crear_boton("*")
    boton9=self.crear_boton(1)
    boton10=self.crear_boton(2)
    boton11=self.crear_boton(3)
    boton12=self.crear_boton("-")
    boton13=self.crear_boton(0)
    boton14=self.crear_boton(".")
    boton15=self.crear_boton("=")
    boton16=self.crear_boton("+")
    

    #Ubicar los botones con el gestor grid
    botones=[boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9, boton10, boton11, boton12, boton13, boton14, boton15, boton16]
    contador=0
    for fila in range(1,5):
      for columna in range(4):
        botones[contador].grid(row=fila,column=columna)
        contador+=1
    
  #Crea un botón mostrando el valor pasado por parámetro
  def crear_boton(self, valor, escribir=True, ancho=9, alto=1):
    return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica",15), command=lambda:self.click(valor,escribir))


ventana=Tk()
calculadora=Calculadora(ventana)
ventana.mainloop()


'''fase 3
class Calculadora:
  def __init__(self, ventana):
    self.ventana=ventana
    self.ventana.title("Calculadora")
    #Agregar una caja de texto para que sea la pantalla de la calculadora
    self.pantalla=Text(ventana, state="disabled", width=40, height=3, background="orchid", foreground="white", font=("Helvetica",15))

    #Ubicar la pantalla en la ventana
    self.pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

    #Inicializar la operación mostrada en pantalla como string vacío
    self.operacion=""

    #Crear los botones de la calculadora
    boton1=self.crearBoton(7)
    boton2=self.crearBoton(8)
    boton3=self.crearBoton(9)
    boton4=self.crearBoton(u"\u232B",escribir=False)
    boton5=self.crearBoton(4)
    boton6=self.crearBoton(5)
    boton7=self.crearBoton(6)
    boton8=self.crearBoton(u"\u00F7")
    boton9=self.crearBoton(1)
    boton10=self.crearBoton(2)
    boton11=self.crearBoton(3)
    boton12=self.crearBoton("*")
    boton13=self.crearBoton(".")
    boton14=self.crearBoton(0)
    boton15=self.crearBoton("+")
    boton16=self.crearBoton("-")
    boton17=self.crearBoton("=",escribir=False,ancho=20,alto=2)

    #Ubicar los botones con el gestor grid
    botones=[boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9, boton10, boton11, boton12, boton13, boton14, boton15, boton16, boton17]
    contador=0
    for fila in range(1,5):
      for columna in range(4):
        botones[contador].grid(row=fila,column=columna)
        contador+=1
    #Ubicar el último botón al final
    botones[16].grid(row=5,column=0,columnspan=4)    


  #Crea un botón mostrando el valor pasado por parámetro
  def crearBoton(self, valor, escribir=True, ancho=9, alto=1):
    return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica",15), command=lambda:self.click(valor,escribir))


ventana_principal=Tk()
calculadora=Calculadora(ventana_principal)
ventana_principal.mainloop()
'''