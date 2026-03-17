preco = float(input("Digite o valor do produto: "))
valor_frete = float(input("Digite o valor do frete: "))
qtd_comprada = int(input("Digite a quantidade de itens comprados: "))

resultado = preco * qtd_comprada + valor_frete

print(f"O valor total da compra foi R${resultado:.2f}")