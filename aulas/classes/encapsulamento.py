class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular    # público
        self._tipo = "Conta Corrente"  # protegido (por convenção)
        self.__saldo = saldo      # privado

    def depositar(self, valor):
        self.__saldo += valor

    def get_saldo(self):
        return self.__saldo

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente!")

    def extrato(self):
        print(f"Saldo de {self.titular}: R$ {self.__saldo}")


conta = ContaBancaria("Ana", 1000)
conta.depositar(500)
conta.extrato()

# 🚨 Acessando diretamente
print(conta.titular)      # OK (público)
print(conta._tipo)        # OK mas não recomendado (protegido)
print(conta.get_saldo())    # ERRO → atributo privado
