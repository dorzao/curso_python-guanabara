#script que recebe um número e mostra seu nome por extenso utilizando tupla
n = int(input('Digite um número entre 0 e 20: '))
while n < 0 or n > 20:
    print('opção inválida! ')
    n = int(input('Digite um número entre 0 e 20: '))
e = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'desesseis', 'desessete', 'desoito', 'desenove', 'vinte')
print(f'Você digitou o número {e[n]}.')