# Cifrado César.
text = input("Ingresa tu mensaje: ")
shift = 0;
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
    
    if char.isupper():
        first = ord('A')
    else:
        first = ord('a')
        
    code = (code - first) % 26
    
    cipher += chr(first + code)
    
print(cipher)