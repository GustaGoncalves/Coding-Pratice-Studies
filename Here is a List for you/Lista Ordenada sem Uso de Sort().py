lista_numeros=[]
for contador in range(0,5):
 numero=int(input('Digite um valor: '))
 if len(lista_numeros)==0 or numero>lista_numeros[-1]:
  lista_numeros.append(numero)
  print('Adicionando valor ao final da lista...')
 else:
  for contador in range(0,len(lista_numeros)):
   if lista_numeros[contador]>=numero:
    lista_numeros.insert(contador,numero)
    print(f'Adicionando valor na posição {contador}...')
    break
print(lista_numeros)
