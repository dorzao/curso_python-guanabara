#script que imprime tabuadas infinitamente até que seja digitado um número negativo
while True:
    n = int(input('Tabuada de quanto? '))
    if n < 0:
        break
    print('=' * 25)
    for c in range (1, 11):
        print(f'{n} x {c} = {n * c}')
    print('=' * 25)
print('Finalizando programa de tabuada... \n Volte Sempre!')
