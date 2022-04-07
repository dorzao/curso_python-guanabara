#script que cadastra n jogadores, mostra uma lista, mostra o levantamento individual de cada jogador solicitado
jogador = {}
time = []
totgols = 0
gols = list()
while True:
    print('=' * 35)
    print(f"{'Novo Cadastro':^35}")
    print('=' * 35)
    jogador['nome'] = input('Nome do jogador:  ')
    jogador['partidas'] = int(input('Número de partidas: '))
    if jogador['partidas'] > 0:
        for c in range(0, jogador['partidas']):
            gols.append(int(input(f'Quantos gols marcou na {c + 1}ª partida? '))) 
    jogador['gols'] = gols[:]
    gols.clear()
    time.append(jogador.copy())
    jogador.clear()
    op = input('Quer cadastrar mais jogadores[S/N]? ').strip().upper()[0]
    while op not in 'SN':
        print('=' * 35)
        print('ERRO: Digite somente S ou N... ')
        op = input('Quer cadastrar mais jogadores[S/N]? ').strip().upper()[0]
    if op == 'N':
        break
print('=' * 35)
print(end=f"{'id':^6}")
print(end=f"{'Nome':<20}")
print(f"{'Gols':<9}")
print('-' * 35)
for c in range (0, len(time)):
    print(end=f"{c:^6}")
    print(end=f"{time[c]['nome']:<20}")
    print(f"{time[c]['gols']}")
while True:
    print('=' * 35)
    op = int(input('Qual jogador deseja consultar Individualmente [999 sái do programa]? '))
    if op == 999:
        print('=' * 35)
        print(f"{'Fegando o programa':^35}")
        print('=' * 35)
        break
    elif op > ( len(time) - 1 ) or op < 0:
        print('=' * 35)
        print('Id de jogador inixistente! ')
    else:
        print('=' * 35)
        print(f'Levantamento geral de: {time[op]["nome"]}')
        print('=' * 35)
        for k, v in enumerate(time[op]['gols']):
            print(f'- Na {k + 1}ª partida fez {v} gols ')
            totgols += v
        partidas = time[op]['partidas']
        print()
        print(f'- Total de partidas: {partidas}')
        print(f'- Total de gols: {totgols}')
        media = totgols / len(time[op]['gols'])
        totgols = 0
        print(f'- Média de gols por partida: {media:5.1f}')
