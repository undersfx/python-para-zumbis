'''
    leia uma palavra (em minusculas e sem acentos) e troque todas as vogais por *
'''

palavra = input("Palavra: ")
i = 0

#for x in range(0, len(palavra)):
#    if palavra[x:x+1] in 'aeiou':
#        palavra = palavra[:x] + '*' + palavra[x+1:]
#print(palavra)

nova = ''
while i < len(palavra):
    if palavra[i] in 'aeiou':
        nova += '*'
    else:
        nova += palavra[i]
    i += 1
        
print(nova)
