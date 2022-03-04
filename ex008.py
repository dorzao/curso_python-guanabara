#script que recebe uma quantidade em metros, e converte para km, cm, mm, em dm
n = int(input('Digite a quantidade de metros: '))
print('Equivale a: \n {} milímetros \n {} centímetros \n {} decímetros \n {} decâmetros \n {} hectômetros \n {} quilômetros'.format(n * 1000, n * 100, n * 10, n / 10, n / 100, n / 1000))
