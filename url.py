pilha = []  

while True:
    print("MENU\n")
    print("1 - digitar nova URL")
    print("2 - voltar pagina")
    print("3 - mostrar pagina atual")
    print("0 - sair")
    
    opcao = input("escolha uma opção: ")

    if opcao == "1":
        url = input("digite a URL: ")
        pilha.append(url) 
        print("pagina aberta:", url)
    elif opcao == "2":
        if len(pilha) > 1:
            pilha.pop() 
            print("voltando para:", pilha[-1])
        elif len(pilha) == 1:
            print("so tem uma página, não dá pra voltar.")
        else:
            print("nenhuma página no histórico.")
    elif opcao == "3":
        if len(pilha) > 0:
            print("pagina atual:", pilha[-1])
        else:
            print("nenhuma pagina aberta.")
    elif opcao == "0":
        print("saindo...")
        break
    else:
        print("opção inválida, tente de novo.")
