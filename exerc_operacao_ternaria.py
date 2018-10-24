import random
secret = random.randint(1, 100)

while True:
	chute = int(input('Chute: '))

	if chute == secret:
		print('Acertou, %d, Miseravi! ' %secret)
		break
	else:
		print ('Alto' if chute > secret else 'Baixo') #Operação Ternária

print ('Fim de Jogo!')