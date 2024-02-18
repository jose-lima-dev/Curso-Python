entrada = input('Entrar ou Sair: ')
senha_digitada = input('Digite sua senha: ')

senha = '123'
if entrada == 'E' and senha_digitada == senha:
    print('Você entrou no sistema.')
elif entrada == 'S':
    print('Você saiu do sistema.')
elif entrada == 'E' and senha_digitada != senha:
    print('Você digitou a senha errada.')
elif entrada == 'S':
    print('Sair')
else:
    print('Digite novamente.')
    
# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor
# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)