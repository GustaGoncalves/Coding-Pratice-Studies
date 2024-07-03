from time import sleep
from os import system
numero=int(input('Digite o número do qual deseja ver a tabuada: '))
while True:
    print(f'Calculando a tabuada do {numero}',end='')
    sleep(0.5)
    print('.',end='')
    sleep(0.5)
    print('.',end='')
    sleep(0.5)
    print('.')
    sleep(0.5)
    print('='*20)
    for tabuada in range(1,11):
        print(f'{numero} X {tabuada} = {numero*tabuada}')
        sleep(0.4)
    print('='*20)
    print('Deseja ver outra tabuada? Digite qual')
    numero=int(input('Digite um número negativo (Ex. -1) para encerrar: '))
    if numero<=-1:
        break
    system('cls')
