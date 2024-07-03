numeros_extenso=('zero','um','dois','três','quatro','cinco',
                 'seis','sete','oito','nove','dez',
                 'onze','doze','treze','catorze','quinze',
                 'dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
 numero_index=int(input('Digite um número de 0 a 20: '))
 if 0<=numero_index<=20:
  break
 print('Tente novamente!', end=' ')
print(f'Você digitou o número {numeros_extenso[numero_index]}')
