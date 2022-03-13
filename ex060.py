#script que calcula fatorial
n = int(input('Digite um número para saber seu fatorial: '))
n2 = n -1
print('O fatorial de {} é: {}'.format(n, n), end=' x ')
while n2 >=1:
    if n2 == 1:
        n = n * n2
        print(n2, ' = ', n, end='. \n')
        n2 = n2 -2
    elif n2 > 1:
        n = n * n2
        print('{} x '.format(n2), end='')
        n2 = n2 - 1
