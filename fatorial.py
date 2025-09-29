numero_fatorial = 0

contador = 1
while numero_fatorial != 1:
  numero_fatorial = int(input("Digite um número: "))
  while numero_fatorial != 0:
    fatorial = numero_fatorial * contador
    contador += 1
    numero_fatorial -= 1
    print(fatorial)
    if numero_fatorial ==0:
        continue