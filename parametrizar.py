import argparse
import csv
import pdb
import random
from collections import defaultdict

# inicializacion variables globales
secciones = defaultdict(list)
parametros = {}
vars_instanciadas = {}

class Parametro:
	def __init__(self, nombre, minimo, maximo, decimales):
		self.nombre = nombre
		self.minimo = minimo if minimo else 0
		self.maximo = maximo if maximo else 100
		self.decimales = decimales if decimales else 2
		self.evaluacion = 0

	def instanciar(self):
		# cuidado que asi como esta nunca devuelve maximo
		numero_random = random.uniform(self.minimo, self.maximo)
		# truncate
		self.evaluacion = round(numero_random, self.decimales)
		return self.evaluacion

	def __str__(self):
		self.instanciar()
		return self.nombre + ':' + str(self.decimales) + ':' +str(self.evaluacion)

def abrir_csv(nombre_archivo):
	return csv.reader(open(nombre_archivo), delimiter='\t')

# def param(nombre, min=0, max=100, dec=1):


# def extraer_variables(cuerpo, variables):
# 	while True:
# 		comienzo = cuerpo.find('param(')
# 		if comienzo >= 0:
# 			break
# 		fin = cuerpo[comienzo:].find(')')
# 		variables = call(cuerpo[comienzo:fin])
# 		cuerpo = cuerpo[:comienzo -1] + '{{' + nombre_variable + '}}' + cuerpo[fin + 1:]

# def computar_formulas():

def pregunta(cuerpo):
	if len(cuerpo) != 1:
		raise Exception('Pregunta mal especificada.')
	secciones['pregunta'] = cuerpo[0]

def respuesta(cuerpo):
	if len(cuerpo) != 1:
		raise Exception('Respuesta mal especificada.')
	secciones['respuesta'] = cuerpo[0]

def distractor(cuerpo):
	if len(cuerpo) != 1:
		raise Exception('Dstractor mal especificado.')
	secciones['distractores'] += [cuerpo[0]]

def parametro(cuerpo):
	if len(cuerpo) <= 1:
		raise Exception('parametro mal especificado.')
	nombre = cuerpo[0]
	minimo = None
	maximo = None
	decimales = None
	for i in range(1, len(cuerpo) // 2 + 1):
		etiqueta = cuerpo[i * 2 - 1].lower()
		valor = int(cuerpo[i * 2])
		if etiqueta == 'minimo':
			minimo = valor
		elif etiqueta == 'maximo':
			maximo = valor
		elif etiqueta == 'decimales':
			decimales = valor
		else:
			raise Exception('Parametro desconocido: ' + label)
	parametros['nombre'] = Parametro(nombre, minimo, maximo, decimales)


def computar(cuerpo):
	print('computar')


def main(in_nombre_archivo):
	print(in_nombre_archivo)
	secciones = {}
	variables = {}
	vars_instanciadas = {}

	lector_csv = abrir_csv(in_nombre_archivo)
	for linea_seccion in lector_csv:
		if len(linea_seccion) > 0:
			# pdb.set_trace()
			tag = linea_seccion[0].lower()
			cuerpo = linea_seccion[1:]
			if tag == 'pregunta':
				pregunta(cuerpo)
			elif tag == 'respuesta':
				respuesta(cuerpo)
			elif tag == 'distractor':
				distractor(cuerpo)
			elif tag == 'parametro':
				parametro(cuerpo)
			elif tag == 'computar':
				computar(cuerpo)

		for k in parametros.values():
			print(k)

		# 	if tag == 'pregunta':
		# 		cuerpo = extraer_variables(cuerpo, variables)
		# 		cuerpo = computar_formulas(cuerpo, variables)
		# 		seciones[tag] = cuerpo
		# 	elif tag == 'respuesta': 
		# 		# leer pregunta, leer variables
		# 		# sustituir valores, extraer variables
		# 	elif tag == 'distractora': 

if __name__ == "__main__": 
	parser = argparse.ArgumentParser(description="Procesa ejercicios parametrizados.")
	parser.add_argument('nombre_archivo', 
						help='Nombre del archivo parametriazable de entrada.')
	args = parser.parse_args()
	
	main(args.nombre_archivo)


