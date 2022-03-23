#script que coleta vários números, cria uma lista, depois crie 2 listas  uma com pares outra com impares
from time import sleep
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    op = input('Deseja continuar adicionando números[S/N]? ').strip().lower()[0]
    while op != 's' and op != 'n':
        print('Opção inválida. ')
        op = input('Deseja continuar adicionando números[S/N]? ').strip().lower()[0]
    if op == 'n':
        break
print(f'Sua lista é: {lista}')
print('Gerando lista de pares')
sleep(3)
print(end='Lista de pares é: ')
for c in lista:
    if c % 2 == 0:
        print(c, end=' -> ')
print('ACABOU')
sleep(2)
print('Gerando lista de impares...')
sleep(3)
print(end='Sua lista de impares é: ')
for c in lista:
    if c % 2 != 0:
        print(c, end=' -> ')
print('Acabou')
print('Finalizando programa...')
sleep(2)
