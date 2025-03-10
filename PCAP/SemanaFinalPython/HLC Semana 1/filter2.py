import random

'''
Ejemplo simple de uso de filtro (filter).
'''

# Genera una lista de números aleatorios entre -10 y 10, crea un filtro 
# que seleccione los números pares positivos y muestra el resultado en pantalla. 

num_aleatorios = [random.randint(-10, 10) for _ in range(10)]

pares_positivos = list(filter(lambda x: x % 2 == 0 and x > 0, num_aleatorios))


print("Números aleatorios: ", num_aleatorios)
print("Nñumeros pares positivos: ", pares_positivos)

print("Julio Muñoz de Hoces")
