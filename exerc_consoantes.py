'''
    Leia 10 caracteres minusculos e diga quantas consoantes foram lidas
'''

vetor = []
vogais = ['a','e','i','o','u']
i = 0
count = 0

while i < 10:
    n = input("%dº Caractere: " %(i+1))
    vetor.append(n)

    # Comparação com vogais forma ruim
    #if n != 'a' and n != 'e' and n != 'i' and n != 'o' and n != 'u':

    # Forma Pythonica
    if vetor[i] not in vogais:
        count +=1
    
    i += 1

print('Número de consoantes = %d' %count)
