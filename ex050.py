#script que recebe 6 números e soma os pares e mostra o resultado
r = 0
for c in range(0,6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        r = r + n

print('='*27)
print('O resultado da soma dos pares digitados é: {}'.format(r))
