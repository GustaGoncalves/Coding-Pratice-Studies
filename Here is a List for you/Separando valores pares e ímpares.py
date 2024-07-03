lista_numeros=[]
lista_par=[]
lista_impar=[]
while True:
 resposta=' '
 lista_numeros.append(int(input('Digite um valor: ')))
 while resposta not in 'SsNn':
  resposta=str(input('Quer continuar? [S/N] ')).strip().upper()[0]
  if resposta not in 'SsNn':
   print('Resposta Inváida! ',end='')
 if resposta in 'Nn':
  break
for numero in lista_numeros:
 if numero%2==0:
  lista_par.append(numero)
 else:
  lista_impar.append(numero)
print(f'Você digitou os valores {lista_numeros}')
print(f'Os valores pares da lista são {lista_par}')
print(f'Os valores ímpares da lista são {lista_impar}')