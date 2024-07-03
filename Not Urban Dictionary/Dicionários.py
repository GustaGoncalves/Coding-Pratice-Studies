dados={'nome':'Pedro','idade':25}
print(dados['nome'])
print(dados['idade'])
dados['sexo']='M'
print(dados)
del dados['idade']
print(dados)
filme={'titulo':'Star Wars',
       'ano':1997,
       'diretor':'George Lucas'
}
print(filme['titulo'])
print(filme['ano'])
print(filme['diretor'])
print(filme.values())
print(filme.keys())
print(filme.items())
for k,v in filme.items():
    print(f'O {k} é {v}')
filme['titulo']='Matrix'
print(f'O diretor de {filme['titulo']} é {filme['diretor']}')
brasil=[]
estado1={'uf':'Rio de Janeiro','sigla':'RJ'}
estado2={'uf':'São Paulo','sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
