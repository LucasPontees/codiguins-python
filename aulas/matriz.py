import numpy as np

matriz = np.zeros((3, 3), dtype=int) 

while True:
    print(f"Matriz atual: \n{matriz}")
    linhaAdicionar = int(input("Digite a linha: \n"))
    colunaAdicionar = int(input("Digite a coluna: \n"))
    if matriz[linhaAdicionar, colunaAdicionar] != 0:
        print("Posição já contem valor!\n")
        continue
    valor = int(input("Qual valor quer adicionar ? \n"))
    matriz[linhaAdicionar, colunaAdicionar] = valor
    print(matriz)