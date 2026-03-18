a = int(input("Insira o valor do primeiro lado do triângulo em cm: "))
b = int(input("Insira o valor do segundo lado do triângulo em cm: "))
c = int(input("Insira o valor do terceiro lado do triângulo em cm: "))

semiperimetro = (a + b + c) / 2
area_heron = semiperimetro * (semiperimetro - a) * (semiperimetro - b) * (semiperimetro - c)

isosceles = (a == b != c) or (a == c != b) or (c == b != a)
escaleno = a != b != c
equilatero = a == b == c
resultado_dict = {"Isósceles?": isosceles, "Escaleno?": escaleno, "Equilatero?": equilatero}

print("O triângulo é: \n", resultado_dict)
print(semiperimetro)
print(f"A área do triângulo é {area_heron} cm")
