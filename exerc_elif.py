m = int(input("Minutos Gastos: "))

#if m < 200: 
#    v = m * 0.2 
#else:
#    if m <= 400:
#        v = m * 0.18 
#    else:
#        if m <= 800:
#        	v = m * 0.15
#        else:
#        	v = m * 0.08

#Usando elif:

if m < 200: 
    v = 0.2 
elif m <= 400:
    v = 0.18 
elif m <= 800:
    v = 0.15
else:
    v = 0.08


#Print sem identação para responder independente do resultado dos if's        
print ("Valor da conta: R$ %5.2f" %(m * v))
