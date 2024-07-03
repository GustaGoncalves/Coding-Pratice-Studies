def contador(comeco,fim,passo):
 print('-'*12)

 #Decrement or increment variable to ensure proper counting
 if comeco<fim:
  fim+=1
 if comeco>fim:
  fim-=1

 #Ensures it never goes infinite
 if passo==0:
  passo=1
 for i in range(comeco,fim,passo):
  print(i,end=' -> ')
 print('ACABOU!')


#Main program
print('  CONTADOR')
print('-'*12)
numero_primeiro=int(input('Digite o ínicio: '))
numero_ultimo=int(input('Digite o número final: '))
numero_passo=int(input('Digite o passo: '))
contador(numero_primeiro,numero_ultimo,numero_passo)
