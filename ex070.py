#script que lê nome e preço de produtos, e mostra estatísticas no final
tam = 50
print('=' * tam)
print(f"{'LOJA DO PEDRÃO' :^50}")
print('=' * tam)
soma = me = cont = contm = 0
mp = op = ''
while True:
    prod = input('Digite o nome do produto: ')
    prec = float(input('Digite o preço dele: R$ '))
    if cont < 1:
        me = prec
        mp = prod
    else:
        if prec < me:
            mp = prod
            me = prec
    soma += prec
    if prec > 1000:
        contm += 1
    op = input('Quer adicinar mais produtos [S/N]? ').strip().lower()[0]
    while op != 's' and op != 'n':
        print('Opção inválida!')
        op = input('Quer adicinar mais produtos [S/N]? ').strip().lower()[0]
    cont += 1
    if op == 'n':
        break

print('=' * tam)
print(f"{'Finalizando o Programa...' :^50}")
print('=' * tam)
print(f'Total de produtos: {cont}')
print(f'Total da compra: R$ {soma:.2f}')
print(f'Media total da compra: {(soma / cont) :.2f}')
print(f'Total de produtos de mais de R$ 1000.00: {contm}')
print(f'Nome do produto mais barato: {mp} que custou R$ {me:.2f}')
