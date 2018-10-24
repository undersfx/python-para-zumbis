'''
    Função para embaralhar string de entrada
'''

def embaralha(n):
    import random
    k = list(n)
    random.shuffle(k)
    return ''.join(k)
