try:
    y = 1 / 0
    
# Excepción más concreta
except (ZeroDivisionError, ArithmeticError):
    print("Hubo un problema al hacer la operación.")
except: # Excepción (sin nombre)
    # Todo lo demás cae aquí.
    print("Algo ha cascao aquí...")
    
print("FIN.")
    