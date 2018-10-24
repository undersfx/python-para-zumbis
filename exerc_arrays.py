'''
    Calcule a média entre 5 notas utilizando Array (list)
'''

notas = [7,9,8,10,4]

soma = 0
x = 0

while x < len(notas):
    soma += notas[x]
    x += 1

print('Média = %.2f' %(soma / len(notas)))
