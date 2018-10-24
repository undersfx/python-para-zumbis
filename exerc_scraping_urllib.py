import urllib.request

# URL do site para Scraping (Exemplo)
url = 'http://www.afterfest.com.br/guten-bier-lancamento-temporada-cafe-de-la-musique/'


# Importa o html
html = urllib.request.urlopen(url).read().decode('utf-8')

# Padrão de imagens a ser procurado
padrao = 'href="http://www.afterfest.com.br/wp-content/uploads/2017/05/'

# # Escreve HTML em arquivo 
# arquivo = open('html.txt', 'w')
# arquivo.write(html)
# arquivo.close()

i = 0
k = 1

# Loop através de todos links atualizando com o nome da imagem e escrevendo os arquivos
while i != -1:
	# Encontra o nome dos arquivos
	i = html.find(padrao) + len(padrao)
	f = html.find('"', i)
	print(k, 'Arquivo encontrado:', html[i:f])

	# Escreve arquivo encontrado
	urlfoto = 'http://www.afterfest.com.br/wp-content/uploads/2017/05/' + html[i:f]
	foto = urllib.request.urlopen(urlfoto).read()
	arquivo = open(html[i:f], 'wb')
	arquivo.write(foto)
	arquivo.close()
	print(k, 'Arquivo Salvo. \n')

	# Atualiza o html para a pesquisa do proximo nome
	html = html[f:]

	k += 1
