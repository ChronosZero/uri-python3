#entrada dos dados
valores = input().split()

#conversao dos valores para int

for i in range(len(valores)):
    valores[i]=int(valores[i])

#identificação das variaveis

a = valores[0]
b = valores[1]
c = valores[2]
d = valores[3]

somaCD = c + d
somaAB = a + b

condicoes = [
    b > c,
    d > a,
    somaCD > somaAB,
    c >= 0,
    d >= 0,
    a %2 ==0
    ]

if all(condicoes):
    print('Valores aceitos')

else:
    print('Valores nao aceitos')
