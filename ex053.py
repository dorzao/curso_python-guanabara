#script que recebe uma frase, e verifica se é um palíndromo
f = input('Digite uma frase para verificar se é um palíndromo: ')
f2 = f.lower().replace(' ', '')
i = 0
i2 = len(f2) - 1
for c in range (0, i2):
    if f2[c] == f2[i2]:
        i = i + 1
    i2 = i2 - 1

if i == (len(f2) -1):
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
