print('='*30)
print(f'{'BANCO':^30}')
print('='*30)
valor=int(input('Digite o valor a sacar: R$'))
cedulas_50=valor//50
cedulas_20=(valor%50)//20
cedulas_10=((valor%50)%20)//10
cedulas_1=(((valor%50)%20)%10)//1
print(f'''O saque solicitado será entregue em
{cedulas_50} cédulas de R$50
{cedulas_20} cédulas de R$20
{cedulas_10} cédulas de R$10
{cedulas_1} cédulas de R$1''')
