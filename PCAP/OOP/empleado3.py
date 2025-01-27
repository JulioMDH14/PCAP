class Empleado:
    plantilla = []
    num_empleados = 0
    
    def __init__(self,nombre: str,cargo: str,salario=25000.50):
        if salario < 0:
            raise ValueError
            
        self.nombre = nombre
        self.cargo = cargo
        self.__salario = salario
        Empleado.plantilla.append(self)
        Empleado.num_empleados = Empleado.num_empleados + 1
        
        
    @staticmethod
    def is_integer(num):
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False   
        
    def get_salario(self):
        return self.__salario
    
    def __str__(self):
        return f"{self.nombre} trabaja de {self.cargo} y cobra {self.get_salario()}€"
    
empleado1 = Empleado("Julio","Programador",20000)
empleado2 = Empleado("Marcos","Director",50000)
empleado3 = Empleado("Juanjo","Conserje",10000)
empleado4 = Empleado("Sara","Marketing",30000)


for empleado in Empleado.plantilla:
    print(empleado)

#print(Empleado.plantilla[0])
#print(Empleado.plantilla[1])
#print(Empleado.plantilla[2])
#print(Empleado.plantilla[3])
#print(Empleado.num_empleados)

print(Empleado.__dict__)
print(Empleado.plantilla)


num1 = 7
num2 = 7.0
num3 = 7.5

if Empleado.is_integer(num1):
    print(num1," es entero.")
else:
     print(num1," NO es entero.")
     
if Empleado.is_integer(num2):
    print(num2," es entero.")
else:
     print(num2," NO es entero.")
     
if Empleado.is_integer(num3):
    print(num3," es entero.")
else:
     print(num3," NO es entero.")
