'''
    Ler valor de data (formato dd/mm/aaaa) e imprimir nome do mês.
'''

dia, mes, ano = input("Data: ").split('/')

meses = [
    'Janeiro',
    'Fevereiro',
    'Março',
    'Abril',
    'Maio',
    'Junho',
    'Julho',
    'Agosto',
    'Setembro',
    'Outubro',
    'Novembro',
    'Dezembro'
    ]

print('%s de %s de %s' %(dia, meses[int(mes)-1], ano))
