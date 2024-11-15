# Cifrado César.
text = input("Ingresa tu mensaje: ")
shift = 0;
shift2 = 0;
while shift == 0:
    try:
        shift = int(input("Introduce cuanto quiere desplazarte: "))
    
        if shift not in range(1,26):
            raise ValueError
    except:
        print("ERROR: ¡Valor de cambio inválido!")
        shift = 0
        
        
text = text.upper()
cipher = ''
for char in text:
    code = ord(char) + shift
    first = ord('A')
    
    shift2 += (code - first) % 26
    cipher += chr(first + shift2)
print(cipher)