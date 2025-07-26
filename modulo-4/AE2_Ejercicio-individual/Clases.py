from funciones import *
import random

class CuentaCorriente:
    def __init__(self, titular, banco, saldo=0):
        self.titular = titular
        self.banco = banco
        self.saldo = saldo
    
    def depositar(self, cantidad):
        self.saldo = movimiento_saldo(self.saldo, cantidad, "deposito")
        return self
        
    def retirar(self, cantidad):
        self.saldo = movimiento_saldo(self.saldo, cantidad, "giro")
        return self
    
    def consultar_saldo(self):
        print(f"El saldo de la cuenta es: {self.saldo}")
        return self

class Tarjeta(): # Clase tarjeta de debito
    def __init__(self, cuenta, numero=random.randint(1000000000000000, 9999999999999999), cvv=random.randint(100, 999), fecha_vencimiento=(str(random.randint(1, 12)))+"/"+(str(random.randint(26, 40))), tipo_tarjeta="Debito"):
        self.cuenta = cuenta
        self.numero = numero
        self.cvv = cvv
        self.fecha_vencimiento = fecha_vencimiento
        self.tipo_tarjeta = tipo_tarjeta
    
    def comprar(self, monto):
        saldo = movimiento_saldo(self.saldo, monto, "compra")
        if saldo != False:
            self.saldo = saldo
        else:
            pass
        print()
        return self

class TC(Tarjeta): # Clase Tarjeta de Crédito
    def __init__(self, cuenta, cupo_max, numero=random.randint(1000000000000000, 9999999999999999), cvv=random.randint(100, 999), fecha_vencimiento=(str(random.randint(1, 12)))+"/"+(str(random.randint(26, 40))), interes=1.5, tipo_tarjeta="Credito"):
        super().__init__(cuenta, numero, cvv, fecha_vencimiento, tipo_tarjeta)
        self.interes = interes / 100
        self.cupo_max = cupo_max
        self.cupo = cupo_max
        self.cupo_usado = 0
        self.valor_cuota = 0
    
    def comprarTC(self, monto):
        cupo = movimiento_saldo(self.cupo, monto, "compra")
        if cupo is not False:
            print(cupo)
            self.cupo = cupo
            self.cupo_usado += monto
            while True:
                cuotas = input("¿Cuántas cuotas quieres? ")
                if not cuotas.isdigit():
                    print("Debes ingresar un número entero")
                else:
                    cuotas = int(cuotas)
                    break
            cuotas = int(cuotas)
            valor_cuota = (monto / cuotas)
            self.valor_cuota += round(valor_cuota)
            print("Compra realizada")
            print(f"Cuotas: {cuotas}")
            print(f"Valor de la cuota: ${round(valor_cuota)}")
        else:
            pass
        print()
        return self
    
    def consultar_tarjeta(self):
        print(f"Tu cupo utilizado es de: ${self.cupo_usado}")
        print(f"Tu cupo es de: ${self.cupo}")
        print(f"Los intereses que son cobrados son de: {self.interes * 100}%")
        print(f"El valor de la próxima cuota es de: ${self.valor_cuota}")
        print()
        return self
    
    def pagar_cuota(self): # Acá se hizo un método para que se pueda pagar la cuota y se cobra el interes al valor_cuota
        valor_cuota_con_interes = round(self.valor_cuota + (self.valor_cuota * self.interes))
        print(f"Valor de la cuota a pagar: ${valor_cuota_con_interes}")
        while True:
            monto_pago = input("Ingrese el monto que desea pagar: $")
            if not monto_pago.isdigit():
                print("Debes ingresar un número entero")
            else:
                monto_pago = int(monto_pago)
                if monto_pago > valor_cuota_con_interes:
                    print("No puedes pagar más de lo que debes")
                else:
                    print()
                    monto_pago = int(monto_pago)
                    if monto_pago <= (self.valor_cuota * self.interes):
                        self.cupo_usado += self.valor_cuota
                        pass # pasa de largo porque solo se canceló el interés y no afecta en el resto del cupo
                    else:
                        saldo_valor_cuota = valor_cuota_con_interes - monto_pago
                        self.cupo_usado -= (self.valor_cuota - saldo_valor_cuota)
                        self.cupo += (self.valor_cuota - saldo_valor_cuota)
                    break
        print()
        return self
        
        