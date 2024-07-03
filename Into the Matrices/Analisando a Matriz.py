matriz=list()
numeros_linha=list()
soma_pares=0
soma_coluna_3=0
maior_linha_2=0
for i in range(0,3):
 for k in range(0,3):
  numeros_linha.append(int(input('Digite um valor: ')))
 matriz.append(numeros_linha[:])
 numeros_linha.clear()
for linha in range(0,len(matriz)):
 for coluna in range(0,len(matriz[linha])):
  if matriz[linha][coluna]%2==0:
   soma_pares+=matriz[linha][coluna]
  if matriz[linha][coluna]==matriz[linha][2]:
   soma_coluna_3+=matriz[linha][coluna]
  if matriz[1][coluna]>maior_linha_2:
   maior_linha_2=matriz[1][coluna]
print(f'A soma dos valores pares é de {soma_pares}')
print(f'A soma dos valores da 3º coluna é de {soma_coluna_3}')
print(f'O maior valor da segunda linha é {maior_linha_2}')
