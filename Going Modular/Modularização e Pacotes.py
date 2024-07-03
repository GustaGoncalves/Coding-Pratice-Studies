from uteis import numeros


numero=int(input('Digite um número para ver o fatorial: '))
fatorial_main=numeros.fatorial(numero)
dobro_main=numeros.dobro(numero)
triplo_main=numeros.triplo(numero)
print(f'O fatorial de {numero} é {fatorial_main}')
print(f'O dobro de {numero} é {dobro_main}')
print(f'O triplo de {numero} é {triplo_main}')
