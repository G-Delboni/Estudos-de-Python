reta1 = float(input('Digite o comprimento de uma reta: '))
reta2 = float(input('Digite o comprimento de outra reta: '))
reta3 = float(input('Digite o comprimento de outra reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2: 
    print(f'As retas de valores {reta1}, {reta2}, {reta3} PODEM formar um triângulo.')

else: 
    print(f'As retas de valores {reta1}, {reta2}, {reta3} NÃO PODEM formar um triângulo.')
