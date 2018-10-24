'''
    Calcular o enesimo número da sequencia de Fibonacci
    Sendo N inputado pelo usuário
'''

n = int(input("Número Interiro: "))

atual=0
d1=0
d2=0
i = 1

while i <= n:
    if i == 1:
        atual = 0
    elif i == 2:
        atual = 1
    else:
        atual = d1 + d2        
    print("F(%d) = %d" %(i, atual))
    #d2 = d1
    #d1 = atual
    #Atribução Multipla:
    d2, d1 = d1, atual
    i = i + 1
    
    
    
