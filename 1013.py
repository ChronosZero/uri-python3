#entrada dos dados
valores = input().split()

#conversao dos valores para int

for i in range(len(valores)):
    valores[i]=int(valores[i])

#identificação das variaveis

a = valores[0]
b = valores[1]
c = valores[2]

maiorAB = (a+b+abs(a-b))/2
maiorABC = (maiorAB + c +abs(maiorAB - c)) / 2

print('{:.0f} eh o maior'.format(maiorABC))
