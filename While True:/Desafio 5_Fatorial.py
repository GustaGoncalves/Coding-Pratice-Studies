
print("="*28)
print('{}FATORIAL{}'.format(' '*10," "*10))
print('='*28)
numero=int(input('Digite o número do qual deseja calcular o \033[33mFatorial\033[m: '))
print('Calculando o fatorial de {}'.format(numero))

fatorial=1
print(numero,end='x')
while numero>1:
    fatorial*=numero
    numero-=1
    if numero>1:
        print(numero,end='x')
    else:
        print(numero,end='=')
print(fatorial)
