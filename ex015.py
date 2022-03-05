#script que mostra o preço de o aluguél de um carro com base no número de dias e km rodados (60/d 0,15/km)
d = int(input('Quantos dias o carro ficou alugado? '))
k = int(input('Quantos Kms ele rodou? '))
print('Tendo rodado {} dias e {} Kms, o total a se pagar é R$ {:.2f}'.format(d, k, (d * 60) + (k * 0.15)))
