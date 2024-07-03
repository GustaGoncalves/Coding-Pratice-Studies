expressão=str(input('Digite a expressão: ')).strip()
conta_parentese=0
for index in range(0,len(expressão)):
 if expressão[index] in '()':
  conta_parentese+=1
if conta_parentese%2==0:
 print('A expressão é válida')
if conta_parentese%2!=0:
 print('A expressão está inválida')