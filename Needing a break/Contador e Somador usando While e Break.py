soma=0
conta_numero=0
while True:
    numero=int(input('Digite um número\nDigite 999 para encerrar: '))
    if numero==999:
        break
    soma+=numero
    conta_numero+=1
print(f'Foram digitados um total de {conta_numero} numeros')
print(f'O valor total da soma dos números digitados é de {soma}')
