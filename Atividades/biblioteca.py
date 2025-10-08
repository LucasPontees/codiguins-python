class Biblioteca:
    def __init__(self, nome: str, livros: list):
        self.__nome = nome
        self.__livros = livros
    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, novo_nome: str):
        if novo_nome != "":
            self.__nome = novo_nome
            print(f"Nome atualizado para: {self.__nome}")
    
    def adicionar_livro(self, titulo: str):
        if(titulo != "" and titulo not in self.__livros):
            self.__livros.append(titulo)
            print(f"Livro '{titulo}' adicionado à biblioteca.")
        else:
            print(f"Livro '{titulo}' já está na biblioteca ou título inválido.")

    def listar_livros(self):
        if len(self.__livros) == 0:
            print("Nenhum livro disponível na biblioteca.")
        else:
            print(f"Livros disponíveis na biblioteca {self.__nome}:")
            for livro in self.__livros:
                print(f"- {livro}")
    
bibliotecaCentral = Biblioteca("Biblioteca Central", ["titulo 1", "titulo 2", "titulo 3"])
bibliotecaCentral.adicionar_livro("titulo 3")
bibliotecaCentral.listar_livros()
bibliotecaCentral.set_nome("Biblioteca Central 2")
bibliotecaCentral.get_nome()