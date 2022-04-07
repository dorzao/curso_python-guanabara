#script que faz 4 jogadores de dados jogarem um dado, e depois mostre quem ganhou pnum ranking (Prigrama passivo)
from random import randint
from time import sleep
from operator import itemgetter
print()
print('=' * 35)
print(f"{'Iniciando partida':^35}")
print('=' * 35)
print()
jogadores = {
    'jogador 1': randint(1, 6),
    'jogador 2': randint(1 ,6),
    'jogador 3': randint(1, 6),
    'jogador 4': randint(1, 6)}
for k, v in jogadores.items():
    print(f'O {k} tirou {v} nos dados!')
    sleep(1)
ordem = list()
ordem = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
sleep(2)
print()
print('=' * 35)
print(f"{'Ranking final':^35}")
print('=' * 35)
print()
for n, p in enumerate(ordem):
    print(f'{n + 1}º Lugar: {p[0]} com {p[1]} pontos')
    sleep(1)
print()
print('=' * 35)
print(f"{'Finalizando programa':^35}")
print('=' * 35)
print()
