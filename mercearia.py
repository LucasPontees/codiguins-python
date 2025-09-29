nomes = [""] * 10       
quantidades = [0] * 10  

while True:
    print("\n===== MENU =====")
    print("1 - inclusão de novo produto")
    print("2 - alteração de quantidade")
    print("3 - exclusão de produto")
    print("4 - impressão dos produtos cadastrados")
    print("5 - consulta por nome do produto")
    print("6 - sair")

    opcao = int(input("escolha uma opção: "))

    if opcao == 1:
        pos = -1
        for i in range(10):
            if nomes[i] == "":
                pos = i
                break
        if pos == -1:
            print("não há espaço para novos produtos!")
        else:
            nomes[pos] = input("nome do produto: ")
            quantidades[pos] = int(input("quantidade: "))
            print("produto cadastrado!")

    elif opcao == 2:
        nome_prod = input("digite o nome do produto para alterar a quantidade: ")
        encontrado = 0
        for i in range(10):
            if nomes[i] == nome_prod:
                quantidades[i] = int(input("nova quantidade: "))
                print("quantidade atualizada!")
                encontrado = 1
                break
        if encontrado == 0:
            print("produto não encontrado.")

    elif opcao == 3:
        nome_prod = input("digite o nome do produto para excluir: ")
        encontrado = 0
        for i in range(10):
            if nomes[i] == nome_prod:
                encontrado = 1
                for j in range(i, 9):
                    nomes[j] = nomes[j + 1]
                    quantidades[j] = quantidades[j + 1]
                nomes[9] = ""
                quantidades[9] = 0
                print("produto excluído!")
                break
        if encontrado == 0:
            print("produto não encontrado.")

    elif opcao == 4:
        print("\nprodutos cadastrados:")
        for i in range(10):
            if nomes[i] != "":
                print(f"{nomes[i]} - quantidade: {quantidades[i]}")

    elif opcao == 5:
        nome_prod = input("digite o nome do produto para consultar: ")
        encontrado = 0
        for i in range(10):
            if nomes[i] == nome_prod:
                print(f"produto: {nomes[i]} - quantidade: {quantidades[i]}")
                encontrado = 1
                break
        if encontrado == 0:
            print("produto não encontrado.")

    elif opcao == 6:
        print("saindo do programa...")
        break

    else:
        print("opção inválida!")
