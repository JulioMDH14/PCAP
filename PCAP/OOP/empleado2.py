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