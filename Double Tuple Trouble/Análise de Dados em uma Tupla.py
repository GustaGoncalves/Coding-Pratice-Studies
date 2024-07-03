numero=(int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))
contador_9=0
posição_primeiro_3=0
numero_par=0
for index in range(0,len(numero)):
 if numero[index]==9:
  contador_9+=1
 if numero[index]==3 and posição_primeiro_3==0:
  posição_primeiro_3=index+1
 if numero[index]%2==0:
  numero_par+=1
print(f'O número 9 apareceu um total de {contador_9} vezes')
print(f'O número 3 apareceu pela primeira vez na {posição_primeiro_3}º')
print(f'Foram digitados {numero_par} números pares')
print('São eles: ',end='')
for numero_par in numero:
 if numero_par%2==0:
  print(numero_par,end=' ')
'''print(f'O número 9 apareceu um total de {numero.count(9)} vezes')
print(f'O número 3 apareceu pela primeira vez na posição {numero.index(3)+1}')'''