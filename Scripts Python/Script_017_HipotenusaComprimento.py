from math import sqrt

cat_oposto = float(input('Digite o comprimento do cateto oposto: '))
cat_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = sqrt((cat_oposto**2)+(cat_adjacente**2)) #r² = co² + ca²

print(f'A hipotenusa de um triângulo retângulo cujo cateto oposto é {cat_oposto} e o cateto adjacente é {cat_adjacente} é {hipotenusa:.2f}')
