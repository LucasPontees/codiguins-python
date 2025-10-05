class ContaBancaria:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.__saldo = saldo
    
    def depositar(self, saldo):
        if saldo <= 0:
            print("Adicione um valor válido!")
        else:
         self.__saldo += saldo

    def get_saldo(self):
       return self.__saldo

pessoa = ContaBancaria("lucas", 100)
pessoa.depositar(999)
print(f"Saldo Atual: {pessoa.get_saldo()}")
        