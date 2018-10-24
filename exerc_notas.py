'''
    Leia quatro notas, mostre as notas e a média na tela
'''

notas = []
i = 0
media = 0

while i < 4:
    n = float(input("%dº Nota: " %(i + 1)))
    notas.append(n)
    media += notas[i]
    i += 1

print("Notas: ", notas, "Média = %.2f" %(media / 4))
    
