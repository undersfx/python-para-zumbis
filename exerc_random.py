'''
    Gerar uma lista de 15 números aleatórios entre 10 e 100 diferentes entre si
'''

import random
lista = []

while len(lista) < 15:
    x = int(random.randint(10, 100))

    if x not in lista:
        lista.append(x)

lista.sort()   
print(lista)
