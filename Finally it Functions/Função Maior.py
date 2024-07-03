def maior(numeros):
 maior=0
 for numero in numeros:
  if numero>maior:
   maior=numero
 return(maior)

#Main program
numeros_input=[]
while True:
 temporario=int(input('Digite um número (Digite 999 para parar): '))
 if temporario==999:
  break
 numeros_input.append(temporario)
print('-'*30)
numero_maior=maior(numeros_input[:])
print(f'O maior número digitado foi {numero_maior}')