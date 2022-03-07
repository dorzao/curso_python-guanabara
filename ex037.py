#script de base de conversão para binário, octal ou hexadecimal

#Atribuindo o valor à variável
n = int(input('Digite o número que deseja converter: '))

#Obtendo a opção de seleção do menu
i = input('Selecione sua opção: \n [b] binário\n [o] octal\n [h] hexadecimal\n [qualquer outra coisa ] Desistir e fechar o programa\n Converter para: ')
if i == 'b':
    print('{} em binário é: {}. '.format(n, bin(n)[2:]))
elif i == 'o':
    print('{} em octal é: {}. '.format(n, oct(n)[2:]))
elif i == 'h':
    print('{} em hexadecimal é: {}. '.format(n, hex(n)[2:]))
else:
    print('Ok, fechando o programa...')
