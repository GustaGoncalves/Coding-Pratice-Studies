jogadores=[]
jogos_jogador=[]
dados_jogador={}

#Main loop for adding players
while True:
 dados_jogador['nome']=str(input('Digite o nome do jogador: ')).strip()
 dados_jogador['partidas']=int(input(f'Quantas partidas {dados_jogador['nome']} jogou? '))
 dados_jogador['total de gols']=0

 #Goal add loop
 for i in range(0,dados_jogador['partidas']):
  gol=int(input(f'Quantos gols foram marcados na {i+1}ª partida? '))
  jogos_jogador.append(gol)
  dados_jogador['total de gols']+=gol

 #Main dict copying
 dados_jogador['gols']=jogos_jogador[:] 
 jogadores.append(dados_jogador.copy())

 #Temporary sets clear
 dados_jogador.clear()
 jogos_jogador.clear()

 #Ensures answer is either 'S' or 'N'
 while True:
  resposta=str(input('Cadastrar outro jogador? [S/N]')).strip().upper()[0]
  if resposta in 'SsNn':
   break
  print('ERRO! Digite apenas S ou N')

 if resposta in 'Nn':
  break

 #For test purposes
 '''print(dados_jogador)
 print(jogos_jogador)
 print(jogadores)
 print('-='*30)'''

#Display loop
while True:
 print('De qual jogador deseja ver a performance?')
 for i in range(0,len(jogadores)):
  print(f'[{i+1} {jogadores[i]['nome']}')

 #Ensures answers remain within displayed range 
 while True:
  escolha=int(input('Digite o número correspondente: (Digite 0 para encerrar) '))
  if escolha>=0 or escolha<=len(jogadores):
   break
  print('ERRO! Digite uma resposta válida!')

 #Stops when zero
 if escolha==0:
  break
 
 #Decrement in one for correct indexing
 escolha-=1

 #Display currently selected information/data
 print('-'*30)
 for k,v in jogadores[escolha].items():
  print(f'- o campo {k} tem o valor {v}')
 print('-='*30)

 #Displays currently selected player information
 print(f'O jogador {jogadores[escolha]['nome']} jogou {jogadores[escolha]['partidas']} partidas')
 for partida,gols in enumerate(jogadores[escolha]['gols']):
  print(f'Na {partida+1}ª partida {jogadores[escolha]['nome']} marcou {gols} gols')
