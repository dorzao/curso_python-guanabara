#script que lê nome e peso de várias pessoas, conta quantas tem, mostra o maior e o menor peso e os pertencedores de cada um
lista = []
dados = []
ma = me = 0
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite o peso em kg: ')))
    if len(lista) == 0:
        me = dados[1]
        ma = dados[1]
    else:
        if dados[1] < me:
            me = dados[1]
        if dados[1] > ma:
            ma = dados[1]
    lista.append(dados[:])
    dados.clear()
    op = input('Deseja adicionar mais pessoas[S/N]?').strip().lower()[0]
    while 's' not in op and 'n' not in op:
        print('Responda com somente S de sim ou com N de não Filhão... ')
        op = input('Deseja adicionar mais pessoas[S/N]?').strip().lower()[0]
    if op == 'n':
        break
print('≃' * 50)
print(f'Ao todo foi/foram cadastrada(s) {len(lista)} pessoa(s) ')
print(end=f'Das mais leves, ou seja, de {me} kg, temos: ')
for c in lista:
    if c[1] == me:
        print(c[0], end='  ')
print()
print(end=f'Das mais pesadas, ou seja, de {ma} kg, temos: ')
for c in lista:
    if c[1] == ma:
        print(c[0], end='  ')
print()
