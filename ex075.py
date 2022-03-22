#script que recebe 4 números e mostra algumas estatísticas
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))
tup = (n1, n2, n3, n4)
print(f'Você digitou os valores: {tup}')
if tup.count(9) >= 1:
    print(f'O valor 9 foi digitado {tup.count(9)} vezes')
else:
    print('O valor 9 não foi digitado')

if tup.count(3) > 0:
    print(f'O valor 3 apareceu na {tup.index(3) + 1}ª posição')
else:
    print('O número 3 não foi digitado')
print(end='Os valores pares foram: ')
par = 0
for c in range (0, 4):
    if tup[c] % 2 == 0:
        print(tup[c], end=' ')
        par += 1
if par == 0:
    print('nenhum')
print('\n')
