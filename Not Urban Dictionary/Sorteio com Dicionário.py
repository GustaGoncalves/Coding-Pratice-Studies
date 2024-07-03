from random import randint
from operator import itemgetter
Jogos={'Jogador1': randint(1,6),
       'Jogador2': randint(1,6),
       'Jogador3': randint(1,6),
       'Jogador4': randint(1,6)

}
ranking=sorted(Jogos.items(),key=itemgetter(1),reverse=True)
for k,v in ranking:
 print(f'{k} sorteou o número {v}')