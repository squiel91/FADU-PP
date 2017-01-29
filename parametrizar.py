import argparse
import csv
import pdb
from ejercicio import Ejercicio

ejercicio = Ejercicio()

def abrir_csv(nombre_archivo):
	return csv.reader(open(nombre_archivo), delimiter='\t')

def problema(cuerpo):
	if len(cuerpo) != 1:
		raise Exception('Pregunta mal especificada.')
	ejercicio.set_problema(cuerpo[0])

def respuesta(cuerpo):
	if len(cuerpo) != 1:
		raise Exception('Respuesta mal especificada.')
	ejercicio.set_respuesta(cuerpo[0])

def distractor(cuerpo):
	if len(cuerpo) != 1:
		raise Exception('Distractor mal especificado.')
	ejercicio.add_distractor(cuerpo[0])

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
	ejercicio.add_parametro(nombre, minimo, maximo, decimales)

def computar(cuerpo):
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
	ejercicio.add_formula(nombre, computo, decimales)


def main(in_nombre_archivo, out_nombre_archivo):
	lector_csv = abrir_csv(in_nombre_archivo)
	for linea_seccion in lector_csv:
		if len(linea_seccion) > 0:
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
	ejercicio.exportar


if __name__ == "__main__": 
	parser = argparse.ArgumentParser(description="Crea prueba a partir de los ejercicios parametrizados")
	parser.add_argument('titulo', help='Titulo de la prueba')
	parser.add_argument('ejercicios_parametrizados', nargs='+', 
						help='Lista de ejercicios parametrizados.')
	parser.add_argument('--cantidad', type=int, help='Cantidad de pruebas')
	parser.add_argument('--pdf', action="store_true", help='Exportacion a PDF')
	parser.add_argument('--eva', action="store_true", help='Para importar a entorno EVA')
	parser.add_argument('--encabezado', help='Encabezado en formato LaTeX')
	args = parser.parse_args()
	
	main(args.ejercicios_parametrizados, args.titulo)


