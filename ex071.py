#script de caixa eletrônico
n = int(input('Quanto tu queres sacar? R$ '))
n2 = n 
cinc = vin = dez = um = 0
while n2 >= 50:
    n2 -= 50
    cinc += 1
while n2 >= 20:
    n2 -= 20
    vin += 1
while n2 >= 10:
    n2 -= 10
    dez += 1
um = n2
print('Ao todo voce sacou: ')
if cinc >= 1:
    print(f'{cinc} notas de R$ 50.00')
if vin >= 1:
    print(f'{vin} notas de R$ 20.00')
if dez >= 1:
    print(f'{dez} notas de R$ 10.00')
if um >= 1:
    print(f'{um} notas de R$ 1.00')

print('Fechando caixa eletrônico...')
