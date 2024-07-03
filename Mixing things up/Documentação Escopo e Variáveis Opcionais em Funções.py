'''from time import sleep

def contador(i,f,p):
 #Docstring, also known as documentation of functionality
 """
    Faz uma contagem e mostra na tela
    Parametro i: Número de inicio da contagem
    Parametro f: Número final do contador
    Paramentro p: Passo da contagem
 """
 f+=1
 for num in range(i,f,p):
  print(num,end=' ')


contador(2,10,2)
help(contador)'''
n=9
z=10
def somar(a=0,b=0,c=0):
 n=8
 global z
 z=7

 """
 Faz a soma de três valores e imprime o valor no terminal.
 param a: o primeiro valor
 param b: o segundo valor
 param c: o terceiro valor
 Função criada por Gustavo Nascimento.
 """
 s=a+b+c
 print(f'A soma vale {s}')
 print(f'Dentro n vale {n} e z vale {z}')
 


#somar(3,2,5)
#somar(8,4)
somar()
#somar(c=2,a=4)
print(f'Fora n vale {n} e z vale {z}')