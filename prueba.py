import re

# una prueba es un encabezado y una coleccion de ejercicios

class Prueba:
	def __init__(self, titulo, numero_instancias, encabezado=None):
		self.nombre = re.sub('[\W]', '', titulo.lower().replace(' ', '_'))
		self.titulo = titulo
		self.encabezado = encabezado
		self.numero_instancias = numero_instancias
		self.ejercicios = []

		self.instancias = []

	def agregar_ejercicio(self, ejercicio):
		self.ejercicio.append(ejercicio)

	def generar(self, tipo_exportacion):
		# encabezado

		for id in range(1, numero_instancias + 1):
			self.instancias.append(Instancia(id, self.ejercicios))
		
		if tipo_exportacion == 'latex':
			directorio = self.nombre
			os.mkdir(directorio, 'w')
			planilla_respuestas = []
			for prueba_individual in self.instancias:
				prueba_individual.exportar_latex(ruta=directorio)
				planilla_respuestas.append(prueba_individual.respuestas)
				generar_archivo_respuestas(planilla_respuestas)
		elif tipo_exportacion == 'eva':
			pass
		else:
			raise Exception(tipo_exportacion + ' no se reconoce como un tipo de exportacion.')

	class Instancia:
		def __init__(self, id, ejercicios):
			self.id = id
			self.ejercicios = ejercicios.instanciar()
			random.shuffle(self.ejercicios)
			self.respuestas = []
			for ejercicio in self.ejercicios:
				self.respuestas.append(ejercicio.posicion_respuesta)

		def exportar_latex(ruta=''): # deberia incluir el encabezado aca
			archivo = open(os.path.join(ruta, nombre_exportado + '.tex'), 'w')
			archivo.write(self.ejercicio.problema + '\n\n')
			archivo.write(self.ejercicio.respuesta + '\n')
			for distractor in instancia.distractoras:
				archivo.write(distractor + '\n')
			archivo.close()

		def exportar_xml_eva():
			pass
