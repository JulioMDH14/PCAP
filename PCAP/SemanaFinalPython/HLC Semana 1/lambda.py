''' Funciones lambda (0) '''


# (1) Función lambda que calcula el área de un triángulo

area_triangulo = lambda base, altura: (base * altura) / 2
print("Área triángulo = ",area_triangulo(20,30))

# (2) Función lambda que calcula el cubo de un número entero

al_cubo = lambda x: pow(x,3)
print("Potencia al cubo = ", al_cubo(10))

# (3) Función lambda que modifica la salida de una cadena (string)

destacar_valor = lambda cadena: f"¡¡¡{cadena}!!!"

comision_empleado_1 = 15500

print(destacar_valor(comision_empleado_1))

print("Julio Muñoz de Hoces")