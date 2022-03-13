#script que recebe um número e mostra os termos de fibonacci até aquele número
n = int(input('Quer saber até qual termo? '))
print('=' * 139)
i = 0
a = 0
b = 1
c = 0
print(a, end=' -> ')
while i <= n:
    a = b
    b = c
    c = a + b
    if i < n:
        print(c, end=' -> ')
    elif i == n:
        print(c, end=' -> TERMINOU! \n')
        print('=' * 139)
    i = i + 1


