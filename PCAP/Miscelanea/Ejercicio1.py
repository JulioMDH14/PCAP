import random
def generador_nombres():
    listaNombres = ["Romario","Lolito","Humberto","Fede","Ronaldinho"]
    random.shuffle(listaNombres)
    for nombre in listaNombres:
        yield nombre
        
generador = generador_nombres()

for x in range(5):
    print(next(generador))
    