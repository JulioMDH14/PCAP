fecha = ''

while True:
    fecha = input("Introduce tu fecha de nacimiento AAAAMMDD: ")
    if fecha.isnumeric():
        break
    print("Debes introducir una fecha en formato AAAAMMDD")
    
digito = 0
suma = 0

for c in fecha:
    suma += int(c)
if suma < 10:
    digito = suma
else:
    for c in str(suma):
        digito += int(c)
        
print("Tu dígito de vida es ", digito)