#script cria método que recebe n parâmetros, e indica o maior
from time import sleep
def maiorador(*n):
    lista = list()
    lista.append(n)
    print('=' * 40)
    sleep(1)
    print(end=f'Na lista: ')
    for i in n:
        print(i, end='  ')
        sleep(1)
    if len(n) > 1:
        print('FIM')
        sleep(1)
        print(f'Foram cadastrados {len(n)} números')
        maior = max(n)
        sleep(1)
        print(f'o maior número é {maior}')
    elif len(n) == 1:
        print('FIM')
        sleep(1)
        print(f'Foi cadastrado apenas {len(n)} número')
        maior = max(n)
        sleep(1)
        print(f'como só foi cadastrado 1 número, o maior número foi o próprio {maior}')
    else:
        sleep(1)
        print('[Vazio]')
        sleep(1)
        print('não foram cadastrados números.')
    lista.clear()
    sleep(2)


#programa principal
maiorador(1, 3, 7, 9)
maiorador(13, -3, 75, 1245)
maiorador()
maiorador(1, 2)
maiorador(6)
print('=' * 40)
