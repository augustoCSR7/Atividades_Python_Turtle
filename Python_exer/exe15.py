km = float(input('Quantidade de km percorridos: '))
dias = float(input('Quantidade de dias: '))
preço = (dias*60)+(km*0.15)
print('O total a pagar é R${:.2f}'.format(preço))