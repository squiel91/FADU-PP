import argparse
import csv
import pdb
from ejercicio import Ejercicio

secciones = defaultdict(list)
parametros = {}
formulas = {}

def abrir_csv(nombre_archivo):
	return csv.reader(open(nombre_archivo), delimiter='\t')

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
		raise Exception('Distractor mal especificado.')
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
	parametros[nombre] = Parametro(nombre, minimo, maximo, decimales)

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
	formulas[nombre] = Formula(nombre, computo, decimales)


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


	vars_instanciadas = {}
	for nombre, param in parametros.items():
		vars_instanciadas[nombre] = param.instanciar()

	vars_instanciadas_backup = vars_instanciadas.copy()

	form_instanciadas = {}
	for nombre, form in formulas.items():
		form_instanciadas[nombre] = form.instanciar(vars_instanciadas)

	vars_instanciadas = vars_instanciadas_backup

	variables = {**vars_instanciadas, **form_instanciadas}

	print('Pregunta:')
	print(sustituir_variables(secciones['pregunta'], variables))

	print('Respuesta:')
	print(sustituir_variables(secciones['respuesta'], variables))

	print('Distractores:')
	for ditractor in secciones['distractores']:
		print(sustituir_variables(ditractor, variables))

	exportar_pregunta_latex(
		out_nombre_archivo, 
		sustituir_variables(secciones['pregunta'], variables), 
		sustituir_variables(secciones['respuesta'], variables), 
		[sustituir_variables(d, variables) for d in secciones['distractores']]
	)
	exportar_pregunta_xml_eva(
		out_nombre_archivo, 
		sustituir_variables(secciones['pregunta'], variables), 
		sustituir_variables(secciones['respuesta'], variables), 
		[sustituir_variables(d, variables) for d in secciones['distractores']]
	)


if __name__ == "__main__": 
	parser = argparse.ArgumentParser(description="Procesa ejercicios parametrizados.")
	parser.add_argument('nombre_archivo_entrada', 
						help='Nombre del archivo parametriazable de entrada.')
	parser.add_argument('nombre_archivo_salida', 
						help='Nombre del archivo de salida (una instancia).')
	args = parser.parse_args()
	
	main(args.nombre_archivo_entrada, args.nombre_archivo_salida)


