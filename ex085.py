#script recebe 7 números, classificandoos compo pares ou impares
lista = [[], []]
n = 0
for c in range (1, 8):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print('=' * 40)
print(f'A ordem crescente dos pares é: {sorted(lista[0])}')
print(f'A ordem crescente dos impares é: {sorted(lista[1])}')
