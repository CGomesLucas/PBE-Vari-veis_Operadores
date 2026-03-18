velocidade = float(input("Qual a velocidade da internet em Mbps: "))
tempo_dowload = int(input("Quantos o tempo de dowload em segundos: "))

resultado = velocidade * tempo_dowload

print(f"A quantidade total de dados tranferidos em megabits é {resultado:.2f}")