class Carrera:
	def __init__(self, tipo, nombreC, n_alumnos):
		self.tipo = tipo
		self.nombreC = nombreC
		self.alumnos = n_alumnos

	def establecer_tipo(self, n):
		self.tipo = n

	def establecer_nombreC(self, n):
		self.nombreC = n

	def establecer_alumnos(self, n):
		self.alumnos = n

	def obtener_tipo(self):
		return self.tipo

	def obtener_nombreC(self):
		return self.nombreC

	def obtener_alumnos(self):
		return self.alumnos

	def __str__(self):
		return "Tipo de Carrera: %s, Nombre de Carrera: %s, Número de alumnos: %d\n" \
			% (self.tipo, self.nombreC, self.alumnos)