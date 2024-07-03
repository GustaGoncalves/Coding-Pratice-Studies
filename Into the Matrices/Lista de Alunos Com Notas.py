lista_alunos=list()
lista_alunos_temporaria=list()
while True:
 resposta=' '
 lista_alunos_temporaria.append(str(input('Digite o nome do aluno: ')))
 lista_alunos_temporaria.append(float(input('Digite a primeira nota do aluno: ')))
 lista_alunos_temporaria.append(float(input('Digite a segunda nota do aluno: ')))
 lista_alunos.append(lista_alunos_temporaria[:])
 lista_alunos_temporaria.clear()
 while resposta not in 'SsNn':
  resposta=str(input('Digitar mais alunos? [S/N] ')).strip().upper()[0]
 if resposta in 'Nn':
  break
print(f'{'-='*15} BOLETIM {'=-'*15}')
print()
for aluno in lista_alunos:
 media=(aluno[1]+aluno[2])/2
 print(f'{'='*5}{aluno[0]}{'='*5}')
 print(f'Nota 1: {aluno[1]:.2f}')
 print(f'Nota 2: {aluno[2]:.2f}')
 print(f'Media: {media:.2f}')
 print('='*(10+len(aluno[0])))