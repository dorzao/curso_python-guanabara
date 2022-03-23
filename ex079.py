#script que recebe números, adiciona a uma lista caso não haja o mesmo nela, e no final imprime a lista
lista = []
lista.append(int(input('Digite um número: ')))
op = input(' Quer adicionar mais números [S/N]? ').strip().lower()[0]
while op != 's' and op != 'n':
    print('Opção inválida! ')
    op = input(' Quer adicionar mais números [S/N]? ').strip().lower()[0]
if op == 's':
    while True:
        n1 = int(input('Digite um número: '))
        while n1 in lista:
            print('Valor já existente! Tente outro...')
            n1 = int(input('Digite um número: '))
        lista.append(n1)
        op = input(' Quer adicionar mais números [S/N]? ').strip().lower()[0]
        while op != 's' and op != 'n':
            print('Opção inválida! ')
            op = input(' Quer adicionar mais números [S/N]? ').strip().lower()[0]
        
        if op == 'n':
            break
print(f'Sua lista é {sorted(lista)}')
