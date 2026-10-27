saldo = 1000

def consultar_saldo():
    global saldo 
    print("su saldo actual es:",
saldo )

def depositar ():
    global saldo 
    monto =float(input("ingreseel momto a depositar : "))

    if monto > 0:
        saldo =saldo + monto 
        print("deposito exitoso.")
        print("nuevo saldo:, saldo ")
    else:
        print("error:el monto debe ser mayor que cero.")

def retirar ():
    global saldo 
    monto= float (input ("ingrese el monto a retirar :"))

    if monto <- 0 : 
        print ("error : el monto debe ser mayor que cero.")
    elif monto > saldo :
        print("saldo insuficiente.")
    else :
        saldo= saldo -monto 
        print("retiro exitosoo,")
        print("nuevo saldo:", saldo )

while True:
    print("\n===cajero automatico===")
    print("1.consultar saldo")
    print("2.depositar dinero")
    print("3.retirar dinero")
    print("o, salir ")

    opcion = input("seleccione una opccion :")
    if opcion == "1":
        consultar_saldo()
    elif opcion == "2":
        depositar ()
    elif opcion == "3":
        retirar
    elif opcion == "o":
        print("gracias por utiulizar el cagero.")
        break
    else:
        print("opcion no valida.")



