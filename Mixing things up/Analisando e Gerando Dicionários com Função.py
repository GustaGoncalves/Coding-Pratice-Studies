def notas(lista_notas,situacao=False):
 """
 Generates a dictionary containing all relevant info required for exercise
 param: lista_notas: receives the respective list containing each student and their grades
 param: situacao (optional): If true, will add on the main dictionary the respective situation of each student
 return: returns a copy of the full dictionary
 """
 
 informacoes={}
 situacao_aluno=[]
 situacao_temporario=[]
 informacoes['maior']=0
 informacoes['menor']=0
 soma_notas=0

 #Analysis loop
 for aluno in lista_notas:
  #Sets best and worst student to match 'aluno' on first instance of the loop only
  if soma_notas==0:
   informacoes['maior']=aluno
   informacoes['menor']=aluno
   
  #After first instance, checks if current grade is higher or lower. If true, replaces it accordingly
  if informacoes['maior']['nota']<aluno['nota']:
   informacoes['maior']=aluno
  if informacoes['menor']['nota']>aluno['nota']:
   informacoes['menor']=aluno

  soma_notas+=aluno['nota'] 
  
  #Adds situation for each student if requested
  if situacao:
   if aluno['nota']>=7:
    situacao_temporario.append(aluno['nome'])
    situacao_temporario.append('APROVADO')
   elif aluno['nota']>=5 and aluno['nota']<7:
    situacao_temporario.append(aluno['nome'])
    situacao_temporario.append('RECUPERAÇÂO')
   elif aluno['nota']<5:
    situacao_temporario.append(aluno['nome'])
    situacao_temporario.append('REPROVADO')
   situacao_aluno.append(situacao_temporario[:])
   situacao_temporario.clear()
 if situacao:
  informacoes['situacao']=(situacao_aluno)

 #Calculates class medium
 informacoes['media']=soma_notas/len(lista_notas)

 return(informacoes.copy())
 

#Main program
lista_aluno_nota=[]
lista_temporaria={}

#Main data insert loop
while True:
 lista_temporaria['nome']=str(input('Digite o nome do aluno: ')).strip().capitalize()
 lista_temporaria['nota']=float(input('Digite a nota do aluno: '))
 lista_aluno_nota.append(lista_temporaria.copy())
 lista_temporaria.clear()
 
 #Validates answers so they're always within expected
 while True:
  resposta=str(input('Inserir outro aluno? [S/N]: ')).strip().upper()[0]
  if resposta in 'SsNn':
   break
  print('ERRO! Digite apenas S ou N')
 
 #Stops the loop if answer is 'No'
 if resposta=='N':
  break
 print('-'*30)

#Validates answer in the same fashion as previous validation
while True:
 resposta=str(input('Deseja ver a situação dos alunos? [S/N]: ')).strip().upper()[0]
 if resposta in 'SsNn':
  break

#A bad way of passing through request to add situation of each student
if resposta=='S':
 data_alunos=notas(lista_aluno_nota,situacao=True)
if resposta=='N':
 data_alunos=notas(lista_aluno_nota)

print('='*30)
print(f'A quantidade de alunos digitados foi de {len(lista_aluno_nota)}')
print(f'A maior nota da turma foi de {data_alunos['maior']['nome']} que tirou {data_alunos['maior']['nota']}')
print(f'A menor nota da turma foi de {data_alunos['menor']['nome']} que tirou {data_alunos['menor']['nota']}')
print(f'A média da turma é de {data_alunos['media']:.2f}')

if resposta=='S':
 print('='*30)
 print(f'{' '*7}SITUACÃO DA TURMA{' '*7}')
 print('-'*31)
 for aluno in data_alunos['situacao']:
  print(f'NOME: {aluno[0]} | SITUACÃO: {aluno[1]}')
