class Restaurante:
    def __init__(self, nome: str, cardapio: list):
        self.__nome = nome
        self.__cardapio = cardapio

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, novo_nome: str):
        if novo_nome != "":
            self.__nome = novo_nome
            print(f"Nome atualizado para: {self.__nome}")

    def adicionar_prato(self, prato: str):
        self.__cardapio.append(prato)
        print(f"Prato '{prato}' adicionado ao cardápio.")

    def listar_cardapio(self):
        print(f"Cardápio do {self.__nome}:")
        for prato in self.__cardapio:
            print(f"- {prato}")

    def atender_cliente(self, nome_cliente: str, prato_escolhido: str):
        if prato_escolhido in self.__cardapio:
            print(f"Atendendo {nome_cliente}. Seu pedido de '{prato_escolhido}' está sendo preparado.")
        else:
            print(f"Desculpe, {nome_cliente}. O prato '{prato_escolhido}' não está disponível no cardápio.")

saborCaseiro = Restaurante("Sabor Caseiro", ["Lasanha", "Frango com quiabo", "Bife acebolado"])
saborCaseiro.adicionar_prato("Feijoada")
saborCaseiro.listar_cardapio()
saborCaseiro.atender_cliente("Hugo", "Panqueca")
saborCaseiro.set_nome("Sabor & Cia")