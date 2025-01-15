class Empleado:
    
    def __init__(self,nombre,apellidos,cargo,salario = 1000):
        self.nombre = nombre
        self.apellidos = apellidos
        self.cargo = cargo
        self.__salario = salario
        
    def getSalario(self):
        return self.__salario
    
    def __str__(self):
        return f"{self.nombre} ({self.cargo}) gana : {round(self.getSalario())}€"
    
listaEmpleados = [
    Empleado("Julio","Muñoz de Hoces","Programador",5500),
    Empleado("Yonarkeison","Pirueta Valeria Locura","Director",2000),
    Empleado("Manuel","Segura","Secretario",6500)
]

empleados_vip = [ empleado for empleado in listaEmpleados if empleado.getSalario() > 5000]
for e in empleados_vip:
    print(e)


