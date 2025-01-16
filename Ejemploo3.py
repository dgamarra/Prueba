def calcular_area_rectangulo(altura, base):
    return  altura * base

def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

if __name__ == '__main__':
    base = 4
    altura = 6
    rectangulo_area = calcular_area_rectangulo(base, altura)
    print("Área del rectángulo:", rectangulo_area)

    base = 5
    altura = 8
    tringulo_area = calcular_area_triangulo(base, altura)
    print("Área del triángulo:", tringulo_area)

