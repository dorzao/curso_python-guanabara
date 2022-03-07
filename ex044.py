#script que fornece formas de pagamentoo e divérsos descontos
p = float(input('Digite o preço do produto: R$ '))
e = input("""
Escolha a forma de pagamento: 

[1] À vista no dinheiro
[2] No débito
[3] Em 2x no crédito
[4] Em 3x ou mais no crédito

Digite somente uma das opções listadas acima:  \n
""")
print('\n')
if e == '1':
    print('Seu desconto é de 10%, pagará: R$ {:.2f}, seu dsconto foi de R$ {:.2f}. '.format(p * 0.9, p * 0.1))
elif e == '2':
    print('Desconto de 5%, tu pagarás R$ {:.2f}, su desconto foi de R$ {:.2f}.'.format(p * 0.95, p * 0.05))
elif e == '3':
    print('Tu não terás desconto. Pagarás duas parcelas de R$ {:.2f}. '.format(p / 2))
else:
    par = int(input('Em quantas parcelas? '))
    print('Tu terás um júros de 20%, pagarás ao todo R$ {:.2f}, dividido em {} parcelas de R$ {:.2f}'.format(p * 1.2, par, (p * 1.2) / par ))

if e != '1' or e != '2' or e != '3' or e != '4':
    print('\nEncerrando programa...')
