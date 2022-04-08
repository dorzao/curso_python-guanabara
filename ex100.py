#script que crie uma lista com função de sortear e de somar pares
from random import randint
from time import sleep
numeros = list()
def sortear(*n):
    print(end=f'Sorteando os 5 números: ')
    for c in range (0, 5):
        if c == 0:
            numeros.append(randint(1, 20))
            print(numeros[c], end='  ')
            sleep(1)
        else: 
            num = randint(1, 20)
            while num in numeros:
                num = randint(1, 20)
            numeros.append(num)
            print(numeros[c], end='  ')
            sleep(1)
    print('Fim')
    sleep(1)

def sopares():
    pares = 0
    print(end='Somando os pares: ')
    for c in numeros:
        if c % 2 == 0:
            print(c, end=' + ')
            pares += c
            sleep(1)
    print(f' nada = {pares}')


#programa principal
sortear()
sopares()
