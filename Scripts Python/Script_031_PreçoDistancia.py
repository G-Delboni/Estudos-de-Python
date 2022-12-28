distancia = float(input('A viagem foi de quantos Km?: '))

if distancia <= 200:
    preço_passagem = distancia * 0.50
    print(f'A viagem de {distancia}Km terá a passagem no valor de R${preço_passagem:.2f}')

else:
    preço_passagem = distancia * 0.45
    print(f'A viagem de {distancia}Km terá a passagem no valor de R${preço_passagem:.2f}')
