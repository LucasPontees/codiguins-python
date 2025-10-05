class Animal:
    def falar(self):
        pass   # método genérico (abstrato aqui)

class Cachorro(Animal):
    def falar(self):
        return "Au Au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

class Vaca(Animal):
    def falar(self):
        return "Muuu!"

# Polimorfismo em ação
animais = [Cachorro(), Gato(), Vaca()]

for animal in animais:
    print(animal.falar())
