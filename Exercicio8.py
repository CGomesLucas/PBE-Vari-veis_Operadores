qtd_cameras = int(input("Qual a quantidade de cameras: "))
preco_camera = float(input("Qual o preço de cada camera: "))
custo_servico = float(input("QUal o custo de instalação das câmeras: "))

resultado = qtd_cameras * preco_camera + custo_servico

print(f"O custo total do sistema de câmeras: R${resultado:.2f}")