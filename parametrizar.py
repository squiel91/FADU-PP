import argparse
import csv
from ejercicio import Ejercicio
from prueba import Prueba

def abrir_csv(nombre_archivo):
	return csv.reader(open(nombre_archivo), delimiter='\t')

def problema(cuerpo, ejercicio):
	if len(cuerpo) != 1:
		raise Exception('Problema mal especificado.')
	ejercicio.set_problema(cuerpo[0])

def respuesta(cuerpo, ejercicio):
	if len(cuerpo) != 1:
		raise Exception('Respuesta mal especificada.')
	ejercicio.set_respuesta(cuerpo[0])

def distractor(cuerpo, ejercicio):
	if len(cuerpo) != 1:
		raise Exception('Distractor mal especificado.')
	ejercicio.agregar_distractor(cuerpo[0])

def parametro(cuerpo, ejercicio):
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
	ejercicio.agregar_parametro(nombre, minimo, maximo, decimales)

def computar(cuerpo, ejercicio):
	if len(cuerpo) <= 1:
		raise Exception('computar mal especificado.')
	nombre = cuerpo[0]
	computo = cuerpo[1]
	decimales = None
	if len(cuerpo) > 2:
		if cuerpo[2].lower() == 'decimales':
			decimales = int(cuerpo[3])
		else:
			raise Exception('Parametro desconocido')
	ejercicio.agregar_formula(nombre, computo, decimales)


def main(titulo, nombres_ejercicios, out_nombre_archivo, numero_instancias=0, texto=False, latex=False, eva=False):
	prueba = Prueba(titulo, numero_instancias)
	for nombre_ejercicio in nombres_ejercicios:
		ejercicio = Ejercicio()
		lector_csv = abrir_csv(nombre_ejercicio)
		for linea_seccion in lector_csv:
			if len(linea_seccion) > 0:
				tag = linea_seccion[0].lower()
				cuerpo = linea_seccion[1:]
				if tag == 'pregunta':
					problema(cuerpo, ejercicio)
				elif tag == 'respuesta':
					respuesta(cuerpo, ejercicio)
				elif tag == 'distractor':
					distractor(cuerpo, ejercicio)
				elif tag == 'parametro':
					parametro(cuerpo, ejercicio)
				elif tag == 'computar':
					computar(cuerpo, ejercicio)
				elif tag == 'comentario':
					pass
				else:
					raise Exception('No se reconoce el tag ' + tag)
		prueba.agregar_ejercicio(ejercicio)
	if texto:
		prueba.generar('texto')
	if latex:
		prueba.generar('latex')
	if eva:
		prueba.generar('eva')



if __name__ == "__main__": 
	parser = argparse.ArgumentParser(description="Crea prueba a partir de los ejercicios parametrizados")
	parser.add_argument('titulo', help='Titulo de la prueba')
	parser.add_argument('ejercicios_parametrizados', nargs='+', 
						help='Lista de ejercicios parametrizados.')
	parser.add_argument('--cantidad', type=int, help='Cantidad de pruebas')
	parser.add_argument('--texto', action="store_true", help='Exportación a texto plano')
	parser.add_argument('--pdf', action="store_true", help='Exportacion a PDF')
	parser.add_argument('--eva', action="store_true", help='Para importar a entorno EVA')
	parser.add_argument('--encabezado', help='Encabezado en formato LaTeX')
	args = parser.parse_args()
	
	main(
		args.titulo, 
		args.ejercicios_parametrizados, 
		args.titulo, 
		numero_instancias=args.cantidad, 
		texto=args.texto, 
		eva=args.eva, 
		latex=args.pdf)


