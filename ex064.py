#script que recebe n números, recebe o valor 99 para parar, e mostra o resultado da soma exceto o 999
i = 0
n1 = 0
n2 = 0
a = 1000
while n1 != a:
    n1 = int(input('Digite um número: '))
    if n1 != 999:
        n2 = n2 + n1
    elif n1 == 999:
        print('Tu somaste {} números e a soma total deles é {}. '.format(i, n2))
        a -= 1
    i += 1
    