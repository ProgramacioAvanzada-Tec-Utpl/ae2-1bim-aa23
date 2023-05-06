class Universidad:
	def __init__(self, institucion, n_tutores, n_facultades):
		self.nombre = institucion
		self.tutores = n_tutores
		self.facultades = n_facultades

	def establecer_nombre(self, n):
		self.nombre = n

	def establecer_tutores(self, n):
		self.tutores = n

	def establecer_facultades(self, n):
		self.facultades = n

	def obtener_nombre(self):
		return self.nombre

	def obtener_tutores(self):
		return self.tutores

	def obtener_facultades(self):
		return self.facultades

	def __str__(self):
		return "Institución Universitaria: %s, Número de tutores: %d, Número de facultades: %d\n" \
			% (self.nombre, self.tutores, self.facultades)
