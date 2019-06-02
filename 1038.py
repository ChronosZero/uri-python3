#entrada dos dados
valores = input().split()

#conversao dos valores para int

for i in range(len(valores)):
    valores[i]=float(valores[i])

#identificação das variaveis

a = valores[0]
b = valores[1]
precoFinal = 0

tabela = [
    {'codigo': 1, 'nome': 'cachorro quente', 'preco': 4.00},
    {'codigo': 2, 'nome': 'x-salada', 'preco': 4.50},
    {'codigo': 3, 'nome': 'x-bacon', 'preco': 5.00},
    {'codigo': 4, 'nome': 'torrada simples', 'preco': 2.00},
    {'codigo': 5, 'nome': 'refrigerante', 'preco': 1.50},
    ]

for i in range(0,5):
    if(a == tabela[i]['codigo']):
        precoFinal += tabela[i]['preco'] * b

print('Total: R$ {:.2f}'.format(precoFinal))
