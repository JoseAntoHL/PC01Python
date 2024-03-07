peso_muneca = 75
peso_payaso = 112

cantidad_payasos = int(input("Cuantos payasos vendidos hay?"))
cantidad_munecas = int(input("Cuantas munecas vendidas hay?"))

peso = peso_muneca * cantidad_munecas + peso_payaso * cantidad_payasos

print(f"El peso total es: {peso} g")