#script que faz o computador jogar pedra papel ou tesoura com você!
from random import randint
pc = randint(1, 3)
vc = int(input("""
Vamos jogar pedra papel ou tesoura?

Selecione sua opção:

[1] Pedra
[2] Papel
[3] Tesoura
[qualquer outra coisa] Não quero jogar

"""))

if vc == 1 or vc == 2 or vc == 3:
    if pc == 1:
        print('Computador Escolheu Pedra')
    elif pc == 2:
        print('Computador jogou Papel')
    else:
        print('Computador jogou Tesoura')

    print('Você jogou ', end='')
    if vc == 1:
        print('Pedra')
    elif vc == 2:
        print('Papel')
    elif vc == 3:
        print('Tesoura')

    if pc == vc:
        print('Empatamos!')
    elif (pc == 3 and vc == 2) or (pc == 2 and vc == 1) or (pc == 1 and vc == 3):
        print('Eu venci!')
    else:
        print('Parabéns, tu venceste!')


print('Até mais...')
