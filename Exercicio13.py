tamanho_log = int(input("Digite o tamanho médio do log em MB (megavytes):"))
logs_por_dia = int(input("Digite a quantidade de logs por dia:"))

resultado = tamanho_log * logs_por_dia

print(f"O tamanho total de logs gerados em um dia é de {resultado} MB")