#script que recebe nome de 4 alunos e sorteia a ordem de apresentação

from random import shuffle
a1 = input('Qual o primeiro aluno? ')
a2 = input('Qual o segundo aluno? ')
a3 = input('Qual o terceiro aluno? ')
a4 = input('Qual o último aluno? ')
l = [a1, a2, a3, a4]
shuffle(l)
print('A ordem de apresentação é: {}, depois {}, logo após {}, e por último {}.'.format(l[0], l[1], l[2], l[3]))
