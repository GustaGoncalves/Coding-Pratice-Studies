lista_num=[]
maior=0
#index_maior=0
menor=0
#index_menor=0
for contador in range(0,5):
 lista_num.append(int(input('Digite um número: ')))
for index,numero in enumerate(lista_num):
 if menor==0:
  maior=menor=numero
  #index_menor=index_maior=index
 if numero>maior:
  maior=numero
  #index_maior=index
 if menor>numero:
  menor=numero
  #index_menor=index
print('Você digitou os números: ',end='')
for num in lista_num:
 print(num,end=' ')
#print(f'\nO maior número digitado foi {maior} na posição {index_maior+1}')
print(f'\nO maior número digitado foi {maior} nas posições',end=' ')
for index,numero in enumerate(lista_num):
 if numero==maior:
  print(index+1,end=' ')
#print(f'O menor número digitado foi {menor} na posição {index_menor+1}')
print(f'\nO menor número digitado foi {menor} nas posições',end=' ')
for index,numero in enumerate(lista_num):
 if numero==menor:
  print(index+1,end=' ')
