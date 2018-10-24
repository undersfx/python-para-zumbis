'''
    Ler cinco valores e adicionalos a um vetor,
    Ao final, imprimir o vetor criado
'''

vetor = []
x = 0

while x < 5:
    valor = input("Número da posição %d: " %x)
    vetor.append(valor)
    x += 1

print ("Valores do Vetor:", vetor)
