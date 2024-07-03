#Calcula a area do retângulo
def calculo_area(comp,alt):
 area=comp*alt
 return(area)


#Main program
comprimento=float(input('Digite o comprimento do retângulo (m): '))
altura=float(input('Digite a altura do triângulo (m): '))
area_main=calculo_area(comprimento,altura)
print(f'A área de um retângulo de comprimento {comprimento} e altura {altura} é de {area_main:.2f}m²')
