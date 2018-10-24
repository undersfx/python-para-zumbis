'''
    Ler um vetor de 10 números reais, e ao final mostra-los na ordem inversa
'''

vetor = []
i = 0

# Populando array com input

while i < 10:
    n = input("Número da posição %d: " %i)
    vetor.append(n)
    i += 1

# Mostrando array na Ordem Inversa

while i > 0:
    print("Número da posição %d = %.1f" %(i, float(vetor[i - 1])))
    i -= 1
    
