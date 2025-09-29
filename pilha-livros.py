from collections import deque

pilha = deque()

for i in range(10):
    livro = input(f"digite o nome do livro {i+1}: ")
    pilha.append(livro)
    print(f"livro '{livro}' adicionado na pilha.")

print("pilha completa\n")
print(pilha)

print("livro no topo da pilha:\n", pilha[-1])

removido = pilha.pop()
print(f"livro removido da pilha:\n {removido}")

print("pilha atual:\n", pilha)
