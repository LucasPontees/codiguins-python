onibus = 0
carro = 0
moto = 0
bicicleta = 0
outros = 0
somaGastoBike = 0
qtdBike = 0
zonaNorteOutros = 0
zonaSulCarro = 0
somaIdadeMulheresOnibus = 0
qtdMulheresOnibus = 0

while True:
    print("\nmeio de transporte principal:")
    print("1-onibus | 2-carro | 3-moto | 4-bicicleta | 5-outros | 0-encerrar")
    transporte = int(input("digite a opção: "))

    if transporte == 0:
        break
    if transporte < 1 or transporte > 5:
        print("Opcao invalida")
        continue

    print("\nzona de moradia:")
    print("1-zona norte | 2-zona sul | 3-outros")
    
    zona = int(input("digite a opção: "))
    gasto = float(input("\ngasto mensal com transporte (R$): "))
    idade = int(input("\nidade: "))

    print("\ngenero:")
    print("1-feminino | 2-masculino | 3-outro")
    genero = int(input("digite a opção: "))

    if transporte == 1:
        onibus += 1
    elif transporte == 2:
        carro += 1
    elif transporte == 3:
        moto += 1
    elif transporte == 4:
        bicicleta += 1
        somaGastoBike += gasto
        qtdBike += 1
    elif transporte == 5:
        outros += 1

    if zona == 1 and transporte == 5:
        zonaNorteOutros += 1

    if zona == 2 and transporte == 2:
        zonaSulCarro += 1

    if genero == 1 and transporte == 1:
        somaIdadeMulheresOnibus += idade
        qtdMulheresOnibus += 1


print("\n===== menu de resultado =====")
print(f"onibus: {onibus}")
print(f"carro: {carro}")
print(f"moto: {moto}")
print(f"bicicleta: {bicicleta}")
print(f"outros: {outros}")

if qtdBike > 0:
    print(f"media de gasto dos ciclistas: R${somaGastoBike / qtdBike}")
else:
    print("nenhum usuario de bicicleta informado.")

print(f"zona norte usando 'outros': {zonaNorteOutros}")
print(f"zona sul usando 'carro':{zonaSulCarro}")

if qtdMulheresOnibus > 0:
    print(f"media de idade das mulheres que usam onibus: {somaIdadeMulheresOnibus / qtdMulheresOnibus}")
else:
    print("nenhuma mulher usuária de onibus informada.")
