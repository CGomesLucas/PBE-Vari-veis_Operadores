tempo_execucao = int(input("Insira o tempo de execução da tarefa em segundos: "))
qtd_tarefas_executadas = int(input("Insira o quantidade de tarefas que foram executadas: "))

resultado = (tempo_execucao / 60) * qtd_tarefas_executadas

print(f"O tempo total em minutos é {resultado} minutos")