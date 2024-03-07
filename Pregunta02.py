consumo = int(input("Cuanto fue su consumo?"))
propina = int(input("Que porcentaje de propina desea dejar al mesero?"))

total = consumo + consumo *(propina / 100)

print(f"Su consumo total es {total}")