'''contador=1
while True:
    print(contador,end=" ")
    contador+=1
print('Acabou')'''

'''n=s=0
while True:
    n = int(input('Digite um número: '))
    if n==999:
        break
    s+=n
#print('A soma dos número foi {}'.format(s))
print(f'A soma vale {s}')'''

'''nome='José'
idade=33
print(f'O {nome} tem {idade} anos')'''
nome='José'
idade=33
salario=1000.7
print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}')

import os
from time import sleep
os.system('cls')
sleep(2)
print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}')
