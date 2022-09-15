lerIdade = int(input("Digite sua idade: "))
lerTempoDeTrabalho = int(input("Digite seu tempo de trabalho: "))
if lerIdade >= 65 and lerTempoDeTrabalho >= 30:
    print("Voce pode se aposentar")
elif lerIdade >= 60 and lerTempoDeTrabalho == 25:
    print("Voce pode se aposentar")
else:
    print("Voce ainda nao pode se aposentar")