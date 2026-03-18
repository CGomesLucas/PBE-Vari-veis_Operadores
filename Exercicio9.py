tamanho_arquivo = int(input("Digite o tamanho do arquivo em MB(Megabytes): "))
qtd_arquivos = int(input("Digite a quantidade de arquivos: "))

resultado = (tamanho_arquivo * qtd_arquivos) / 1000

print(f"O tamanho total em GB é {resultado:.2f} GB ")