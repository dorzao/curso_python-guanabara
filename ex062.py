#script gerador de pa, com opção de continuação por números de termos
p = int(input('Digite o primeiro termo: '))
r = int(input('Qual a razão: '))
i = 1
ifi = 10
print(p, end=' -> ')
while i <= ifi:
    if i == ifi:
        print(p + (i * r), end=' -> Pausado \n')
        n = int(input('Quantos termos você quer ver a mais? '))
        ifi = ifi + n
    elif i < ifi:
        print(p + (r * i), end=' -> ')
    i = i + 1
print('Ok! Finalizando Progressão Aritimética. seu {}º termo(último) foi: {}. '.format(ifi, p + (r * ifi)))
