#List Comprehension facilita a criação de objetos tipo lista

#Sem List Comprehension:
# new_list = []
# for i in old_list:
#     if filter(i):
#         new_list.append(expressions(i))

#Com List Comprehension:
#new_list = [expression(i) for i in old_list if filter(i)]

#Exemplos:

print('Exemplo 1')
x = [i for i in range(10)]
print('x = [i for i in range(10)] gera x =', x,'\n')

print('Exemplo 2')
s = [x**2 for x in range(1,11)]
print('s = [x**2 for x in range(1,11)] gera s =', s,'   \n')

print('Exemplo 3')
k = [x+y for x in [10,30,50] for y in [20,40,60]]
print('k = [x+y for x in [10,30,50] for y in [20,40,60]] gera k =', k,'   \n')