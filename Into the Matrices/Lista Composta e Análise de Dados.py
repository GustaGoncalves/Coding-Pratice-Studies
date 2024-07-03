dados=list()
pessoas=list()
peso_maior=peso_menor=0
pessoas_mais_pesadas=list()
pessoas_mais_leves=list()

while True:
 resposta=' '
 dados.append(str(input('Digite o nome: ')).strip().lower().capitalize())
 dados.append(float(input('Digite o peso: ')))
 pessoas.append(dados[:])
 dados.clear()

 while resposta not in 'SsNn':
  resposta=str(input('Quer continuar? [S/N] ')).upper()[0]
 if resposta in 'Nn':
  break
 
for peso in pessoas:
 if peso_maior==0 and peso_menor==0:
  peso_maior=peso[1]
  pessoas_mais_pesadas.append(peso[0][:])
  peso_menor=peso[1]
  pessoas_mais_leves.append(peso[0][:])

 else:
  if peso[1]==peso_maior:
   pessoas_mais_pesadas.append(peso[0][:])

  if peso[1]>peso_maior:
   peso_maior=peso[1]
   pessoas_mais_pesadas.clear()
   pessoas_mais_pesadas.append(peso[0][:])

  if peso_menor==peso[1]:
   pessoas_mais_leves.append(peso[0][:])  

  if peso_menor>peso[1]:
   peso_menor=peso[1]
   pessoas_mais_leves.clear()
   pessoas_mais_leves.append(peso[0][:])    
print(f'Foram cadastradas um total de {len(pessoas)} pessoas')
print(f'O maior peso informado foi de {peso_maior:.2f}Kg. Peso de {pessoas_mais_pesadas}')
print(f'O menor peso informado foi de {peso_menor:.2f}Kg. Peso de {pessoas_mais_leves}')