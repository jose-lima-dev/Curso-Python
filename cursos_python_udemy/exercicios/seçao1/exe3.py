# nome = input('Digite seu nome: ')
# idade = input('Digite sua idade: ')
# print(10 * '-')
# if nome and idade:
#     print(f'Seu nome é {nome}.')
#     print(f'Seu nome invertido é {nome[::-1]}')
#     print(f'Seu nome contém (ou não) ')
#     print(f'Seu nome tem {len(nome)}.')
#     print(f'A primeira letra do seu nome é {nome[0]}')
#     print(f'A ultima letra do seu nome é {nome[-1]}')
# else:
#     print('Desculpe, você deixou campos em branco.')

nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios.")