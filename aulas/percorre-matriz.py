import numpy as np

matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

for i in range(matriz.shape[0]):      
    for j in range(matriz.shape[1]):  
        print(f"Posição ({i}, {j}) → {matriz[i, j]}")
