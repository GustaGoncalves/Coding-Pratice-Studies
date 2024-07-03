import math
import emoji
from math import floor
import random
num=int(input('Digite um número: '))
raiz=math.sqrt(num)
num2=random.random()
num3=random.randint(1,10)


print('A raiz quadrada do número {} é {}'.format(num,raiz))

print('A raiz do número {} arredonda para cima é {}'.format(num,math.ceil(raiz)))
print('A raiz do número {} arredonda para baixo é {}'.format(num,floor(raiz)))

print(num2)
print(num3)

print(emoji.emojize(':smiling_face_with_sunglasses:'))
