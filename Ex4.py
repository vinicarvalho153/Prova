print('''Opções: 
[1]- Consultar saldo
[2]- Saque
[3]- Depósito
[4]- sair''')
inserirValor = int(input("Escolha uma opção: "))
consultarSaldo = 0
if inserirValor == 1:
    print(consultarSaldo)
elif inserirValor == 2:
    retirarSaque = float(input("Insira um valor de saque: "))
    valorRetirado = retirarSaque - consultarSaldo
    print(valorRetirado)
elif inserirValor == 3:
    inserirDeposito = float(input("insira um valor de deposito: "))
    valorDepositado = inserirDeposito + consultarSaldo
    print(valorDepositado)
elif inserirValor == 4:
    print("Até a proxima!")
