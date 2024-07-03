lista_numeros=[]
while True:
 resposta=' '
 lista_numeros.append(int(input('Digite um valor: ')))
 while resposta not in 'SsNn':
  resposta=str(input('Quer continuar? [S/N]')).strip().upper()[0]
  if resposta in 'SsNn':
   break
  print('Tente Novamente!')
 if resposta in 'Nn':
  break
lista_numeros.sort(reverse=True)
print(f'Você digitou {len(lista_numeros)} elementos!')
print(f'Os valores em ordem decrescente da lista são {lista_numeros}')
if 5 or -5 in lista_numeros:
 print('O número 5 está presente na lista!')
else:
 print('O número 5 não está presente na lista!')