'''
    Comentário de várias linhas;
    Programa para ler três números e mostra o maior usando ELIF
'''
print('Maior Número')

a = int(input('Primeiro: '))
b = int(input('Segundo: '))
c = int(input('Terceiro: '))

#if a >= b and a >= c:
#    print(a)
#else:
#    if b >= a and b >= c:
#        print (b)
#    else:
#        if c >= a and c >= b:
#            print (c)

if a >= b and a >= c:
    print (a)
elif b >= c:
    print (b)
else:
    print (c)
