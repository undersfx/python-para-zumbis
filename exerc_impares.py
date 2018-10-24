'''
    Imprimir de números pares de 0 a X (sendo X inputado pelo usuário
'''

x = int(input("Número de Loops: "))

y = 0

while y <= x:
    #if y % 2 != 0: #ímpar
    if y % 2 == 0: #par
        print (y)        
    y = y + 1
