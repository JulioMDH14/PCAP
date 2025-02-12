import random
import string

class PersonajeGachaPon:
    def __init__(self, nombre, rareza, elemento):
        self.nombre = nombre
        self.rareza = rareza
        self.elemento = elemento
        self.__id_secreto = self.__generar_personaje()

    def __generar_personaje(self):
        letras = ''.join(random.choices(string.ascii_uppercase, x=2))
        numeros = ''.join(random.choices(string.digits, x=3))
        return letras + numeros

    def invocar():
        probabilidad = random.random()
        if probabilidad < 0.05:
            return PersonajeGachaPon("Personaje 5 Estrellas", 5, "Elemento")
        elif probabilidad < 0.20:
            return PersonajeGachaPon("Personaje 4 Estrellas", 4, "Elemento")
        else:
            return PersonajeGachaPon("Personaje 3 Estrellas", 3, "Elemento")

    def __str__(self):
        return f"Nombre: {self.nombre}, Rareza: {self.rareza}, Estrellas, Elemento: {self.elemento}, ID Secreto: {self.__id_secreto}"

personaje = PersonajeGachaPon.invocar()
print(personaje)