lista = [('gif','image/gif'),('jpg','image/jpeg'),('jpeg','image/jpeg'),('png','image/png'),('pdf','application/pdf'),('txt','text/plain'),('zip','application/zip')]

nombre = str(input("Ingrese el nombre de su archivo: "))
final = nombre.rsplit('.')
tipo = final[-1]

tupla = next((tupla for tupla in lista if tupla[0] == tipo), None)

if tupla:
    segundo_factor_gif = tupla[1]
    print(segundo_factor_gif)
else:
    print("application/octet-stream")
