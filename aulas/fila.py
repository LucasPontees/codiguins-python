from collections import deque
import time

fila = deque()

while True:
    print("\n--- Sistema de Atendimento ---")
    print("1 - Adicionar cliente")
    print("2 - Atender cliente")
    print("3 - Mostrar fila")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do cliente: ")
        fila.append(nome)
        print(f"Cliente {nome} entrou na fila.")

    elif opcao == "2":
        if fila:
            cliente = fila.popleft()
            print(f"Atendendo cliente {cliente}...")
            time.sleep(1) 
            print(f"Cliente {cliente} atendido com sucesso!")
        else:
            print("Nenhum cliente na fila.")

    elif opcao == "3":
        print("Fila atual:", list(fila))

    elif opcao == "0":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida!")
