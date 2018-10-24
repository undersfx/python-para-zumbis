'''
    Imprimir o resultado de todas as tabuadas de 1 a 10
'''

tab = 1

while tab <= 10:
    n = 1
    print ("Tabuada do %d" %tab)
    while n <= 10:
        print ("%d x %d = %d" %(tab, n, tab * n))
        n = n + 1
    tab = tab + 1
        
