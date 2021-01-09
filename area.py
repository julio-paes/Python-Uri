a, b, c = [float(x) for x in input().split()]

area_triangulo = a * c / 2

print("TRIANGULO: {:.3f}" .format(area_triangulo))


area_circulo = 3.14159 * c ** 2

print("CIRCULO: {:.3f}" .format(area_circulo))


area_trapezio = (a + b) * c / 2

print("TRAPEZIO: {:.3f}" .format(area_trapezio))


area_quadrado = b * b

print("QUADRADO: {:.3f}" .format(area_quadrado))

area_retangulo = a * b

print("RETANGULO: {:.3f}" .format(area_retangulo))
