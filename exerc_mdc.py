'''
    Calcular MDC (Maior divisor comum entre dois números interiros
'''

a = int(input("a= "))
b = int(input("b= "))

resto = 0

while a % b != 0:
    a, b = b, a % b
print("mdc=%d" %b)
