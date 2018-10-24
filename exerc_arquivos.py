#Abrir arquivo mensagem.txt
with open('mensagem.txt') as f:
	texto = f.read()

#Trocar vogais por *
for x in range(len(texto)):
	if texto[x:x+1] in 'aeiou':
		texto = texto[:x] + '*' + texto[x+1:]

#gravar arquivo cripto.txt com
cripto = open('cripto.txt', 'w')
cripto.write(texto)
cripto.close()