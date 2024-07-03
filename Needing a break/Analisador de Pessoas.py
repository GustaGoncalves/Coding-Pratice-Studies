conta_mais18=0
conta_homem=0
conta_mulher_mais20=0
while True:
  continuar=' '
  sexo=' '
  nome=str(input('Digite o nome: ')).strip().lower().capitalize()
  while sexo not in 'MmFf':
    sexo=str(input('Qual o sexo? [M/F] ')).strip().upper()[0]
    if sexo not in 'MmFf':
      print('Resposta Inválida! Tente Novamente')
  idade=int(input('Digite a idade: '))
  if idade>18:
    conta_mais18+=1
  if sexo in 'Mm':
    conta_homem+=1
  if idade>20 and sexo in 'Ff':
    conta_mulher_mais20+=1  
  while continuar not in 'SsNn':
    continuar=str(input('Cadastrar outra pessoa? [S/N] ')).strip().upper()[0]
    if continuar not in 'SsNn':
      print('Resposta Inválida! Tente novamente')  
  if continuar in 'Nn':
    break
print(f'O total de pessoas com mais de 18 anos é de {conta_mais18}')
print(f'O total de homens cadastrados é de {conta_homem}')
print(f'O total de mulheres com mais de 20 anos é de {conta_mulher_mais20}')
