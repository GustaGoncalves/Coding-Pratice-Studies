dias=int(input('Quantos dias alugados? '))
kmrod=float(input('Quantos quilomêtros rodados? '))

diaspag=dias*60
kmpag=kmrod*0.15
totalpag=diaspag+kmpag

print('O valor total a pagar é {:.2f}'.format(totalpag))
