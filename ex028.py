#script que chuta um número, e pede para pessoa adivinhar! Se ela acertar, imprimir, se não, também imprimir que errou
from random import randint
n = randint(1, 5)
p = int(input('Tente advinhar em que número pensei entre 1 e 5: '))
if p == n:
    print('Parabéns! Eu havia pensado no {} mesmo.'.format(n))
else:
    print('Que pena, você errou! Eu havia pensado no número {}.'.format(n))
