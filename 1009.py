nome = input()
salario_fixo = float(input())
vendas_no_mes = float(input())

total_receber = salario_fixo + (vendas_no_mes * 0.15)

print('TOTAL = R$ {:.2f}'.format(total_receber))
