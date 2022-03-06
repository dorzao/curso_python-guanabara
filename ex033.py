#script que lê 3 números e imprime o maior e o menor
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
ma = n1
if n2 > ma or n3 > ma:
    ma = n2
if n3 > ma:
    ma = n3
print('O maior número é: ', ma)
me = n1
if n2 < me or n3 < me:
    me = n2
if n3 < me:
    me = n3
print(me, ' é o menor número')
