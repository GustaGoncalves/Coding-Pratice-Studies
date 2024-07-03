lista_numeros=[[],[]]
for i in range(0,7):
	numero=int(input('Digite um valor: '))
	if numero%2==0:
		lista_numeros[0].append(numero)
	else:
		lista_numeros[1].append(numero)
print(f'Os números pares digitados foram {lista_numeros[0]}')
print(f'Os números impares digitados foram {lista_numeros[1]}')
