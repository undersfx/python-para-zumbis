'''
    Ler uma paralha e verificar se a mesma é palíndrome.

    Wikipedia: Um palíndromo é uma palavra, frase ou qualquer outra sequência
    de unidades que tenha a propriedade de poder ser lida tanto da direita para
    a esquerda como da esquerda para a direita.
'''

palavra = str(input("Texto: "))

##[::-1] Fatia a string do último ao primeiro cartere ("passo" -1)
if palavra == palavra[::-1]:
    print(palavra, "é palíndromo de ", palavra[::-1])
else:
    print(palavra, "não é palíndromo de ", palavra[::-1])
