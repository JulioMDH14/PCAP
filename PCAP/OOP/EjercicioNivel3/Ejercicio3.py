import random

class Personaje:
    def __init__(self,nombre,vida,ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        
    def atacar(self,personaje):
        if type(personaje).__name__ == "Personaje":
            esquivar = personaje.esquivar()
            try:
                if personaje.vida > 0 and esquivar == False:
                    personaje.vida = personaje.vida - self.ataque
                    print(f"El aventurero {self.nombre} ha atacado a {personaje.nombre}")
                    print(f"A {personaje.nombre} le quedan {personaje.vida} puntos de vida")
                elif personaje.vida > 0 and esquivar == True:
                    personaje.vida = personaje.vida
                    print(f"El aventurero {personaje.nombre} ha esquivado el ataque de {self.nombre}")
            except:
                raise Exception(f"El aventurero {personaje.nombre} se ha debilitado")
        else:
            print(f"El objeto {personaje.nombre} no es un personaje")
            
    def esquivar(self):
        probabilidad = random.randrange(1,10)
        if probabilidad <= 5:
            return True
        else:
            return False
        
            
marcos= Personaje("Marcos",100,40)
pepe = Personaje("Pepe",100,50)

marcos.atacar(pepe)
pepe.atacar(marcos)
pepe.atacar(marcos)
marcos.atacar(marcos)
