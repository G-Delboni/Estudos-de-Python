nome = input('Digite seu nome completo: ').title().strip()
dividido = nome.split()
dividido = dividido[0]

print(f'Seu nome em letras maiúsculas fica: {nome.upper()}')
print(f'Seu nome em letras minúsculas fica: {nome.lower()}')
print(f'Seu nome tem ao todo: {len(nome.replace(" ", ""))} letras.')
print(f'Seu primeiro nome é: {dividido} e tem {len(dividido)} letras.')