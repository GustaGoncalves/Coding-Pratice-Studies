tabela_produtos=('Lápis',1.75,'Borracha',2,'Caderno',15.90,'Estojo',25,
                 'Transferidor',4.2,'Compasso',9.99,'Mochila',120.32,
                 'Canetas',22.3,'Livro',34.9)
print('='*35)
print(f'{'TABELA DE PREÇOS':^35}')
print('='*35)
for index in range(0,len(tabela_produtos)):
 if index%2!=0:
  print(f'R${tabela_produtos[index]:>6.2f}\n')
 if index%2==0:
  print(f'{tabela_produtos[index]:_<26}',end='')