#script que imprime uma razão de 10 termos onde o usuário digita o termo inicial e a razão
i = int(input('Digite o termo inicial: '))
r = int(input('Digite a razão: '))
d = i + (10 - 1) * r + r
for c in range (i, d, r):
    if c == d - r:
        print(c, end='. ')
    else:
        print(c, end=', ')
            
print(' ')