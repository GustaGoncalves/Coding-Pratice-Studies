from os import system
dados=['Pedro',25]
dados2=['Maria',19]
dados3=['João',32]
pessoas=list()
pessoas.append(dados[:])
pessoas.append(dados2[:])
pessoas.append(dados3[:])
#Uma lista dentro de outra lista
print(pessoas)
print(pessoas[0])
pessoas2=[['Pedro',25],['Maria',19],['João',32]]
print(pessoas2)
print(pessoas[0])
#O segundo index refere-se ao index da lista interna, no primeiro caso [0] para a lista pessoas
#E o segundo [0] para indicar o index da lista onde esta ['Pedro',25]
print(pessoas2[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
input('Aperte ENTER para continuar\n')
system('cls')
teste=list()
teste.append('Gustavo')
teste.append('22')
galera=list()
galera.append(teste[:])
teste[0]='Maria'
teste[1]=22
galera.append(teste[:])
print(galera)
teste[0]='João'
teste[1]=19
galera.append(teste[:])
teste[0]='Ana'
teste[1]=32
galera.append(teste[:])
#O método append cria uma ligação entre as listas, sendo assim, quando a original é afetada, tudo que foi
#Relacionado a ela via append também é alterado
#Para evitar isso usa-se [:] como index para indicar a criação de uma cópia ao invés de uma vinculação
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
#É possível usar loops da forma acima usando um index fixo para poder requisitar informações específicas de uma lista inteira
#É possível também usar múltiplos loops para requisitar multiplas informações diferentes de indexes diferentes para análises por exemplo
for p in galera:
    print(p)
#Ou ainda utilizar da forma mais simples para requisitar as partes inteiras das listas internas presentes na lista mãe
#Com isso pode-se criar laços similares para inserção de dados, para criar uma base de dados
dado=list()
base_de_pessoas=list()
total_maior_de_idade=total_menor_de_idade=0
for i in range(0,4):
    dado.append(str(input('Digite o nome da pessoa: ')))
    dado.append(int(input('Digite a idade da pessoal: ')))
    base_de_pessoas.append(dado[:])
    dado.clear()
print(base_de_pessoas)
#A partir disso é possível gerar análises usando condicionais, como mostrar os dados apenas das pessoas maiores de idade
for p in base_de_pessoas:
    if p[1]>=18:
        print(f'{p[0]} é maior de idade')
        total_maior_de_idade+=1
    else:
        print(f'{p[0]} é menor de idade')
        total_menor_de_idade+=1
print(f'{total_maior_de_idade} são maiores de idade e {total_menor_de_idade} são menor de idade')
