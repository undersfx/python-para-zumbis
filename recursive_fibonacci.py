#Funciona, porém, vemos que varias chamadas feitas são repeditas
def fibsimples(x):
	print('fib(%d)' %x)
	if x <= 2:
		return 1
	return fibsimples(x - 1) + fibsimples(x - 2)

#Para solucionar, podemos adicionar um dicionário de "cache".
fib_cache = {}

def fibcache(x):
	print('fib(%d)' %x)
	if x <= 2:
		return 1
	else:
		if x not in fib_cache:
			fib_cache[x] = fibcache(x - 1) + fibcache(x - 2)
		return fib_cache[x]

#Functools proporciona ferramenta para facilitar a criação de Cache
from functools import lru_cache

@lru_cache (maxsize=None)
def fib(x):
	print('fib(%d)' %x)
	if x <= 2:
		return 1
	return fib(x - 1) + fib(x - 2)