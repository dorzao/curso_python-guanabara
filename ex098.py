#script triplo contador: 1 a 10 crescente, 10 a 0 decrescente de 2 em 2, e personalizado por meio de função
from time import sleep
def contador(i, f, p):
    print('=' * 35)
    f += p
    for c in range (i, f, p):
        print(c, end='  ')
        sleep(1)
    print('Pronto!')
    print('=' * 35)
    print()


#programa principal
contador(1, 10, 1)
contador(10, 1, -2)
contador(
    int(input('Digite o passo inicial: ')),
    int(input('Digite o passo final: ')),
    int(input('Digite o passo: '))
    
)
