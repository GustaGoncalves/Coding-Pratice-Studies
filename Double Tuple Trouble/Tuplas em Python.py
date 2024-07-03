#Tuples are constants, they cannot be changed
lanches='Hambúrguer','Suco','Pizza','Pudim'
index=int(input('Digite o index: '))
print(lanches[index])
print(lanches[1:3])
print(lanches[1:])
print(lanches[-1])
print(lanches[-2:])
#For function comprehends Tuple index limits, and pulls its value directly from the Tuple
for comida in lanches:
 #For each iteration 'comida' will receive, as it's value/data, the equivalent part of the tuple
 #On this case, in order: 'Hambúrguer, Suco, Pizza, Pudim
 print(comida,end=' ')
print()
#It is possible to use the for loop in a different way like so:
for cont in range(0,len(lanches)):
 print(cont)
#NOTE that the print will output an integer instead of the contents of the tuple's index
#This is because when wrote like such, the program understands the value of 'cont' to be in a range
#Of 0 to 4 because len gives out the NUMBER(integer) of itens inside the tuple rather than its contents
#As such is possible to use the 'cont' variable as the index itself for the tuple

#It is possible to use loops similarly with the 'While' function by using the len function
#As it declares de number of itens contained inside the tuple like so
print(len(lanches))
#On loop with while it may go like so:
#NOTE that this IS less efficient than with the For loop in this presented case
contador=0
while contador<len(lanches):
 print(lanches[contador],end=" ")
 contador+=1
print()
#You may sort a tuple using functions like sorted, but it does not change the tuple
print(sorted(lanches))
#It is possible to request the specific index of a given piece of data in the tuple. Follows:
print(lanches)
print(lanches.index('Pizza'))
#IMPORTANT! Tuples are NOT limited to a single type of data, it may contain strings, integers, floats etc.
