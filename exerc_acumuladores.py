'''
    Soma de Dez números inputados usando contador e acumulador
'''

n = 1
soma = 0

while n <= 10:
    x = int(input("Digite o %d º número: " %n))
    soma = soma + x
    n = n + 1
print("Soma: %d" %soma)
