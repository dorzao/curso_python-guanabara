#script que faz o pc jogar par ou impar, anota as vitórias do player e só para quando o player perde
from random import randint

i = 0
while True:
    pl = int(input('Digite um valor: '))
    print('=' * 35)
    pc = randint(1, 10)
    e = input('Quer Par ou Impar [P/I]? ').strip().lower()[0]
    print('=' * 35)
    while e != 'p' and e != 'i':
        print('opção inválida...')
        e = input('Quer Par ou Impar [P/I]? ').strip().lower()[0]
        print('=' * 35)
    if e == 'i':
        ep = 'par'
        es = 'impar'
    else:
        ep = 'impar'
        es = 'par'
    print(f'Você jogou {pl} e pediu {es}.')
    print('=' * 35)
    print(f'Computador jogou {pc} e pediu {ep}')
    print('=' * 35)
    print(f'{pl} + {pc} = {pl + pc} que é um número ', end='')
    if ( (pc + pl) % 2 == 0 and e == 'p' ) or ( (pc + pl) % 2 == 1 and e == 'i' ):
        print(es)
        print('Você venceu! Bora jogar de novo... ')
        print('=' * 35)
        i += 1
    else:
        print(ep)
        print('Tu perdeste! ')
        break

if i > 0:
    print(f'Você venceu {i} vezes!')
else:
    print('Infelizmente você não venceu nenhuma rodada!')
print('Jogo finalizado! ')
