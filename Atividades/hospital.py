class Paciente:
    def __init__(self, nome, idade, cpf, doenca):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.doenca = doenca
    
    def exibirPaciente(self):
        print('----Formulário----')
        print(f'Nome do paciente: {self.nome}\n')
        print(f'Idade do paciente: {self.idade}\n')
        print(f'Documento do paciente: {self.cpf}\n')
        print(f'Doenca do paciente: {self.doenca}\n')

    def atualizarDoenca(self, novaDoenca):
        self.doenca = novaDoenca    
        print(f"Doença atualizada: {self.doenca}")

paciente1 = Paciente("Lucas", 25, "000.000.000-00", "Virose")
paciente1.exibirPaciente()

paciente2 = Paciente("Hugo", 35, "000.000.000-01", "Virose")
paciente2.exibirPaciente()
paciente2.atualizarDoenca("Dor de cabeça")
