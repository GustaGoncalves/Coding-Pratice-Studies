'''def mostra_linha():
 print('-'*30)

 
def mensagem_sistema(msg):
 mostra_linha()
 print(msg)
 mostra_linha()

 
def mensagem_cadastro(msg):
 mostra_linha()
 print(msg)
 mostra_linha()

 
def mensagem_erro(msg):
 mostra_linha()
 print(msg)
 mostra_linha()

 
#Programa principal
mensagem_sistema('SISTEMA DE ALUNOS')
mensagem_cadastro('CADASTRO DE ALUNOS')
mensagem_erro('ERRO DO SISTEMA')'''

'''def soma(a,b):
 print(f'A={a} e B={b}')
 s=a+b
 print(f'A+B é igual a {s}')


#Programa principal
soma(b=4,a=5)
print()
soma(4,5)
print()
soma(8,9)
print()
soma(2,1)'''

'''def contador(*num):
 print(num)
 print(type(num))
 for valor in num:
  print(valor, end=' ')
 print('FIM!')


contador(5,7,3,1,4)
contador(8,4,7)
contador(8,0)'''

def dobra(lst):
 pos=0
 print(type(lst))
 while pos<len(lst):
  lst[pos]*=2
  pos+=1
 return(lst)

#Programa principal
valores=[7,2,5,0,4]
dobro=dobra(valores[:])
print(valores)
print(dobro)