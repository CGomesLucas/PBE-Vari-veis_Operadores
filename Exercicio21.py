#Primeira maneira

import math

a = int(input("Insira o valor do primeiro lado do triângulo em cm: "))
b = int(input("Insira o valor do primeiro lado do triângulo em cm: "))
c = int(input("Insira o valor do primeiro lado do triângulo em cm: "))

semiperimetro = (a + b + c) / 2
area = math.sqrt(semiperimetro * (semiperimetro - a) * (semiperimetro - b) * (semiperimetro - c))

nomes = ["Equilátero", "Isósceles", "Escaleno"]
tipo = nomes[len({a, b, c})-1]

print(f"\nO triângulo é: {tipo}")
print(f"Área: {area:.2f} cm²")

#Segunda maneira

import math

a = int(input("Insira o valor do primeiro lado do triângulo em cm: "))
b = int(input("Insira o valor do segundo lado do triângulo em cm: "))
c = int(input("Insira o valor do terceiro lado do triângulo em cm: "))

semiperimetro = (a + b + c) / 2
area_heron = math.sqrt(semiperimetro * (semiperimetro - a) * (semiperimetro - b) * (semiperimetro - c))

lados = len({a,b, c})

tipo_dict = {
     1: "Equilátero",
     2: "Isósceles",
     3: "Escaleno",
 }
print(f"O triângulo é: {tipo_dict[lados]}", )
print(f"O semiperimetro é {semiperimetro} cm")
print(f"A área do triângulo é aproximadamente {area_heron:.2f} cm²")

#Terceira maneira

import math

a = int(input("Insira o valor do primeiro lado do triângulo em cm: "))
b = int(input("Insira o valor do segundo lado do triângulo em cm: "))
c = int(input("Insira o valor do terceiro lado do triângulo em cm: "))

semiperimetro = (a + b + c) / 2
area_heron = math.sqrt(semiperimetro * (semiperimetro - a) * (semiperimetro - b) * (semiperimetro - c))

isosceles = (a == b != c) or (a == c != b) or (c == b != a)
escaleno = a != b != c
equilatero = a == b == c

resultado_dict = {"Isósceles?": isosceles, "Escaleno?": escaleno, "Equilatero?": equilatero}

print("O triângulo é:\n", resultado_dict)
print(f"O semiperimetro é {semiperimetro} cm")
print(f"A área do triângulo é aproximadamente {area_heron:.2f} cm²")
