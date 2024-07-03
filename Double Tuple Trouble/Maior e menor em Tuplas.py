from random import randint
list_numeros_aleatorios=randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10)
maior=list_numeros_aleatorios[0]
menor=list_numeros_aleatorios[0]
for cont in range (0,len(list_numeros_aleatorios)):
 print(list_numeros_aleatorios[cont],end=' ')
 if maior<list_numeros_aleatorios[cont]:
  maior=list_numeros_aleatorios[cont]
 if menor>list_numeros_aleatorios[cont]:
  menor=list_numeros_aleatorios[cont]
print(f'\nO maior número sorteado foi {maior} e o menor foi {menor}')