valor = int(input())

cedulas = [100, 50, 20, 10, 5, 2, 1]
qtd = []

print(valor)

for i in range(0, 7):
    qtd.append(valor // cedulas[i])
    valor -= qtd[i] * cedulas[i]
    print('{} nota(s) de R$ {},00'.format(qtd[i], cedulas[i]))
