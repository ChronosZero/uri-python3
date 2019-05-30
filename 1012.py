#entrada dos dados
valores = input().split()

#conversao dos valores para float

for i in range(len(valores)):
    valores[i]=float(valores[i])

#identificação das variaveis

a = valores[0]
b = valores[1]
c = valores[2]
pi = 3.14159

#calculo das areas

triangulo = a*c / 2
circulo = pi * c**2
trapezio = (a + b) / 2 * c
quadrado = b * b
retangulo = a * b

#saida

print('TRIANGULO: {:.3f}'.format(triangulo))
print('CIRCULO: {:.3f}'.format(circulo))
print('TRAPEZIO: {:.3f}'.format(trapezio))
print('QUADRADO: {:.3f}'.format(quadrado))
print('RETANGULO: {:.3f}'.format(retangulo))
