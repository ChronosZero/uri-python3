dias = int(input())

anos = dias // 365
meses = (dias - anos * 365) // 30
dias = dias - (meses * 30 + anos * 365)

print('{} ano(s)\n{} mes(es)\n{} dia(s)'.format(anos, meses, dias))
