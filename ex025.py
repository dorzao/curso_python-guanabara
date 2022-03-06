#script que verifica se a pessoa tem silva no nome
n = input('Digite teu nome completo: ')
r = n.lower().find('silva')
if r == -1:
    r = 'Não'
else:
    r = 'Sim'
print('{} tem Silva no nome? {}'.format(n, r))
