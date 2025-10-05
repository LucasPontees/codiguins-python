# Classe Pai (Superclasse)
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print("O animal faz um som.")

# Classe Filha (Subclasse)
class Cachorro(Animal):
    def falar(self):  # sobrescrita de método
        print(f"{self.nome} diz: Au Au!")

class Gato(Animal):
    def falar(self):  # sobrescrita de método
        print(f"{self.nome} diz: Miau!")


dog = Cachorro("Rex")
cat = Gato("Mimi")

dog.falar()  # Rex diz: Au Au!
cat.falar()  # Mimi diz: Miau!
