pessoas_cadastradas=[]
pessoa={}
soma_idade=0
lista_mulheres=[]
pessoas_acima_idade_media=[]
while True:
 pessoa['nome']=str(input('Digite o nome: ')).strip()
 
 #Loop ensures input is only M or F
 while True:
  pessoa['sexo']=str(input('Digite o sexo [F/M]: ')).strip().upper()[0]
  if pessoa['sexo'] in 'MmFf':
   break
  print('ERRO! Digite apenas F ou M')

 pessoa['idade']=int(input('Digite a idade: '))

 soma_idade+=pessoa['idade']
 pessoas_cadastradas.append(pessoa.copy())
 
 if pessoa['sexo'] in 'Ff':
  lista_mulheres.append(pessoa.copy())

 pessoa.clear()

 #Loop ensures input is only M of F
 while True:
  resposta=str(input('Registrar outra pessoa? ')).strip().upper()[0]
  if resposta in 'SsNn':
   break
  print('ERRO! Digite apenas S ou N')

 if resposta in 'Nn':
  break

media=soma_idade/len(pessoas_cadastradas)

for p in pessoas_cadastradas:
 if p['idade']>media:
  pessoas_acima_idade_media.append(p.copy())

print('Lista de mulheres digitadas')
print(30*'=')
for mulher in lista_mulheres:
 for k,v in mulher.items():
  print(f'- {k} tem o valor {v}')
 print('-'*30)

print('-='*30)
print(f'A média de idade é {media:.2f} anos')
print('-='*30)

print('Lista de pessoas acima da média de idade')
print('='*30)
for p in pessoas_acima_idade_media:
 for k,v in p.items():
  print(f'- {k} tem o valor {v}')
 print('-'*30)