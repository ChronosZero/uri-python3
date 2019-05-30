peca1 = input().split()
peca2 = input().split()

for i in range(len(peca1)):
    peca1[i]=float(peca1[i])

valor_peca1 = peca1[1] * peca1[2]

for i in range(len(peca2)):
    peca2[i]=float(peca2[i])

valor_peca2 = peca2[1] * peca2[2]

total_pagar = valor_peca1 + valor_peca2

print('VALOR A PAGAR: R$ {:.2f}'.format(total_pagar))
