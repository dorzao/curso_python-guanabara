#script que cria uma tabuada com o for
n = int(input('Digite o número que quer saber a tabuada: '))
print('='*12)
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n *c))

print('='*12)
