def leiadinheiro(mensagem):
 """
 Realiza uma validação de dados, garantindo que sejam digitados apenas números
 param: mensagem: mensagem de prompt para o usúario digitar o valor desejado
 """

 valido=False
 
 while not valido:
  valor=input(mensagem).replace(',','.')
  if valor.isalpha() or valor.strip()=='':
   print(f'Erro! "{valor}" não é um valor válido!')
  else:
   valido=True
   return float(valor)
