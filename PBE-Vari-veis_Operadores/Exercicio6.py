qtd_computadores = int(input("Insira a quantidade de computadores: "))
qtd_memoriaRAM = int(input("Insira a quantidade de memoria RAM em GB de cada computador: "))

resultado = qtd_computadores * qtd_memoriaRAM

print(F"A quantidade de memória RAM em GB disponível no laboratório é {resultado:.2f}")