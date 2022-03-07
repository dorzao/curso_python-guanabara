#script que recebe 2 valores, e imprime quem é o maior, quem é o menor ou se são iguais
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
if n1 > n2:
    print('{} é maior que {}! Ou seja, o primeiro é maior'.format(n1, n2))
elif n2 > n1:
    print('{} é maior que {}. OU seja, o segundo é maior.'.format(n2, n1))
else:
    print('Os dois são iguais. Ou seja, {} é igual a {}.'.format(n1, n2))
