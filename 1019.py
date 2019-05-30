segundos = int(input())

horas = segundos // 3600
minutos = (segundos - horas * 3600) // 60
segundosF = segundos - (minutos * 60 + horas * 3600)

print('{}:{}:{}'.format(horas, minutos, segundosF))
