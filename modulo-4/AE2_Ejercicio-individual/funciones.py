def movimiento_saldo(saldo, cantidad, tipo_movimiento):
    if tipo_movimiento == "deposito":
        saldo += cantidad
        print("Depósito exitoso")
        print(f"Depósito realizado: ${cantidad}")
        print(f"Saldo actual: ${saldo}")
        return saldo
    elif tipo_movimiento == "giro":
        if saldo >= cantidad:
            saldo -= cantidad
            print("Retiro exitoso")
            print(f"Retiro realizado: ${cantidad}")
        else:
            print("Tu saldo es insuficiente")
        print(f"Saldo actual: ${saldo}")
        return saldo
    elif tipo_movimiento == "compra":
        if saldo >= cantidad:
            saldo -= cantidad
            print("Compra exitosa")
            print(f"Compra realizada: ${cantidad}")
            return int(saldo)
        else:
            print("Tu saldo es insuficiente")
            return False
    else:
        print("Tipo de operación no válido")
        return False