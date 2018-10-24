# Função que valida o IP
def ip_ok(ip):
	ip = ip.split('.')
	for byte in ip:
		if int(byte) > 255
			return False
	return True

# Abre os arquivos a serem escritos
arq = open('ips.txt')
validos = open('validos.txt', 'w')
invalidos = open('invalidos.txt', 'w')

# Escreve linha por linha com base no resultado da função
for linha in arq.readlines():
	if ip_ok(linha):
		validos.write(linha)
	else:
		invalidos.write(linha)

# Fechar arquivos escritos
arq.close()
validos.close()
invalidos.close()