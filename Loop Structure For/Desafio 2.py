from time import sleep
print('\033[36mOLÁ!\033[m Sejá bem-vindo!')
print('Mostrando os números \033[32mpares\033[m de 1 a 50...')
sleep(1)
for c in range (1,51):
    if c%2==0:
        print(c,end=' ')
    sleep(0.1)
