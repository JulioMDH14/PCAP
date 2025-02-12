class Pokemon:
    def __init__(self,nombre,tipo,vida,ataque):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida
        self.ataque = ataque
        
    def atacar(self, pokemon):
        if type(pokemon).__name__ == "Pokemon":
            try:
                if pokemon.vida > 0:
                    pokemon.vida = pokemon.vida - self.ataque
                    print(f"El pokemon {self.nombre} ha atacado a {pokemon.nombre}")
                    print(f"A {pokemon.nombre} le quedan {pokemon.vida} puntos de vida")
            except:
                raise Exception(f"El pokemon {pokemon.nombre} se ha debilitado")
        else:
            print(f"El pokemon {pokemon.nombre} no es un pokemon")
            
squirtle = Pokemon("Squirtle","Agua",100,10)
charmander = Pokemon("Charmander","Fuego",100,20)

squirtle.atacar(charmander)
charmander.atacar(squirtle) 



