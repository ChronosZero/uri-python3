tempo_viagem = int(input())
velocidade_media = float(input())

litros_necessarios = velocidade_media / 12 * tempo_viagem

print('{:.3f}'.format(litros_necessarios))
