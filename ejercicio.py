import random

class Ejercicio:
	def __init__(self, titulo, problema, respuesta, distractoras):
		self.titulo = None
		self.problem = None
		self.respuesta = None
		self.distractores = []

		self.parametros = {}
		self.formulas = {}

	def set_titulo(self, titulo):
		self.titulo = titulo

	def set_problema(self, problema):
		self.problema = problema

	def set_respuesta(self, respuesta):
		self.respuesta = respuesta

	def agregar_distractor(self, distractor):
		self.distractores.append(distractor)

	def agregar_parametro(self, nombre, minimo=0, maximo=100, decimales=2):
		parametro = Parametro(nombre, minimo, maximo, decimales)
		self.parametros[nombre] = parametro

	def agregar_formula(self, nombre, computo, decimales=2): 
		formula = Formula(nombre, computo, decimales)
		self.formulas[nombre] = formula


	class Parametro:
		def __init__(self, nombre, minimo, maximo, decimales):
			self.nombre = nombre
			self.minimo = minimo if minimo else 0
			self.maximo = maximo if maximo else 100
			self.decimales = decimales if decimales else 2
			self.evaluacion = None

		def instanciar(self):
			# cuidado que asi como esta nunca devuelve maximo
			numero_random = random.uniform(self.minimo, self.maximo)
			# truncar en vez
			self.evaluacion = round(numero_random, self.decimales)
			return self.evaluacion

		def __str__(self):
			self.instanciar()
			return self.nombre + ':' + str(self.decimales) + ':' +str(self.evaluacion)

	class Formula:
		def __init__(self, nombre, computo, decimales):
			self.nombre = nombre
			self.computo = computo
			self.decimales = decimales if decimales else 2
			self.evaluacion = 0

		def instanciar(self, vars_instanciadas):
			self.evaluacion = round(eval(self.computo, vars_instanciadas), self.decimales)
			return self.evaluacion

		def __str__(self):
			self.instanciar()
			return self.nombre + ':' + str(self.decimales) + ':' +str(self.evaluacion)

	def exportar_latex(self, nombre_exportado):
		archivo = open(nombre_exportado + '.tex', 'w')
		archivo.write(pregunta + '\n\n')
		archivo.write(respuesta + '\n')
		for distractor in distractoras:
			archivo.write(distractor + '\n')
		archivo.close()

def sustituir_variables(texto, variables):
	semi_sustituido = texto
	for nombre, valor in variables.items():
		semi_sustituido = semi_sustituido.replace('{' + nombre + '}', str(valor))
	return semi_sustituido
	# def exportar_xml_eva(self, nombre_exportado):
	# 	archivo = open(nombre_exportado + '.xml', 'w')
	# 	archivo.write(pregunta + '\n\n')
	# 	archivo.write(respuesta + '\n')
	# 	for distractor in distractoras:
	# 		archivo.write(distractor + '\n')
	# 	archivo.close()