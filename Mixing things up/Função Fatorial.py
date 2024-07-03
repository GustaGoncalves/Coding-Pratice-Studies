def fatorial_funcao(numero,show=False):
 """
 Calcula o fatorial de um número
 param: numero: O número do qual se calculará o fatorial
 param: show: (opcional), se deve ou não mostrar o processo do cálculo (conta)
 return: retorna o valor do fatorial de numero
 """
 
 from time import sleep
 fatorial_total=1
 for i in range(numero,0,-1):
  if show and i>1:
   print(f'{i}',end=' x ')
   sleep(0.3)
  fatorial_total*=i

 if show:
  print(f'1 = {fatorial_total}')
 return(fatorial_total)


#Main program
numero_main=int(input('Digite um número para ver o fatorial: '))

#Ensures responses remain within the expected
while True:
 resposta=str(input('Deseja ver o processo na tela? [S/N] ')).strip().upper()[0]
 if resposta in 'SsNn':
  break
 print('ERRO! Responda com apenas S ou N')

if resposta=='S':
 resposta=True
if resposta=='N':
 resposta=False

fatorial_main=fatorial_funcao(numero_main,resposta)
print('-'*20)
print(f'O fatorial de {numero_main} é {fatorial_main}')