from tkinter import *

class Calculadora:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Calculadora")
        self.texto_pantalla = StringVar(value="")
        
        # Pantalla
        self.pantalla = Label(self.ventana, textvariable=self.texto_pantalla, width=26, height=2, 
                              background="black", foreground="white", font=("Helvetica", 20), 
                              anchor="e", padx=10)
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="we")

        # Variables de estado
        self.operacion_pendiente = "" # Almacena si es +, -, *, /
        self.primer_numero = 0.0      # Almacena el primer valor de la operación

        # Creación de botones
        boton1=self.crear_boton("7")
        boton2=self.crear_boton("8")
        boton3=self.crear_boton("9")
        boton4=self.crear_boton("/", False)
        boton5=self.crear_boton("4")
        boton6=self.crear_boton("5")
        boton7=self.crear_boton("6")
        boton8=self.crear_boton("*", False)
        boton9=self.crear_boton("1")
        boton10=self.crear_boton("2")
        boton11=self.crear_boton("3")
        boton12=self.crear_boton("-", False)
        boton13=self.crear_boton("0")
        boton14=self.crear_boton(".")
        boton15=self.crear_boton("=", False)
        boton16=self.crear_boton("+", False)
          
        botones=[boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, 
                 boton9, boton10, boton11, boton12, boton13, boton14, boton15, boton16]
        
        contador=0
        for fila in range(1,5):
            for columna in range(4):
                botones[contador].grid(row=fila, column=columna, padx=2, pady=2)
                contador+=1

        self.ventana.mainloop()
  
    def crear_boton(self, valor, operando=True):
        return Button(self.ventana, text=valor, width=9, height=1, font=("Helvetica", 15), 
                      command=lambda: self.escribir(valor, operando))
    
    def escribir(self, valor, operando):
        valor_actual = self.texto_pantalla.get()

        if operando:
            # Si es un número o punto, lo añadimos a la pantalla
            self.texto_pantalla.set(valor_actual + str(valor))

        else:
            # Si es un operador (+, -, *, /)
            if valor in ["+", "-", "*", "/"]:
                try:
                    self.primer_numero = float(valor_actual)
                    self.operacion_pendiente = valor
                    self.texto_pantalla.set("") # Limpiamos para el segundo número
                except ValueError:
                    self.texto_pantalla.set("Error")

            # Si es el botón "="
            elif valor == "=":
                try:
                    segundo_numero = float(valor_actual)
                    resultado = 0

                    if self.operacion_pendiente == "+":
                        resultado = self.primer_numero + segundo_numero
                    elif self.operacion_pendiente == "-":
                        resultado = self.primer_numero - segundo_numero
                    elif self.operacion_pendiente == "*":
                        resultado = self.primer_numero * segundo_numero
                    elif self.operacion_pendiente == "/":
                        if segundo_numero != 0:
                            resultado = self.primer_numero / segundo_numero
                        else:
                            resultado = "Error: Div/0"

                    # Mostramos el resultado y reseteamos la operación
                    self.texto_pantalla.set(resultado)
                    self.operacion_pendiente = "" 
                except:
                    self.texto_pantalla.set("Error")

Calculadora()