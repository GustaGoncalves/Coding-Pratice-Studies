print('='*42)
print('{}SEQUÊNCIA DE FIBONACCI'.format(' '*10))
print('='*42)
n=int(input('Digite um número: '))
print('Calculando os {} termos da Sequência de Fibonacci'.format(n))
sequencia1=0
sequencia2=1
fibonacci=0
contador=2
print('{} {}'.format(sequencia1,sequencia2),end=' ')
while contador<n:
    fibonacci=sequencia1+sequencia2
    sequencia1=sequencia2
    sequencia2=fibonacci
    contador+=1
    print(fibonacci,end=' ')
