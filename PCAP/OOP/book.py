class Book:
    #Constructor
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        #Si pones __ es un atributo privado
        self.__price = price
        self.__discount = None
        
    #Método set
    def set_discount(self, discount):
        self.__discount = discount
        
    #Función get
    def get_price(self):
        if self.__discount:
            return self.__price * (1-self.__discount)
        return self.__price
    
    def __repr__(self):
        return f"Título:\'{self.title}\', Cantidad: {self.quantity}, Autor: {self.author}, Precio: {round(self.get_price(),3)} €"
                
book1 = Book('El Señor de los anillos', 30, 'J.R.R. Tolkien', 22)
book2 = Book('El cuanto de la criada', 20, 'Margaret Atwood', 30)
book3 = Book('Reina Roja', 25, 'Juan Gómez Jurado', 28)

print(book1)
print(book2)
print(book3)

print(book1.title)
print(book1.quantity)
print(book1.author)
print(book1.get_price())
