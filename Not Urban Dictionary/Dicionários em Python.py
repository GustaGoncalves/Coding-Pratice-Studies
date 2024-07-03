dados={}
dados['nome']=str(input('Digite o nome do aluno: ')).strip()
dados['nota 1']=float(input('Digite a primeira nota do aluno: '))
dados['nota 2']=float(input('Digite a segunda nota do aluno: '))
dados['media']=(dados['nota 1']+dados['nota 2'])/2
if dados['media']>7:
 dados['situação']='Aprovado'
else:
 dados['situação']='Reprovado'
for k,v in dados.items():
 print(f'{k}: {v}'if type(v)!=type(dados['nota 1']) else f'{k}: {v:.1f}')
 