times=('Palmeiras','Grêmio','Atlético','Flamengo','Botafogo','Bragantino',
       'Fluminense','Athletico-PR','Internacional','Fortaleza','São Paulo',
       'Cuiabá','Corinthians','Cruzeiro','Vasco','Bahia','Santos','Goiás',
       'Coritiba','América')
print('Tabela de times ')
print('Os 5 primeiros colocados são')
'''for index in range(0,5):
 print(f'{index+1}º {times[index]}')'''
print(times[0:5])
print('Os 4 últimos colocados são')
'''for index in range (16,20):
 print(f'{index+1}º {times[index]}')'''
print(times[-1:-5:-1])
print('Os times, em ordem alfabética')
print(sorted(times))
print(f'O time do São Paulo está na posição de {times.index('São Paulo')+1}º')
