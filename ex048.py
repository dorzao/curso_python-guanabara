#script que soma todos os múltiplos de entre 1 e 500
r = 0
for c in range(1, 500):
    if c % 3 == 0 and c % 2 != 0:
        r += c

print('A soma entre todos os múltiplos de 3 impares entre 1 e 500 é: {}'.format(r))
