'''
    Calcular a média entre 10 números Inteiros
'''

n = 1
soma = 0

while n <= 10:
    x = int(input("Digite o %d º número: " %n))
    soma = soma + x
    n = n + 1
print("Média: %5.2f" %(soma/10))
