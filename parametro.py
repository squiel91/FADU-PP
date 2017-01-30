import random

class Parametro:
	def __init__(self, nombre, minimo=0, maximo=100, decimales=2):
		self.nombre = nombre
		self.minimo = minimo
		self.maximo = maximo
		self.decimales = decimales

	def instanciar(self):
		numero_random = random.uniform(self.minimo, self.maximo) # cuidado que asi como esta nunca devuelve maximo
		self.evaluacion = round(numero_random, self.decimales) # truncar en vez
		return self.evaluacion

	def __str__(self):
		self.instanciar()
		return self.nombre + ':' + str(self.decimales) + ':' +str(self.evaluacion)