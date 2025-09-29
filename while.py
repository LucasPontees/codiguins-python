
n = 0

while n < 1:
    n = int(input("Digite um valor: "))
    if n < 1:
        print("O valor precisa ser maior que 0")

contador = 1
while contador <= 10:
    print(f"{n} x {contador} = {n * contador}")
    contador += 1