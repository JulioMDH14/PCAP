class Item:
    def __init__(self,nombre,tipo,rareza):
        self.nombre = nombre
        self.tipo = tipo
        self.rareza = rareza
        
class InventarioLlenoError(Exception):
    "El inventario está lleno"
    pass

class Personaje:
    def __init__(self,nombre):
        self.nombre = nombre
        self.inventario = []
        
    def agregar_item(self,item):
        if type(item).__name__ == "Item":
            try:
                if(len(self.inventario) < 5):
                    self.inventario.append(item)
                    print("Item insertado al inventario")
                else:
                    raise InventarioLlenoError
            except InventarioLlenoError:
                print(f"El inventario de {self.nombre} está lleno")
                
    def mostrarInventario(self):
        for i in self.inventario:
            print(i.nombre)
            
    def borrarItem(self,item):
        self.inventario.remove(item)
            
            
item1 = Item("Espada","Arma blanca","Rara")
item2 = Item("Escudo","Protección","Simple")
item3 = Item("Hacha","Herramienta","Épica")
item4 = Item("Casco","Vestimenta","Normal")
item5 = Item("Blue label","Elixir","Exquisita")
item6 = Item("Ronaldinho","Jugador","Icono")

mario = Personaje("Mario")
mario.agregar_item(item1)
mario.agregar_item(item2)
mario.agregar_item(item3)
mario.agregar_item(item4)
mario.agregar_item(item5)
mario.agregar_item(item6)
print("-------------")
mario.mostrarInventario()
print("-------------")
mario.borrarItem(item2)

mario.mostrarInventario()
