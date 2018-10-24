'''
    Desafio Lista V Google Developer Day 2010, Questão E;
    Dado uma lista de telefones (não tenho a lista, por isso o input), processe quais deles são validos de acordo com as seguintes regras:
    1 - O número de telefone não pode ter dois digitos consegutivos identicos;
    2 - A soma dos dígitos tem de ser par;
    3 - O último digito não pode ser igual ao primeiro;
'''

#tel = int(input('telefone: '))

tel = '''213752
236043
254711
275001
292559
310638
327249
237350'''

tel = tel.split('\n')

for k in range(len(tel)):
        
        regra1 = True
        regra2 = True
        regra3 = True

        array_tel = list(str(tel[k]))

        #Validando regra 1;
        x = 0
        while x < len(array_tel) - 1:
            if array_tel[x] == array_tel[x+1]:
                regra1 = False
            x +=1

        #Validando regra 2;
        soma = 0
        for i in range(len(array_tel)):
            soma += int(array_tel[i])

        if soma % 2 != 0:
            regra2 = False


        #Validando regra 3;
        if array_tel[0] == array_tel[5]:
            regra3 = False


        #Compilando resposta e mostrando número válido;
        if regra1 and regra2 and regra3:
            print(tel[k])
