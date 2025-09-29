import numpy as np
matriz = np.zeros((3, 3), dtype=int)

for i in range(3):       
    for j in range(3):   
        valor = int(input(f"Digite um valor para posição ({i}, {j}): "))
        matriz[i][j] = valor

print("\nMatriz preenchida:")
for linha in matriz:
    print(linha)
