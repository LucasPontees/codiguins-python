class AvaliarAluno:
    def __init__(self, aluno, nota1, nota2):
     self.aluno = aluno
     self.nota1 = nota1
     self.nota2 = nota2

    
    def calularMedia(self):
        nota = self.nota1 + self.nota2
        return  nota
    
    def avaliar(self):
       media = self.calularMedia() /2
       if media >= 7:
          return(f"Aluno aprovado com média: {media}")
       else:
          return(f"Aluno reprovado com média: {media}")
          

lucas = AvaliarAluno("Lucas", 5, 7)
lucas.avaliar()
print(lucas.avaliar())