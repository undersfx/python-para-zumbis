'''
    Ler tamanho de área de calcular minimo interiro de latas para pinta-la;
    Printar o valor total do custo considerando que cada lata;
    Tem 18 litros, custa 80 reais e cada litro de tinta pinta 3 metros quadrados.
'''

metros = int(input("M² de área a ser pintada: "))

if metros % 54 != 0:
    latas = int(metros / (18 * 3)) + 1
    #Se o resto da divisão não for zero
    #É preciso uma lata adicional para terminal o perímetro
else:
    latas = metros / (18 * 3)

preco = int(latas) * 80

print("Serão necessárias %d latas, totalizando R$%5.2f" %(latas, preco))
