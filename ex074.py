#script que sorteia 5 números aleatórios, adiciona em uma tupla e mostra qual foi o maior e o menor
from random import randint
num = randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20)
print(end='Os números sorteados foram: ')
for c in num:
    print(c, end=' ')

print(f'\n O maior sorteado foi o {max(num)}')
print(f'O menor número sorteado foi o {min(num)}')
