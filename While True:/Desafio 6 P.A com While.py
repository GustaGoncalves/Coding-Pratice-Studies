print('PROGRESSÃO ARITIMÉTICA')
print('='*22)
loop_progressao=10
termo1=int(input('Digite o \033[36mprimeiro termo\033[m da P.A.: '))
razao=int(input('Digite a \033[33mrazão\033[m da P.A.: '))
cont=0
progressão=termo1
while loop_progressao!=0:
    while cont<loop_progressao:
        print(progressão,end=' ')
        progressão+=razao
        cont+=1
    print('\033[36mAcabou!\033[m')       
    resposta=int(input('Deseja ver mais termos? Digite a quantidade desejada!\n[Digite 0 para encerrar]\n'))
    if resposta==0:
        loop_progressao=resposta
    else:
        loop_progressao+=resposta
print('Ao todo foram mostrados um total de {} termos da Progressão'.format(cont))