class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Ola, meu nome eh {self.nome} e tenho {self.idade} anos.")

pessoa1 = Pessoa("Lucas", 25)
pessoa1.apresentar()