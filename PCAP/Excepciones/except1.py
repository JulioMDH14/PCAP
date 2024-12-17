try:
    y = 1 / 0
    
# Excepción más concreta
except ZeroDivisionError:
    print("¡División entre cero!")
# Excepción más abstracta/general
except ArithmeticError:
    print("¡Problema Aritmético!")
except: # Excepción (sin nombre)
    # Todo lo demás cae aquí.
    print("Algo ha cascao aquí...")
    
print("FIN.")
    