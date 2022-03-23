#script que recebe 5 valores, mostra o maior, o menor, e suas posições na lista
lista = []
for c in range (0, 5):
    lista.append(int(input('Digite um número: ')))

print(end=f'O maior valor digitado foi o {max(lista)} na(s) posição(ções): ')
for cont, num in enumerate(lista):
    if max(lista) == lista[cont]:
        print(cont, end=' ')
print('')
print(end=f'O menor valor digitado foi o {min(lista)} na(s) posição(ções): ')
for contador, numero in enumerate(lista):
    if min(lista) == lista[contador]:
        print(contador, end=' ')
print('')
