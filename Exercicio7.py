qtd_pecas_por_minuto = int(input("Quantos peças são montadas por minuto: "))
temp_operacao_minutos = int(input("Qual o tempo de operação em minutos: "))

resultado = temp_operacao_minutos / qtd_pecas_por_minuto

print(f"A quantidade total de peças produzidas dentro de {temp_operacao_minutos} minutos foi {resultado} peças")