lista=('Aprender','Programar','Linguagem','Python','Curso','Gratis',
       'Estudar','Praticar','Trabalhar','Mercado','Programador','Futuro')
for contador in lista:
 print(f'\nNa palavra {contador.upper()} temos as vogais: ',end='')
 for cont_vogal in range(0,len(contador)):
  if contador[cont_vogal] in 'AaEeIiOoUu':
   print(contador[cont_vogal],end=' ')
