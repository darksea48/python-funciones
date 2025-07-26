from Clases import *
import random
import os

cuenta_douglas = CuentaCorriente("Douglas", "Banco Estado")
cuenta_douglas.depositar(1000000)
# cuenta_douglas.consultar_saldo()

cuenta_1 = CuentaCorriente("Cliente 1", "Scotiabank")
cuenta_1.depositar(200000)
# cuenta_1.consultar_saldo()

cuenta_2 = CuentaCorriente("Cliente 2", "Banco de Chile")
cuenta_2.depositar(500000)
# cuenta_2.consultar_saldo()

cuenta_3 = CuentaCorriente("Cliente 3", "Banco Santander")
cuenta_3.depositar(1000000)
# cuenta_3.consultar_saldo()

while True:
    print("¿Quieres limpiar la pantalla para probar la siguiente parte del código? (S/N): ")
    respuesta = input().upper()
    if respuesta == "S":
        os.system("cls")
        break
    elif respuesta == "N":
        print("Saliendo del programa...")
        exit()
    else:
        print("Respuesta inválida. Por favor, ingrese S o N.")

tarjeta_1 = TC(cuenta=cuenta_1, cupo_max=500000)

tarjeta_2 = TC(cuenta=cuenta_2, cupo_max=100000)

tarjeta_3 = TC(cuenta=cuenta_3, cupo_max=300000)

# Tarjeta 1
tarjeta_1.comprarTC(30000).comprarTC(50000)
tarjeta_1.pagar_cuota()
tarjeta_1.consultar_tarjeta()

# Tarjeta 2
tarjeta_2.comprarTC(20000).comprarTC(50000).comprarTC(10000)
tarjeta_2.pagar_cuota().pagar_cuota()
tarjeta_2.consultar_tarjeta()

# Tarjeta 3
tarjeta_3.comprarTC(100000).comprarTC(50000).comprarTC(50000).comprarTC(75000).comprarTC(100000)
tarjeta_3.consultar_tarjeta()