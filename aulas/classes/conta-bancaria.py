class ContaBancaria:
    def __init__(self, nome: str, saldo: float):
        self.nome = nome
        self.__saldo = saldo
    
    def depositar(self, saldo):
        if saldo <= 0:
            print("Adicione um valor válido!")
        else:
         self.__saldo += saldo
    def sacar(self, saque: float):
        if saque >= self.__saldo:
            print("Saldo acima do permitido!")
        else:
         self.__saldo = self.__saldo - saque
         print(self.__saldo)

    def get_saldo(self):
       return self.__saldo

pessoa = ContaBancaria("lucas", 100)
pessoa.sacar(99.99)
print(f"Saldo Atual: {pessoa.get_saldo()}")
        