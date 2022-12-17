dias_alugados = int(input('Por quantos dias o carro foi alugado? '))
km_percorridos = float(input('Quantos kms foram percorridos? '))

preco_dia = dias_alugados * 60
preco_km = km_percorridos * 0.15
preco_total = preco_dia + preco_km

print(f'O carro foi alugado por {dias_alugados} dias e percorreu {km_percorridos}km , portanto o valor a pagar será de R${preco_total:.2f} ')