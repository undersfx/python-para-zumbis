def reverso(dados):
	"""Busca por nome de host"""
	
	from subprocess import check_output
	import re

	#Gera lista de IPs bloqueados

	for x in range(len(dados)):
		try:
			#Roda o commando 'Host' com o IP da lista no shell
			t = check_output(['host ' + dados[x]], shell=True)

			#Pega a porção do reverso do resultado
			regex = re.search('pm.+\.', str(t.split()[4]))
			t = regex.group()

			#Contatena o valor do Host ao IP
			dados[x] = str(dados[x]) + ';' + str(t)
		except:
			#IPs sem reverso configurado retornam non-zero para o shell
			dados[x] = str(dados[x]) + ';Null'
	return dados

if __name__ == '__main__':
	r = input('IP ou lista de IPs (separados por ,):')
	r = r.split(',')
	print('\r\n'.join(reverso(r)))