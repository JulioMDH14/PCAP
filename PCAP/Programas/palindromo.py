frase = input("Introduce una frase: ")

frase2 = (frase.lower()).replace(' ','')

if frase2 == frase2[::-1]:
    print("La frase ", frase2 , " es un palindromo")
else:
    print("No son palindromos")