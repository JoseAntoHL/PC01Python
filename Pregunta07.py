n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))

opcion = int(input("Digite el numero de la opcion del menu que desea ejecutar: (1)Suma / (2)Resta / (3)Multiplicacion "))

if(opcion == 1):
    suma = n1 + n2
    print(f"La suma de {n1} + {n2} es: {suma}")
if(opcion == 2):
    resta = n1 - n2
    print(f"La resta de {n1} - {n2} es: {resta}")
if(opcion == 3):
    multi = n1 * n2
    print(f"La multiplicacion de {n1} * {n2} es: {multi}")
else:
    print("###Opcion Invalida###")