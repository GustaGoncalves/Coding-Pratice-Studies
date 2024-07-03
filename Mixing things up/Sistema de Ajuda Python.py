def help_system(comando):
 print(help(comando))


while True:
 comando_entrada=str(input('Digite um comando ou biblioteca: ')).strip()
 if comando_entrada.upper()=='FIM':
  break
 help_system(comando_entrada)
