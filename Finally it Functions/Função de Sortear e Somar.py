from random import randint

def sorteia_numeros():
 numeros_sorteados=[]
 for i in range(0,5):
  numeros_sorteados.append(randint(1,10))
 return(numeros_sorteados[:])


def somar_par(lista_numeros):
 total_par=0
 for numero in lista_numeros:
  if numero%2==0:
   total_par+=numero
 return(total_par)


#Main program
numeros_main=sorteia_numeros()
total_par_main=somar_par(numeros_main)
print(f'Foram sorteados os números {numeros_main}')
print(f'A soma dos números pares é de {total_par_main}')
