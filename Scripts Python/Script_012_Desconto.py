valortotal = float(input('Digite o valor do produto R$'))

desconto = valortotal * 0.05
valornovo = valortotal - desconto

print(f'O produto de R${valortotal:.2f}, com 5% de desconto, custarĂ¡ R${valornovo:.2f}')