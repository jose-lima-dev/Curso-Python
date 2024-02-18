"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# num_int = input('Digite um número inteiro: ')
# if num_int.values(0):
#     print('Número par.')
# else:
#     print('Número impar.')
    
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = int(input('Que hora é? '))

manha = horario >= 0 and horario <= 11
tarde = horario >= 12 and horario <= 17
noite = horario >= 18 and horario <= 23

if manha:
    print(f'Bom dia, são {horario} horas.')
elif tarde:
    print(f'Boa tarde, são {horario} horas.')
elif noite:
    print(f'Boa noite, são {horario} horas.')
else:
    print('Nenhum valor digitado.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

