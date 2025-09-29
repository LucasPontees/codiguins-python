Aqui está uma implementação em Python que atende aos requisitos solicitados, utilizando apenas estruturas de dados básicas e sem funções:

```
Inicialização das matrizes de custo unitário e capacidade máxima
custo_unitario = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
capacidade_maxima = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
caixas_expedidas = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

Listas para armazenar pedidos e fila de expedição
pedidos = []
fila_expedicao = []
pilha_expedicao = []

Variáveis para relatórios
custo_por_deposito = [0, 0, 0]
custo_por_loja = [0, 0, 0]
custo_total = 0
urgentes_expedidos = 0
normais_expedidos = 0
com_risco_expedidos = 0

Cadastro das matrizes
print("Cadastro de custo unitário por caixa (R$)")
for i in range(3):
    for j in range(3):
        custo_unitario[i][j] = float(input(f"Depósito D{i+1} para Loja L{j+1}: R$"))

print("\nCadastro de capacidade máxima (Número de caixas)")
for i in range(3):
    for j in range(3):
        capacidade_maxima[i][j] = int(input(f"Depósito D{i+1} para Loja L{j+1}: "))

Registro de N pedidos
N = int(input("\nNúmero de pedidos a registrar: "))
for _ in range(N):
    codigo = input("Código do pedido: ")
    urgencia = input("Urgência (U/N): ").upper()
    peso = float(input("Peso (kg): "))
    qtd_caixas = int(input("Quantidade de caixas: "))
    deposito = int(input("Depósito (1, 2 ou 3): ")) - 1
    loja = int(input("Loja (1, 2 ou 3): ")) - 1
    
    custo_estimado = custo_unitario[deposito][loja] * qtd_caixas
    risco = peso > 20 or qtd_caixas > 100
    
    pedido = {
        'codigo': codigo,
        'urgencia': urgencia,
        'peso': peso,
        'qtd_caixas': qtd_caixas,
        'deposito': deposito,
        'loja': loja,
        'custo_estimado': custo_estimado,
        'risco': risco
    }
    pedidos.append(pedido)
    
    # Priorização na fila de expedição
    if urgencia == 'U':
        fila_expedicao.insert(0, pedido)
    elif peso <= 5:
        fila_expedicao.append(pedido)
    elif peso >= 20:
        fila_expedicao.append(pedido)
    else:
        fila_expedicao.append(pedido)

Ordenação da fila com prioridade: Urgente, Leves (peso <=5), Pesados (peso >=20), outros
fila_expedicao.sort(key=lambda x: (x['urgencia'] != 'U', not (x['peso'] <= 5), not (x['peso'] >= 20)))

while True:
    print("\nMenu:")
    print("1 - Expedir próximo")
    print("2 - Consultar próximo (sem remover)")
    print("3 - Desfazer última expedição")
    print("4 - Relatórios")
    print("5 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        if fila_expedicao:
            pedido = fila_expedicao.pop(0)
            deposito = pedido['deposito']
            loja = pedido['loja']
            qtd_caixas = pedido['qtd_caixas']
            
            if caixas_expedidas[deposito][loja] + qtd_caixas <= capacidade_maxima[deposito][loja]:
                caixas_expedidas[deposito][loja] += qtd_caixas
                pilha_expedicao.append(pedido)
                
                custo_por_deposito[deposito] += pedido['custo_estimado']
                custo_por_loja[loja] += pedido['custo_estimado']
                custo_total += pedido['custo_estimado']
                
                if pedido['urgencia'] == 'U':
                    urgentes_expedidos += 1
                else:
                    normais_expedidos += 1
                if pedido['risco']:
                    com_risco_expedidos += 1
                
                print(f"Pedido {pedido['codigo']} expedido.")
            else:
                print("Capacidade da rota excedida. Pedido não expedido.")
        else:
            print("Fila de expedição vazia.")
            
    elif opcao == '2':
        if fila_expedicao:
            pedido = fila_expedicao[0]
            print(f"Próximo pedido: {pedido['codigo']} (Urgência: {pedido['urgencia']}, Peso: {pedido['peso']}kg, Caixas: {pedido['qtd_caixas']})")
        else:
            print("Fila de expedição vazia.")
            
    elif opcao == '3':
        if pilha_expedicao:
            pedido = pilha_expedicao.pop()
            deposito = pedido['deposito']
            loja = pedido['loja']
            qtd_caixas = pedido['qtd_caixas']
            
            caixas_expedidas[deposito][loja] -= qtd_caixas
            
            custo_por_deposito[deposito] -= pedido['custo_estimado']
            custo_por_loja[loja] -= pedido['custo_estimado']
            custo_total -= pedido['custo_estimado']
            
            if pedido['urgencia'] == 'U':
                urgentes_expedidos -= 1
            else:
                normais_expedidos -= 1
            if pedido['risco']:
                com_risco_expedidos -= 1
                
            fila_expedicao.insert(0, pedido)
            print(f"Expedição do pedido {pedido['codigo']} desfeita.")
        else:
            print("Nenhuma expedição para desfazer.")
            
    elif opcao == '4':
        print("\nRelatórios:")
        print("a) Custo por rota (matriz 3x3):")
        for i in range(3):
            for j in range(3):
                print(f"D{i+1} -> L{j+1}: R${custo_unitario[i][j] * caixas_expedidas[i][j]:.2f}", end=' | ')
            print()
        
        print("\nb) Custo por depósito:", [f"D{i+1}: R${custo_por_deposito[i]:.2f}" for i in range(3)])
        print("c) Custo por loja:", [f"L{i+1}: R${custo_por_loja[i]:.2f}" for i in range(3)])
        print(f"d) Custo total: R${custo_total:.2f}")
        print(f"e) Pedidos expedidos - Urgentes: {urgentes_expedidos}, Normais: {normais_expedidos}, Com risco: {com_risco_expedidos}")
        
    elif opcao == '5':
        print("Saindo do sistema.")
        break
        
    else:
        print("Opção inválida.")
```

Este código implementa o sistema solicitado, permitindo o cadastro de matrizes de custo e capacidade, registro de pedidos, priorização em uma fila de expedição e operações de expedição, consulta, desfazer e relatórios através de um menu.
