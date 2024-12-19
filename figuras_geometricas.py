# Calculadora das areas das formas geométricas
def calcular_area_quadrado(lado):
    area = lado * lado
    return area

def calcular_area_retangulo(altura, base):
    area = altura * base
    return area

def calcular_area_circulo(raio):
    area = 3.14 * raio * raio
    return area

def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

def calcular_area_trapezio(base_maior, base_menor, altura):
    area = ((base_maior + base_menor) * altura) / 2
    return area

def calcular_area_paralelogramo(base, altura):
    area = base * altura
    return area

def calcular_area_losangulo(diagonal_maior, diagonal_menor):
    area = (diagonal_maior * diagonal_menor) /2
    return area

def calcular_area_cubo(lado):
    area = 6 * (lado *lado)
    return area


figura = str(input("Digite o nome da forma geométrica: "))

if figura=="retangulo":
    altura = float(input("Digite a medida da altura do retângulo: "))
    base = float(input("Digite a medida da base do retângulo: "))
    area = calcular_area_retangulo(altura, base)
    print(f"A área do retângulo é {area}")

elif figura=="quadrado":
    lado = float(input("Digite a medida do lado do quadrado: "))
    area = calcular_area_quadrado(lado)
    print(f"A área do quadrado é: {area}")

elif figura=="circulo":
    raio = float(input("Digite a medida do raio do circulo: "))
    area = calcular_area_circulo(raio)
    print(f"A área do circulo é: {area}")

elif figura == "triangulo":
    base = float(input("Digite a medida da base do triangulo: "))
    altura = float(input("Digite a medida da altura do triangulo: "))
    area = calcular_area_triangulo(base, altura)
    print(f"A área do triangulo é: {area}")

elif figura == "trapezio":
    base_maior = float(input("Digite a medida da base maior do trapezio: "))
    base_menor = float(input("Digite a medida da base menor do trapezio: "))
    altura = float(input("Digite a medida da altura do trapezio: "))
    area = calcular_area_trapezio(base_maior, base_menor, altura)
    print(f"A área do trapezio é: {area}")

elif figura == "paralelogramo":
    base = float(input("Digite a medida da base do paralelogramo: "))
    altura = float(input("Digite a medida da altura do paralelogramo: "))
    area = calcular_area_paralelogramo(base, altura)
    print(f"A área do paralelogramo é: {area}")

elif figura == "losangulo":
    diagonal_maior = float(input("Digite a medida da diagonal maior do losangulo: "))
    diagonal_menor = float(input("Digite a medida da diagonal menor do losangulo: "))
    area = calcular_area_losangulo(diagonal_maior, diagonal_menor)
    print(f"A área do losangulo é: {area}")

elif figura == "cubo":
    lado = float(input("Digite a medida do lado do cubo: "))
    area = calcular_area_cubo(lado)
    print(f"A área do cubo é: {area}")

else:
    print("Figura geométrica não encontrada, tente novamente.")


