contanumero=soma=numero=0
while numero!=999:
    print('Digite um número')
    numero=int(input('Para parar, digite 999 ou mais: '))
    if numero!=999:
        contanumero+=1
        soma+=numero
print('Ao todo, foram digitados {} número(s)'.format(contanumero))
print('A soma total dos números digitados é de {}'.format(soma))