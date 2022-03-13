#script gerador de pa com while
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
print(p, end=' -> ')
i = 1
while i <= 10:
    if i == 10:
        print('{} -> FIM!'.format(p + (r * i)))
    elif i < 10:
        print(p + (r * i), end=' ->')
    i += 1
