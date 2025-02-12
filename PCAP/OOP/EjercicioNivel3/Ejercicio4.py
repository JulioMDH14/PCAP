class Carta:
    def __init__(self, nombre, ataque,defensa,tipo):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.tipo = tipo
    
    
class Jugador:
    def __init__(self):
        self.mazo = []
    
    def agregar_carta(self,carta):
        if type(carta).__name__ == "Carta":
            self.mazo.append(carta)
    
    def invocar_carta(self,carta):
        if type(carta).__name__ == "Carta":
            try:
                if carta not in self.mazo:
                    print(f"La carta {carta.nombre} no está en el mazo")
                else:
                    print(f"El jugador ha lanzado la carta {carta.nombre}")
            except:
                raise Exception(f"No se ha lanzado la carta")
        else:
            print(f"Ese objeto no es una carta")
            
jugador = Jugador()

carta1 = Carta("Mago místico",200,50,"Rara")
carta2 = Carta("Dragón morado",300,150,"Legendaria")

jugador.agregar_carta(carta2)
jugador.invocar_carta(carta2)
jugador.invocar_carta(carta1)