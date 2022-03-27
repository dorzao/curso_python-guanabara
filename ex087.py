#script que recebe e mostra uma matriz 3 x 3 e algumas estatísticas
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = n = coluna3 = malinha2 = 0
for l in range (0, 3):
    for c in range (0, 3):
        n = int(input(f'Digite um valor para [{l}, {c}]: '))
        matriz[l][c] = n
        if n % 2 == 0:
            pares += n
        coluna3 += matriz[l][2]
        if l == 1:
            if c == 0:
                malinha2 = matriz[l][c]
            if matriz[l][c] > malinha2:
                malinha2 = matriz[l][c]

print('=' * 21)

for l in range (0, 3):
    for c in range (0,3):
        print(end=f'[{matriz[l][c]:^5}]')
    print()
print('=' * 21)
print(f'A soma dos pares é: {pares}')
print(f'A soma da coluna 3 é: {coluna3}')
print(f'O maior da linha 2 é: {malinha2}')
