lista_numeros=[]
while True:
 resposta=' '
 numero_entrada=(int(input('Digite um número: ')))
 if numero_entrada not in lista_numeros:
  lista_numeros.append(numero_entrada)
 else: 
  print('O valor já está na lista! Desconsidarando...')
 while resposta not in 'SsNn':
  resposta=str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
  if resposta not in 'SsNn':
   print('Tente Novamente!',end=' ')
 if resposta in 'Nn':
  break
lista_numeros.sort()
print(f'Os valores digitados foram: {lista_numeros}')
 