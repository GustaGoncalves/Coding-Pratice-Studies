lista=['Hambúrguer','Suco','Pizza','Pudim']
#Listas são expressas em Python por colchetes, é no contrário das tuplas, podem ser alteradas
print(lista)
lista[3]='Picolé'
print(lista)
#Listas também podem ser extendidas/aumentadas através de comandos como .append(item a ser inserido)
lista.append('Biscoito')
print(lista)
#É possível também acrescentar itens no meio da lista usando o comando .insert(index,item a ser inserido)
lista.insert(0,'Cachorro Quente')
print(lista)
#Pode-se também apagar elementos das listas, usando o comando del variavel[index do item]
del lista[3]
print(lista)
#É possivel usar também o metódo .pop(index do item), apesar desse ser usado para eliminação do último item
lista.pop(1)
print(lista)
lista.pop() #Sem index, o último item é deletado
print(lista)
#Existe ainda o metódo .remove(item que deseja remover) onde se específica qual item será deletado ou retirado
lista.insert(0,'Picolé')
print(lista)
lista.remove('Picolé')
print(lista)
#Note que o remove só irá retirar a primeira ocorrência do elemento específicado
#É possível criar listas partindo de ranges também
lista_num=list(range(4,11))
print(lista_num)
#Note que o range gera uma lista já ordenada, para listas não ordenadas é necessário usar de recursos manuais
#Ou funções como randint() com uso de condicionais lógicos para gerar a lista
from random import randint
lista_rand=[randint(1,10)]
while len(lista_rand)<7:
    num_random=randint(1,10)
    if num_random not in lista_rand:
        lista_rand.append(num_random)
print(lista_rand)
#A lista acima foi produzida aleatoriamente, não contém números que repetem e está desordenada
#É possível, porém ordená-la corretamente usando o metódo .sort()
lista_rand.sort()
print(lista_rand)
#Pode-se ordená-la da forma inversa também
lista_rand.sort(reverse=True)
print(lista_rand)
#Exemplo de análise de dados dentro de uma lista
numeros=[]
numeros.append(5)
numeros.append(4)
numeros.append(9)

for c, v in enumerate(numeros):
    print(f'Na posição {c} encontrei o valor {v}')
lista_A=[1,4,9,5,2]
lista_B=lista_A
lista_B[2]=8
#Usando esse formato porém a ligação não é estabelecida e portanto os valores são alterados separadamente
lista_C=lista_A[:]
lista_C[0]=9
print(lista_A)
print(lista_B)
print(lista_C)
#Note como ambas(A e B) as listas foram alteradas apesar do comando de alteração ser dirigido apenas a lista_B
#O Python cria uma especie de ligação entre duas listas quando igualadas dessa forma, assim quando uma altera também segue a outra
