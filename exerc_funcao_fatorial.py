'''
    Função que retorna o fatorial de n
'''

def fat(n):
    fat = 1

    while n >= 1:
        fat = fat * n
        n = n - 1

    return (fat)
