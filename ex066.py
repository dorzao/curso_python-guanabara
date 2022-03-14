#script que receba vários números, mostre a soma deles, quantos foram e quando digitado 999 ele para com o break
i = s = 0
while True:
    n = int(input('Digite um número[999 para parar]: '))
    if n == 999:
        break
    s += n
    i += 1
        
print(f'Tu digitaste {i} números e a soma total foi {s}.')
