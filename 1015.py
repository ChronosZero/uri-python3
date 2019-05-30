from math import sqrt


#entrada de dados

valores = input().split()
valores2 = input().split()

#conversão de valores de x1 e y1 para float

for i in range(len(valores)):
    valores[i]=float(valores[i])

x1 = valores[0]
y1 = valores[1]

#conversão de valores de x2 e y2 para float

for i in range(len(valores2)):
    valores2[i]=float(valores2[i])

x2 = valores2[0]
y2 = valores2[1]

#calcular a distancia

distancia = sqrt((x2 - x1)**2 + (y2 - y1)**2)

print('{:.4f}'.format(distancia))
