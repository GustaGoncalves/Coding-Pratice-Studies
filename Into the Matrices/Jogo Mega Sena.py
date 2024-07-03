from random import randint
jogos_feitos=list()
jogos=list()
print('-'*35)
print(f'{'MEGA SENA':^35}')
print('-'*35)
qtd_jogos=int(input('Quantos jogos você quer sortear? '))
for sorteio in range(0,qtd_jogos):
 for i in range(0,6):
  jogos.append(randint(1,60))
 jogos_feitos.append(jogos[:])
 jogos.clear()
print(f'{'-='*3} SORTEANDO {len(jogos_feitos)} JOGOS {'=-'*3}')
for jogo in range(0,len(jogos_feitos)):
 print(f'Jogo {jogo+1}: {jogos_feitos[jogo]}')