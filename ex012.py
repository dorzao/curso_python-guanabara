#script pergunta o preço cheio do produto, e mostra o novo valor com 5% de desconto e depois ainda mostra o valor do desconto
p = float(input('Digite o preço cheio do produto: R$ '))
print('Um produto que custava R$ {:.2f} agora com 5% de desconto custa R${:.2f}. \n O desconto foi de R$ {:.2f}'.format(p, p * 0.95, p * 0.05))
