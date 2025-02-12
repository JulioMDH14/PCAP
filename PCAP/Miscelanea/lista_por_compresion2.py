mi_lista = []

for x in range(11):
    mi_lista.append(x % 2)
    
print(mi_lista)

mi_lista = [0 if x % 2 == 0 else 1 for x in range(11)]

print(mi_lista)