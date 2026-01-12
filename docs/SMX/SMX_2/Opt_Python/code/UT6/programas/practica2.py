from tkinter import Tk, Label, Button, re

class Interfaz:
    def __init__(self, ventana):
        # Inicializar la ventana con un título
        self.ventana = ventana
        self.ventana.title("Calculadora")

        # Cambiamos Text por Label
        # anchor="e" sirve para que el texto se alinee a la derecha (East)
        self.pantalla = Label(ventana, text="", width=26, height=2, background="orchid", 
                             foreground="white", font=("Helvetica", 20), anchor="e", padx=10)

        # Ubicar la pantalla en la ventana
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="we")

        # Inicializar la operación mostrada en pantalla como string vacío
        self.operacion = ""

        # Crear los botones de la calculadora
        boton1 = self.crearBoton(7)
        boton2 = self.crearBoton(8)
        boton3 = self.crearBoton(9)
        #boton4 = self.crearBoton(u"\u232B", escribir=False)
        boton5 = self.crearBoton(4)
        boton6 = self.crearBoton(5)
        boton7 = self.crearBoton(6)
        boton8 = self.crearBoton(u"\u00F7")
        boton9 = self.crearBoton(1)
        boton10 = self.crearBoton(2)
        boton11 = self.crearBoton(3)
        boton12 = self.crearBoton("*")
        boton13 = self.crearBoton(".")
        boton14 = self.crearBoton(0)
        boton15 = self.crearBoton("+")
        boton16 = self.crearBoton("-")
        boton17 = self.crearBoton("=", escribir=False, ancho=20, alto=2)

        # Ubicar los botones con el gestor grid
        botones = [boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9, 
                   boton10, boton11, boton12, boton13, boton14, boton15, boton16, boton17]
        
        contador = 0
        for fila in range(1, 5):
            for columna in range(4):
                botones[contador].grid(row=fila, column=columna)
                contador += 1
        
        # Ubicar el último botón al final
        botones[16].grid(row=5, column=0, columnspan=4)

    # Crea un botón mostrando el valor pasado por parámetro
    def crearBoton(self, valor, escribir=True, ancho=9, alto=1):
        return Button(self.ventana, text=valor, width=ancho, height=alto, 
                      font=("Helvetica", 15), command=lambda: self.click(valor, escribir))

    # Controla el evento disparado al hacer click en un botón
    def click(self, texto, escribir):
        if not escribir:
            if texto == "=" and self.operacion != "":
                # Reemplazar el valor unicode de la división por el operador "/"
                self.operacion = re.sub(u"\u00F7", "/", self.operacion)
                try:
                    resultado = str(eval(self.operacion))
                    self.operacion = resultado # Guardamos el resultado para seguir operando
                    self.limpiarPantalla()
                    self.mostrarEnPantalla(resultado)
                except:
                    self.limpiarPantalla()
                    self.mostrarEnPantalla("Error")
                    self.operacion = ""
            
            elif texto == u"\u232B":
                self.operacion = ""
                self.limpiarPantalla()
        else:
            self.operacion += str(texto)
            self.mostrarEnPantalla(self.operacion)

    # Borra el contenido visual del Label
    def limpiarPantalla(self):
        self.pantalla.configure(text="")

    # Actualiza el texto del Label con el valor actual
    def mostrarEnPantalla(self, valor):
        self.pantalla.configure(text=valor)

ventana_principal = Tk()
calculadora = Interfaz(ventana_principal)
ventana_principal.mainloop()