qtd_arquivos = int(input("Quantos arquivos estão armazenados?: "))
tamanho_medio = float(input("Qual o tamanho de cada arquivo em MB(Megabytes)?: "))

resultado = (qtd_arquivos * tamanho_medio) / 1000

print(f"O espaço total ocupado em GB é: {resultado:.2f} GB")

