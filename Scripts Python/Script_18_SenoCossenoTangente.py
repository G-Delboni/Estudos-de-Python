from math import cos, sin, tan, radians
angulo_graus = float(input('Digite um ângulo: '))
angulo_radianos = radians(angulo_graus)

cosseno = cos(angulo_radianos)
seno = sin(angulo_radianos)
tangente = tan(angulo_radianos)

print(f'O ângulo {angulo_graus} tem cosseno de valor {cosseno:.2f}, seno de valor {seno:.2f} e tangente de valor {tangente:.2f}')
