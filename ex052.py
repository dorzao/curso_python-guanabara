#script que recebe um número e diz se é primo
n = int(input('Digite um número para saber se é primo: '))
i = 0
for c in range (n, 0, -1):
    if n % c == 0:
        i = i + 1

if i == 2:
    print(n, ' é primo!')
else:
    print(n, ' não é primo!')

