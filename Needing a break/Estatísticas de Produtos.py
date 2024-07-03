print('_'*30)
print(f'{'Loja':^30}')
print('_'*30)
preco_total=0.0
conta_produto_mais1000=preco_mais_baixo=0
produto_mais_barato=' '
while True:
  continuar=' '
  produto=str(input('Nome do produto: ')).strip().lower().capitalize()
  preco=float(input('Preço: R$'))
  if preco_mais_baixo==0:
    preco_mais_baixo=preco
    produto_mais_barato=produto
  if preco<preco_mais_baixo:
    preco_mais_baixo=preco
    produto_mais_barato=produto
  preco_total+=preco
  if preco>=1000:
    conta_produto_mais1000+=1
  while continuar not in 'SsNn':
    continuar=str(input('Continuar a comprar? [S/N]')).strip().upper()[0]
  print('_'*30)
  if continuar in 'Nn':
	  break
print(f'{'COMPRA FINALIZADA':-^30}')
print(f'O valor total da compra é de {preco_total:.2f}')
print(f'Foram comprados {conta_produto_mais1000} produto(s) que custam mais de R$1000.00')
print(f'O produto mais barato foi {produto_mais_barato}, custando {preco_mais_baixo:.2f}')