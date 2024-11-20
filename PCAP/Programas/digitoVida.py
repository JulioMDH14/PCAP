fecha = ''

while True:
    fecha = input("Introduce tu fecha de nacimiento AAAAMMDD: ")
    if fecha.isnumeric():
        break
    print("Debes introducir una fecha en formato AAAAMMDD")
    
digito = 0
suma = 0

for c in fecha:
    digito = int(c)
    suma = suma + digito
        
print("Tu dígito de vida es ", suma)