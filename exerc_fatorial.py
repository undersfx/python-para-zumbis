'''
    Fatorial de N
'''

n = int(input("Número Interiro: "))
x = n
fat = 1

while n >= 1:
    fat = fat * n
    n = n - 1
print("Fat(%d)=%d" %(x, fat))
