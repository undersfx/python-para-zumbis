'''
    Calcular a soma de inteiros até ser digitado 0
'''

soma = 0

while True:
    x = int(input("Digite o número para continuar a soma (0 para sair): "))
    if x == 0:
        break
    soma = soma + x
print ("Soma= %d" %soma)
