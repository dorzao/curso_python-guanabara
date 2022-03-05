#script que receb um número real e mostra somente a parteinteira
from math import trunc
n = float(input('Digite um número decimal (com ponto) ex: 3.2: '))
print('A parte inteira do número {} é {}'.format(n, trunc(n)))
