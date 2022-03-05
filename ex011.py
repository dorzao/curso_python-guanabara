#script que calcula e imprime dimensão de parede e quantos litros de tinta seriam necessários para pintá-la
l = float(input('Qual a largura da tua parede? '))
a = float(input('Agora me diga qual é a altura dela? '))
print('Tu tens uma parede de dimensão {}x{} que tem a área total de {:.2f}m². \n Para pintá-la são necessários {:.2f} litros de tinta!'.format(l, a, l *a, (l * a) / 3))
