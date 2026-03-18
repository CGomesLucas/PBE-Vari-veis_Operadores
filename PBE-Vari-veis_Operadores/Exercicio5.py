preco_licenca = float(input("Digite o preco da licença:"))
qtd_desenvolvedores = int(input("Insira a quantidade de desenvolvedores:"))

resultado = preco_licenca * qtd_desenvolvedores

print(f"O custo total da compra das licenças foi R${resultado:.2f}")
