valor = float(input())

cedulas = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
qtd = []

#calculo das cedulas e moedas
for i in range(0, 12):
    if(i == 11):
        qtd.append(valor / cedulas[i])

    else:
        qtd.append(valor // cedulas[i])
        valor -= qtd[i] * cedulas[i]
        valor = round(valor, 3)


#Impressao das notas
print('NOTAS:')
for i in range(0, 6):
    print('{:.0f} nota(s) de R$ {}.00'.format(qtd[i], cedulas[i]))

#Impressao das moedas

print('MOEDAS:')
for i in range(6, 12):
    #Impressao da moeda de 1 real
    if(i == 6):
        print('{:.0f} moeda(s) de R$ {}.00'.format(qtd[i], cedulas[i]))

    elif(i == 7):
        print('{:.0f} moeda(s) de R$ {}0'.format(qtd[i], cedulas[i]))

    elif(i == 9):
        print('{:.0f} moeda(s) de R$ {}0'.format(qtd[i], cedulas[i]))

    #Demais moedas
    else:
        print('{:.0f} moeda(s) de R$ {}'.format(qtd[i], cedulas[i]))
