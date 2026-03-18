valor_mensal = float(input("Insira o valor mensal:"))
qtd_meses_contratados = int(input("Insira a quantidade de meses constratados: "))

resultado = valor_mensal * qtd_meses_contratados

print(f"O valor total a ser pago é R${resultado:.2f}")
