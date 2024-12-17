import math
x = float(input("Ingresa un número: "))
try:
    assert x >= 0.0
    x = math.sqrt(x)
except AssertionError:
    print("El valor ha de ser mayor que 0")
    exit(1)
x = math.sqrt(x)
print(x)