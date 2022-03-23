#script que receber vários números, adiciona a uma lista, mostra quantos números digitados ao todo, a lista na ordem decrescente, e quantas vezes o 5 foi digitado
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    op = input('Deseja continuar a digitar números[S/N]? ').lower().strip()[0]
    while op != 's' and op != 'n':
        print('Opção inválida!')
        op = input('Deseja continuar a digitar números[S/N]? ').lower().strip()[0]
    if op == 'n':
        break
print(f'Sua lista tem {len(lista)} números')
listarev = sorted(lista, reverse=True)
print(f'Sua lista em ordem decrescente é: {listarev}')
if lista.count(5) > 0:
    print(f'O número 5 apareceu {lista.count(5)} vezes')
else:
    print('O número 5 não foi digitado')