class Aluno:
    def __init__(self, nome: str, idade: int, curso: str):
        self.__nome = nome
        self.__idade = idade
        self.__curso = curso

    def get_nome(self):
        return self.__nome
    def set_nome(self, novo_nome: str):
        if novo_nome != "":
            self.__nome = novo_nome
            print(f"Nome atualizado para: {self.__nome}")

    def get_idade(self):
        return self.__idade
    
    def set_idade(self, nova_idade: int):
        if nova_idade > 0:
            self.__idade = nova_idade
            print(f"Idade atualizada para: {self.__idade}")

    def get_curso(self):
        return self.__curso
    
    def set_curso(self, novo_curso: str):
        if novo_curso != "":
            self.__curso = novo_curso
            print(f"Curso atualizado para: {self.__curso}")

    def apresentar(self):
        print(f"Aluno: {self.__nome}, Idade: {self.__idade}, Curso: {self.__curso}")

class Escola:
    def __init__(self, nome: str, alunos: list):
        self.__nome = nome
        self.__alunos = alunos

    def get_nome(self):
        return self.__nome
    def set_nome(self, novo_nome: str):
        if novo_nome != "":
            self.__nome = novo_nome
            print(f"Nome da escola atualizado para: {self.__nome}")
    
    def adicionar_aluno(self, aluno: Aluno):
        self.__alunos.append(aluno)
        print(f"Aluno '{aluno.get_nome()}' adicionado à escola.")

    def listar_alunos(self):
        if len(self.__alunos) == 0:
            print("Nenhum aluno matriculado na escola.")
        else:
            print(f"Alunos matriculados na escola {self.__nome}:")
            for aluno in self.__alunos:
                aluno.apresentar()

escolaFuturo = Escola("Escola do Futuro", [])
aluno1 = Aluno("Ana", 20, "Matemática")
aluno2 = Aluno("Bruno", 22, "Física")
escolaFuturo.adicionar_aluno(aluno1)
escolaFuturo.adicionar_aluno(aluno2)
escolaFuturo.listar_alunos()
aluno1.set_nome("Ana Clara")
escolaFuturo.listar_alunos()
