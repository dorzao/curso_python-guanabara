#script que lê 5 números, coloca na ordem sem usar o sorted
lista = []
n = 0
lista.append(int(input('Digite um número: ')))
print('Adicionei no início da fila...')
for c in range(0, 4):
    n = int(input('Digite um número: '))
    if n < lista[0] :
        lista.insert(0, n)
        print(f'Adicionei {n} no inicio da fila!')
    elif n > lista[-1]:
        lista.append(n)
        print(f'Adicionei {n} no final da fila!')
    elif lista[0] < n < lista[1]:
        lista.insert(1, n)
        print(f'{n} agora é o segundo da fila')
    elif lista[1] < n < lista[2]:
        lista.insert(2, n)
        print(f'{n} agora é o terceiro da fila!')
    elif lista[2] < n < lista[3]:
        lista.insert(3, n)
        print(f'{n} agora é o penúltimo da fila')
print(f'A ordem certa crescente da lista é: {lista}')