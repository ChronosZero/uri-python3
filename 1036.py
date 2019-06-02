from math import sqrt
#entrada dos dados
valores = input().split()

#conversao dos valores para int

for i in range(len(valores)):
    valores[i]=float(valores[i])

#identificação das variaveis

a = valores[0]
b = valores[1]
c = valores[2]

delta = (b**2) - (4 * a * c)
if (delta > 0 and a != 0):
    x1 = ((-1 * b) + sqrt(delta)) / (2 * a)
    x2 = ((-1 * b) - sqrt(delta)) / (2 * a)
    print('R1 = {:.5f}'.format(x1))
    print('R2 = {:.5f}'.format(x2))
else :
    print('Impossivel calcular')
