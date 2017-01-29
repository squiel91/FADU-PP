import random

def sustituir_variables(texto, variables):
	semi_sustituido = texto
	for nombre, valor in variables.items():
		semi_sustituido = semi_sustituido.replace('{' + nombre + '}', str(valor))
	return semi_sustituido

class Ejercicio:

	def __init__(self):
		self.titulo = None
		self.problema = None
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

	def instanciar(self):
		nueva_instancia = Instancia(
				self.titulo, 
				self.problema, 
				self.respuesta, 
				self.distractores, 
				self.parametros, 
				self.formulas
			)

		return nueva_instancia

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

	class Instancia:
		def __init__(self, titulo, problema, respuesta, distractores, parametros, formulas):
			vars_instanciadas = {}
			for nombre, param in self.parametros.items():
				vars_instanciadas[nombre] = param.instanciar()

			vars_instanciadas_backup = vars_instanciadas.copy()

			form_instanciadas = {}
			for nombre, form in self.formulas.items():
				form_instanciadas[nombre] = form.instanciar(vars_instanciadas)

			vars_instanciadas = vars_instanciadas_backup

			variables = {**vars_instanciadas, **form_instanciadas}

			self.titulo = titulo
			self.problema = sustituir_variables(problema, variables)
			self.respuesta = sustituir_variables(secciones['respuesta'], variables)
			self.distractores = [sustituir_variables(d, variables) for d in secciones['distractores']]

			random.shuffle(self.distractores)

			self.posicion_respuesta = random.randint(0,len(self.distractores))

			self.opciones = self.distractores[:posicion_respuesta] + [self.respuesta] + self.distractores[posicion_respuesta:]

		def exportar_latex(self, nombre_exportado):
			archivo = open(nombre_exportado + '.tex', 'w')
			instancia_ejercicio = problema.instanciar()
			archivo.write(instancia.pregunta + '\n\n')
			archivo.write(instancia.respuesta + '\n')
			for i in range(self.opciones):
				archivo.write('{}) {}\n'.format(chr(i), self.opciones[i]))
			archivo.close()
	
		def exportar_xml_eva(self, nombre_exportado):
			pass