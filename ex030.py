#script que recebe um número inteiro e escreve se ele é par ou impar
n = int(input("Digite um número inteiro para saber se é par ou impar: "))
if n % 2 == 0:
    print('{} é um número par!'.format(n))
else:
    print('{} é um número impar!')
