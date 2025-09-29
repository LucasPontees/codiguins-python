#lista = [10, 20, 30]
#lista.append(40)  # adiciona
#lista.remove(20)  # remove
#print(lista[0])   # acessar
lista = []
while True:
    escolha = int(input("1 - Adicionar a Lista\n2 - Remover da Lista\n0 - Sair\nEscolha: "))
    if escolha == 1:
        valorAdicionado = int(input("qual numero deseja adicionar a lista ?\n"))
        lista.append(valorAdicionado)
        print(lista)
    elif escolha == 2:
        print(lista)
        valorRemovido = int(input("qual numero deseja remover da lista ?\n"))
        lista.remove(valorRemovido)
        print(lista)
    elif escolha == 0:
        break
    else:
        print("opcao invalida!")
