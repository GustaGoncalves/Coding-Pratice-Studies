nome=str(input('Digite o seu nome: ')).strip()

if nome.upper()=='GUSTAVO':
    print('Homão GOSTOSO!!!')
elif nome.upper() == 'PEDRO' or nome.upper() == 'MARIA':
    print('Teu nome é bem comum')
elif nome.upper() in 'MARIA ANA GIOVANA':
    print('Seu nome é bonito')

print('Tenha um bom dia {}!'.format(nome.capitalize()))