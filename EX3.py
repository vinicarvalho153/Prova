letraDaForca = 'a'
valorChances = 0
while valorChances <=5:
    inserirLetra = str(input("Digite uma Letra: "))
    if inserirLetra == letraDaForca:
        print("Voce acertou a forca!")
    else:
        print("Voce errou!")
        valorChances +=1
print("Acabou suas chances!")
