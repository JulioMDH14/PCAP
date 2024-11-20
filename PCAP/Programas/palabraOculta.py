#Encuentra la palabra oculta

palabra = input("Introduce la palabra a buscar: ").upper()
grupo = input("Introduce grupo de caracteres: ").upper()

contiene = True
posicion = 0

for c in palabra:
    contador = grupo.find(c, posicion)
    if contador < 0:
        contiene = False
        break
    contador = posicion + 1
if contiene:
    print("La palabra si se encuentra dentro")
else:
    print("La palabra no se encuentra dentro")
	   