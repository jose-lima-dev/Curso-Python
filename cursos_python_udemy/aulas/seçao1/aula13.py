nome = 'José Soares'
altura = 1.75
peso = 50
imc = peso / (altura * altura)
peso_ideal = peso + imc

#f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}. Seu peso ideal é {peso_ideal:.2f}'

print(linha_1)
print(linha_2)
print(linha_3) 