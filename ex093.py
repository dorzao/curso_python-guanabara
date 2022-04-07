#script que cria um dicionário e mostre o aproveitamento de gols de um jogador
jogador = dict()
gols = []
jogador['nome'] = input('Qual é o nome do jogador? ')
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = []
total = 0
for c in range (0, jogador['partidas']):
    gols.append(int(input(f'Quntos cols marcados na {c + 1}ª partida? ')))
    total += gols[c]
jogador['gols'] = gols[:]
jogador['total'] = total
del gols, total
print()
print('=' * 35)
print(f"{'Maneira 1':^35}")
print('=' * 35)
print()
print(jogador)
print()
print('=' * 35)
print(f"{'Maneira 2':^35}")
print('=' * 35)
print()
for c, v in jogador.items():
    print(f'No campo {c} o valor é: {v}')
print()
print('=' * 35)
print(f"{'Última maneira':^35}")
print('=' * 35)
print()
print(f'O jogador {jogador["nome"]} fez {jogador["partidas"]} partidas e ao todo marcou {jogador["total"]} gols. Seu rendimento jogo a jogo de gols foi: ')
for p, g in enumerate(jogador['gols']):
    print(f'-> Na {p + 1}ª partida {jogador["nome"]} marcou {g} gols.')
