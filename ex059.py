#script lê 2 números, e dá opções do que fazer como somar, multiplicar, etc...
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
o = int(input("""
{}
Menú principal
{}
[1] Somar os dois números
[2] Multiplicar os dois números
[3] Mostra quem é o maior
[4] Escolher outros números
[0] Sair do programa
{}
Selecione sua opção: """.format('='*50, '='*50, '='*50)))
print('='*50)
if o == 1:
    print('A soma entre {} e {} é {}.'.format(n1, n2, n1 + n2))
    print('='*50)
elif o == 2:
    print('A multiplicação entre {} e {} é {}. '.format(n1, n2, n1 * n2))
    print('='*50)
elif o == 3:
    if n1 > n2:
        print(n1, ' é maior que ', n2)
        print('='*50)
    elif n2 > n1:
        print(n2, ' é maior que ', n1)
        print('='*50)
    else:
        print(n1, ' e ', n2, ' são iguais!')
        print('='*50)
elif o == 4:
    n1 = int(input('Digite o novo valor do primeiro número: '))
    n2 = int(input('Digite o novo valor do segundo número: '))
    print('='*50)
else:
    print('Opção inválida. Aperte uma das teclas indicadas pelo menu! ')
    print('='*50)

while o != 0:
    o = int(input("""
{}
Menu Principal
{}
[1] Somar os dois números
[2] Multiplicar os dois números
[3] Mostra quem é o maior
[4] Escolher outros números
[0] Sair do programa
{}
Selecione sua opção: """.format('=' * 50, '=' * 50, '=' * 50)))
    print('=' * 50)
    if o == 1:
        print('A soma entre {} e {} é {}.'.format(n1, n2, n1 + n2))
        print('=' * 50)
    elif o == 2:
        print('A multiplicação entre {} e {} é {}. '.format(n1, n2, n1 * n2))
        print('='*50)
    elif o == 3:
        if n1 > n2:
            print(n1, ' é maior que ', n2)
            print('='*50)
        elif n2 > n1:
            print(n2, ' é maior que ', n1)
            print('='*50)
        else:
            print(n1, ' e ', n2, ' são iguais!')
            print('='*50)
    elif o == 4:
        n1 = int(input('Digite o novo valor do primeiro número: '))
        n2 = int(input('Digite o novo valor do segundo número: '))
        print('='*50)
    else:
        print('Opção inválida. Aperte uma das teclas indicadas pelo menu! ')
        print('='*50)
print('Ok, finalizando o programa!')
print('='*50)