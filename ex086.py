#script que gera uma matriz 3x3 com listas compostas
valor = 0
matriz = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
for l in range(0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f'Digite o {(l +1) * (c + 1)} valor da matriz 3 x 3: '))
print('='*40)
for l in range (0, 3):
    for c in range(0, 3):
        print(end=f'[{matriz[l][c]:^5}] ')
    print()
