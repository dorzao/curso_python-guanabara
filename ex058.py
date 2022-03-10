#script jogo do 10, computador pensa num número entre 1 e 10, e anote quantos chutes errados você fez
from random import randint
pc = randint(0, 10)
i = 0
n = int(input('Chute um número entre 0 e 10: '))
while n != pc:
    if pc > n:
        mm = 'MENOR'
    elif pc < n:
        mm = 'MAIOR'
    n = int(input('O valor que vc chutou é {} que o que pensei! Chute outro número: '.format(mm)))
    i += 1
    
if i == 0:
    print('Parabéns, você acertou de primeira. Eu tinha pensado no {} mesmo!'.format(n))
else:
    print('Você acertou na {}ª tentativa. '.format(i + 1))
   