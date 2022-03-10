#script com contagem regressiva de 10 a 1, dizendo feliz ano novo no final
from time import sleep
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('Feliz ano novo!')