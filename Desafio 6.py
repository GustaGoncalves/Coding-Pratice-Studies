alt=float(input('Digite a altura da parede: '))
larg=float(input('Digite a largura da parede: '))
area=alt*larg
tintalit=area/2

print('A area de uma parede com {} de largura e {} de altura é {:.2f}'.format(larg,alt,area))
print('Você precisará de {:.2f} litros de tinta para pintá-la'.format(tintalit))

