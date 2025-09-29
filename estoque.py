# Programa para cadastrar 3 produtos

produtos = []

for i in range(3):
    print(f"\nCadastro do produto {i+1}:")
    descricao = input("Descrição: ")
    preco = float(input("Preço: R$ "))
    quantidade = int(input("Quantidade: "))

    produto = {
        "descricao": descricao,
        "preco": preco,
        "quantidade": quantidade
    }

    produtos.append(produto)

# Exibindo os produtos cadastrados
print("\nProdutos cadastrados:")
for p in produtos:
    print(f"- {p['descricao']} | Preço: R$ {p['preco']:.2f} | Quantidade: {p['quantidade']}")

print(max(produtos['preco']))
print(min(produtos['preco']))