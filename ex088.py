#script que sorteia x jogos de mega sena para o usuário
from random import randint
cont = nj = 0
jogo = list()
jogos = list()
nj = int(input('Quantos jogos tu queres que eu gere? '))
print('=' * 30)
print(f"{'JOGOS DA MEGA SENA':^30}")
print('=' * 30)
for c in range (0, nj):
    while True:
        n = randint(1, 60)
        if n not in jogo:
            jogo.append(n)
            cont += 1
        if cont == 6:
            jogos.append(jogo[:])
            cj = ''.join(str(sorted(jogo)))
            cj = cj.center(26, ' ')
            jogo = []
            cont = 0
            break
    print(f'Jogo {c + 1}: {cj} ')
    