def leiaint(input):
 
 if input.isnumeric():
  return(True)
 else:
  print('ERRO! Tente Novamente')
  return(False)


#Main program
while True:
 numero=input('Digite um número: ')
 if leiaint(numero):
  break