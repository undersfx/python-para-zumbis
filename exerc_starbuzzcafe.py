preco = 5

while preco >= 4.74:
    import urllib.request

    #Abreo request no objeto pagina
    pagina = urllib.request.urlopen('http://beans.itcarlow.ie/prices-loyalty.html')

    #Decodifica o conteudo da pagina para a variavel texto
    texto = pagina.read().decode('utf-8')

    #Localiza a posicao do preco
    onde = texto.find('>$')

    #Armazena o preco encontrado
    preco = float(texto[onde+2:onde+6])

    import time

    #Imprime preço caso abaixo do esperado ou aciona sleep de 1 minuto e libera novo loop do while
    if preco >= 4.74:
            print('Preço atual: %5.2f, aguardadno baixa.' %preco)
            time.sleep(60)

print('Comprar! Preço abaixo do esperado: %5.2f.' %preco)