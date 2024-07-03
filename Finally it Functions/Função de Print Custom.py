def escreva(mensagem):
 tamanho=len(mensagem)+4
 print('='*tamanho)
 print(f'  {mensagem}')
 print('='*tamanho)


frase=str(input('Digite uma mensagem: ')).strip()
escreva(frase)
