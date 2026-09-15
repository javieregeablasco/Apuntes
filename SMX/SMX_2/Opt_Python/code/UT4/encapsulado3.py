class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo  # atributo privado

    # Método privado que devuelve el saldo
    def __obtener_saldo(self):
        return self.__saldo
    
    # Método privado que fija el saldo
    def __fijar_saldo_inicial(self, nuevo_saldo):
        self.__saldo = nuevo_saldo

    # Getter de la propiedad
    @property
    def visualizar_saldo(self):
        return self.__obtener_saldo()
    
    # Setter de la propiedad
    @visualizar_saldo.setter
    def visualizar_saldo(self, nuevo_saldo):
        self.__fijar_saldo_inicial(nuevo_saldo)


# --- Uso del objeto ---
cuenta = Cuenta(100)
print("Saldo inicial:", cuenta.visualizar_saldo)  # 100

cuenta.visualizar_saldo = 80  # usar el setter
print("Saldo actualizado:", cuenta.visualizar_saldo)  # 80
