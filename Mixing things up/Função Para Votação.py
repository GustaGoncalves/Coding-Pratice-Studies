def voto(nascimento):
 
 from datetime import datetime
 data_atual=datetime.now().year
 mensagem=''
 idade=data_atual-nascimento
 
 if idade>18 and idade<=70:
  mensagem='VOTO OBRIGATÓRIO'
 elif (idade>=16 and idade<=18) or idade>70:
  mensagem='VOTO OPCIONAL'
 elif idade<16:
  mensagem='NÃO VOTA'
  
 return(mensagem,idade)

#Main program
mensagem_main,idade_main=voto(int(input('Digite o ano de seu nascimento: ')))
print(f'Com {idade_main} anos: {mensagem_main}')
