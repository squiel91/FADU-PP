class Formula:
	def __init__(self, nombre, computo, decimales=2):
		self.nombre = nombre
		self.computo = computo
		self.decimales = decimales
		
	def instanciar(self, vars_instanciadas):
		self.evaluacion = round(eval(self.computo, vars_instanciadas), self.decimales)
		return self.evaluacion

	def __str__(self):
		self.instanciar()
		return self.nombre + ':' + str(self.decimales) + ':' +str(self.evaluacion)