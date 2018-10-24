#Importa lib de string para utilizar as pontuações
import string

word = 'alice'

#Abre arquivo alice.txt em alice
with open('alice.txt', encoding="utf8") as alice:
	
	#carrega o texto de alice em uma variavel.
	texto = alice.read()

	#Converte tudo para minusculo
	texto = texto.lower()

	#Substitui todos os caracteres de pontuação por ' '
	for x in string.punctuation:
		texto = texto.replace(x, ' ')
	
	#Quebra o texto em uma list com base no espaço em branco
	texto = texto.split()

	#Cria um dicionario e popula o mesmo com o valor de palavras adicionando 1 caso já exista	
	d = {}

	for p in texto:
		if p not in d:
			d[p] = 1
		else:
			d[p] += 1

#Mostra o total somado correspondente ao indice 'alice'
print('A palavra "'+ word + '" aparece %s vezes.' %d[word])