tempo = int(input("Insira o tempo em minutos para imprimir uma peça:"))
qtd = int(input("insira a quantidade de peças produzidas:"))

conversao = tempo / 60
resultado = conversao * qtd

print(f"O tempo total de produção em hora é {resultado} horas")