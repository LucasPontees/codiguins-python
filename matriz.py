import numpy as np

n = 3
matriz = np.zeros((n, n), dtype=int)

preenchidos = 0
total = n * n

while preenchidos < total:
    print("\nMatriz atual:")
    print(matriz)

    try:
        linha = int(input(f"Digite a linha (0 a {n-1}): "))
        coluna = int(input(f"Digite a coluna (0 a {n-1}): "))
        valor = int(input("Digite o valor que deseja inserir: "))

        if 0 <= linha < n and 0 <= coluna < n:
            if matriz[linha, coluna] == 0:  # verifica se ainda não foi preenchido
                matriz[linha, coluna] = valor
                preenchidos += 1
            else:
                print("⚠️ Esse espaço já está preenchido!")
        else:
            print("⚠️ Posição inválida! Tente de novo.")
    except ValueError:
        print("⚠️ Entrada inválida! Digite apenas números.")

print("\n✅ Matriz final preenchida:")
print(matriz)
