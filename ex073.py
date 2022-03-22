#Script que declara uma tupla com a tabela do brasileirão e mostra estatísticas
t = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Coríntians', 'Bragantino', 'Fluminense', 'América', 'Atlético-Go', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Atlético-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
print('{:=^139}'.format('Mostrando Estatísticas'))
print(f'Os 5 primeiros colocados foram: ', end='')
for c in range (0, 5):
    if c == 4:
        print(f'{t[c]}. ')
    else:
        print(t[c], end=', ')


print(end='Os 4 últimos foram: ')
for c in range (-4, 0):
    if c == -1:
        print(f'{t[c]}. ')
    else:
        print(end=f'{t[c]}, ')
alf = sorted(t)
print(f'A tabela em ordem alfabética é: ', end='')
for c in range(0, 20):
    if c == 19:
        print(f'{alf[c]}. ')
    else:
        print(end=f'{alf[c]}, ')
chape = t.index('Chapecoense')
print(f'A Chapecoense ficou na {chape + 1}ª posição!')
print('{:=^139}'.format('Fim do Programa !!!'))
