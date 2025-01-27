class Reptil:
    def __init__(self,nombre):
        self.nombre = nombre
        
class Serpiente(Reptil):
    pass

class Culebra(Serpiente):
    pass

reptil1 = Reptil("Lagarto")
reptil2 = Serpiente("Mamba")
reptil3= Culebra("Culebra")

'''
print(Reptil.__name__);
print(type(reptil1).__name__)
print(type(reptil2).__name__)
print(type(reptil3).__name__)
'''
print(f"\t{Reptil.__name__}\t{Serpiente.__name__} {Culebra.__name__}")
for srp1 in [Reptil, Serpiente, Culebra]:
    print(srp1.__name__, end="\t")
    for srp2 in [Reptil, Serpiente, Culebra]:
        print(issubclass(srp1,srp2), end="\t")
    print()
print()

print(f"\t{type(reptil1).__name__}\t{type(reptil2).__name__} {type(reptil3).__name__}")
for obj in [reptil1, reptil2, reptil3]:
    print(obj.nombre, end="\t")
    for clase in [Reptil, Serpiente, Culebra]:
        print(isinstance(obj,clase), end="\t")
    print()
print()

reptil_1 = Reptil("Rana")
reptil_2 = Reptil("Vibora")
reptil_3 = Reptil("Cocodrilo")

reptil_1 = reptil_2
reptil_2 = reptil_3

print(reptil_1 == reptil_2, reptil_1 is reptil_2)
print(reptil_2 == reptil_3, reptil_2 is reptil_3)

reptil_1 = reptil_3
print(reptil_1 == reptil_3, reptil_1 is reptil_3)