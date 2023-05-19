dinheiro = float(input('Qual o valor na sua carteira ? '))
dolar = dinheiro / 5.28
euro = dinheiro / 5.95
iene = dinheiro / 0.046
print('Com R${} reais, você pode converter em: \n{:.2f} dólares \n{:.2f} euros \n{:.2f} ienes'.format(dinheiro, dolar, euro, iene))