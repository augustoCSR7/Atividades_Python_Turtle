larg = float(input('Digite a largura: '))
altu = float(input('Digite a altura: '))
tint = (larg * altu)/2
print('Sua parede tem a dimensão de {:.1f} x {:.1f} e sua área é de {:.1f} m² \nPara pintar essa parede, você precisará de {:.1f}L de tinta'.format(larg, altu, larg*altu, tint))