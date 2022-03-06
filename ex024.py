#script que recebe o nome de uma cidade e verifica se começa com santo
c = input('Digite o nome de uma cidade: ')
v = 'santo' in c.split()[0].lower()
if v == True :
    v = 'sim'
else:
    v = 'não'

print('{} começa com a palavra santo? {}.'.format(c, v))
