def aumenta(valor=0,taxa=0,format=False):
 """
 Aumenta o valor segunda a taxa informada em porcento
 param: valor: o valor que será aumentado
 param: taxa: taxa em que se aumentará em porcento
 param: format: se deve ou não formatar o valor para conter ',' ao invés de '.'
 return: retorna o valor diminuido
 """

 valor_aumentado=valor+((taxa/100)*valor)
 if format==False:
  return valor_aumentado
 else:
  return formatar_moeda(valor_aumentado)


def diminui(valor=0,taxa=0,format=False):
 """
 diminui o valor segunda a taxa informada em porcento
 param: valor: o valor que será diminuido
 param: taxa: taxa em que se diminuirá em porcento
 param: format: se deve ou não formatar o valor para conter ',' ao invés de '.'
 return: retorna o valor diminuido
 """

 valor_diminuido=valor-((taxa/100)*valor)
 if format==False:
  return (valor_diminuido)
 else:
  return formatar_moeda(valor_diminuido)

def dobro(valor=0,format=False):
 """
 Dobra o valor segunda a taxa informada em porcento
 param: valor: o valor que será dobrado
 param: format: se deve ou não formatar o valor para conter ',' ao invés de '.'
 return: retorna o dobro do valor
 """

 valor_dobro=valor*2
 if format==False:
  return valor_dobro
 else:
  return formatar_moeda(valor_dobro)


def metade(valor=0,format=False):
 """
 Divide o valor pela metade
 param: valor: valor o qual será divido pela metade
 param: format: Se deve ou não formatar o valor para conter ',' ao invés de '.'
 return: retorna a metade do valor
 """

 valor_metade=valor/2
 if format==False:
  return valor_metade
 else:
  return formatar_moeda(valor_metade)


def formatar_moeda(valor, cifrao='R$'):
 """
 Formata o valor para conter ',' ao invés de '.'
 param: valor: valor que será formatado
 param: cifrao: contém o cifrão e símbolo da moeda brasileira, o Real
 return: retorna o valor formatado
 """

 return f'{cifrao}{valor:.2f}'.replace('.',',')


def resumo(valor,taxa_aumento,taxa_diminui):
 """
 Gerá um resumo analisando o valor informado
 param: valor: valor do qual se fará o resumo
 param: taxa_aumento: taxa a qual o valor será aumentado em porcento
 param: taca_diminui: taxa a qual o valor será diminuido em porcento
 """

 print('-'*30)
 print('RESUMO DO VALOR'.center(30))
 print('-'*30)
 print(f'Valor analisado: \t{formatar_moeda(valor)}')
 print(f'Dobro do Valor: \t{dobro(valor,True)}')
 print(f'Metade do Valor: \t{metade(valor,True)}')
 print(f'{taxa_aumento}% de Aumento: \t{aumenta(valor,taxa_aumento,True)}')
 print(f'{taxa_diminui}% de Redução: \t{diminui(valor,taxa_diminui,True)}')
 print('-'*30)
 
