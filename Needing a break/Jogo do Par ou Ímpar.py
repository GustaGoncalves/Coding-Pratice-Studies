from time import sleep
from os import system
from random import randint
print('='*30)
print(f'{' '*5}JOGO DO PAR OU ÍMPAR')
print('='*30)
sleep(2)
num_jogador=int(input('Digite o valor: '))
computador=randint(0,10)
total_parouimpar=computador+num_jogador
contador_vitoria=0
while True:
  par_ou_impar=str(input('Vai escolher Par ou Ímpar [P/I] ')).strip().upper()
  if par_ou_impar in 'PpIi':
    break
  system('cls')
  print('\033[31mResposta Inválida!\033[m\nDigite \033[36mP\033[m ou \033[36mI\033[m')
print(f'Você jogou {num_jogador} e o computador {computador}. O total é de {total_parouimpar}')
if par_ou_impar in 'Pp' and total_parouimpar%2==0 or par_ou_impar in 'Ii' and total_parouimpar%2==1:
  contador_vitoria+=1
while True:
  if contador_vitoria==0:
    break
  print('\033[32mVOCÊ VENCEU!\033[m Vamos jogar denovo...')
  sleep(4)
  system('cls')
  num_jogador=int(input('Digite o valor: '))
  while True:
    par_ou_impar=str(input('Vai escolher Par ou Ímpar [P/I] ')).strip().upper()[0]
    if par_ou_impar in 'PpIi':
      break
    system('cls')
    print('\033[31mResposta Inválida!\033[m\nDigite \033[36mP\033[m ou \033[36mI\033[m')
  computador=randint(0,10)
  total_parouimpar=computador+num_jogador
  print(f'Você jogou {num_jogador} e o computador {computador}. O total é de {total_parouimpar}')
  if par_ou_impar in 'Pp' and total_parouimpar%2==0 or par_ou_impar in 'Ii' and total_parouimpar%2==1:
    contador_vitoria+=1
  else:
    system('cls')
    print(f'Você jogou {num_jogador} e o computador {computador}. O total é de {total_parouimpar}')
    break
print('\033[31mVOCÊ PERDEU!\033[m Que pena!')
if contador_vitoria>0:
  print(f'Você venceu {contador_vitoria} vezes')
