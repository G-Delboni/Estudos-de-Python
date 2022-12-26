vel_carro = float(input('Qual a velocidade do veículo (Em Km/h)?: '))
vel_maxima = float(80)

if vel_carro <= vel_maxima:
    print(f'O veículo estava a {vel_carro} Km/h, portanto estava dentro do limite permitido de {vel_maxima}Km/h.')

else: 

    multa = (vel_carro - vel_maxima) * 7
    print(f'O veículo estava a {vel_carro} Km/h, portanto estava fora do limite permitido de {vel_maxima}Km/h e será multado em {multa:.2f}R$.')
