from datetime import datetime
dados_trabalhador={}
dados_trabalhador['nome']=str(input('Digite o nome do trabalhador: ')).strip()
dados_trabalhador['data de nascimento']=int(input('Ano de nascimento: '))
dados_trabalhador['carteira de trabalho']=int(input('Carteira de trabalho (0 não tem): '))
dados_trabalhador['idade']=datetime.now().year-dados_trabalhador['data de nascimento']
if dados_trabalhador['carteira de trabalho']!=0:
 dados_trabalhador['ano de contratacao']=int(input('Ano de contratação: '))
 dados_trabalhador['salario']=float(input('Informe o salário: R$'))
 dados_trabalhador['aposentadoria']=((dados_trabalhador['ano de contratacao']+60)-datetime.now().year)+dados_trabalhador['idade']
print('-='*30)
for k,v in dados_trabalhador.items():
 print(f'- {k} tem o valor {v}')
