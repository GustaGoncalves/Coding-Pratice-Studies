def ficha(nome_jogador='SEM NOME',gols=0):
 print(f'NOME: {nome_jogador}')
 print('-'*(len(nome_jogador)+6))
 print(f'O jogador {nome_jogador} marcou {gols} gols')


ficha('Zico',3)
print('='*30)
ficha(gols=2)
print('='*30)
ficha(nome_jogador='Ronaldo')
print('='*30)
ficha()