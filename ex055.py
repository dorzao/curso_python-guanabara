#script que lê 5 pesos, e mostra no final o maior e o menor
p = float(input('Digite o primeiro peso em kg: '))
ma = p
me = p
for c in range (0, 4):
    p = float(input('Digite o próximo peso em Kg: '))
    if p > ma:
        ma = p
    if p < me:
        me = p

print('O maior peso digitado foi de {:.1f} kg e o menor foi de {:.1f} kg.'.format(ma, me))

