largura = float(input('Digite a largura da parede '))
altura = float(input('Digite a altura da parede '))

area = largura * altura
tinta = area / 2

print(f'A quantidade de tinta necessária para pintar {area:.2f} m² de parede é {tinta:.2f}L')