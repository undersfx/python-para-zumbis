class Televisao:
	def __init__(self):
		self.ligada = False
		self.canal = 2
	def canal_mais(self):
		self.canal += 1
	def canal_menos(self):
		self.canal -= 1