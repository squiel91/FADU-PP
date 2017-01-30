from instancia_ejercicio import InstanciaEjercicio

from formula import Formula
from parametro import Parametro

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
		self.parametros[nombre] = Parametro(nombre, minimo, maximo, decimales)

	def agregar_formula(self, nombre, computo, decimales=2): 
		self.formulas[nombre] = Formula(nombre, computo, decimales)

	def instanciar(self):
		return InstanciaEjercicio(
				self.titulo, 
				self.problema, 
				self.respuesta, 
				self.distractores, 
				self.parametros, 
				self.formulas
			)