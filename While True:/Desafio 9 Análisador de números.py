contanumero=0
digitar_novamente='S'
soma=0
while digitar_novamente in 'Ss':
    numero=int(input('Digite um número: '))
    if contanumero==0:
        maior=menor=numero
    if numero>maior:
        maior=numero
    if numero<menor:
        menor=numero
    soma+=numero
    contanumero+=1
    digitar_novamente='m'    
    while digitar_novamente!='S' and digitar_novamente!='N':
        digitar_novamente=str(input('Deseja continuar a digitar? [S/N] ')).strip().upper()[0]
        if digitar_novamente!='S' and digitar_novamente!='N':
            print('\033[31mResposta Inválida!\033[m')
            print('Digite apenas \033[33mS[Sim]\033[m ou \033[33mN[Não]\033[m')
media=soma/contanumero
print('O maior número digitado foi {}'.format(maior))
print('O menor número digitado foi {}'.format(menor))
print('A media dos números digitados é {:.2f}'.format(media))
