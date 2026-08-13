class CuentaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
        else:
            print("el monto a depositar debe ser mayor a 0.")

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
        else:
            print("fondos insuficientes para realizar el retiro.")

    def mostrar_info(self):
        print(f"titular: {self.titular} - saldo: ${self.saldo:.2f}")


cuenta1 = CuentaBancaria("pilar villegas", 5000.0)
cuenta2 = CuentaBancaria("otro titular")  

cuenta1.mostrar_info()
cuenta1.depositar(1500)
cuenta1.retirar(2000)
cuenta1.mostrar_info()

cuenta2.mostrar_info()
cuenta2.depositar(300)
cuenta2.retirar(1000) #no tenemos suficiente
cuenta2.mostrar_info()