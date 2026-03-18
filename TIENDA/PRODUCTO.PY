class Producto:

	def __init__(self, codigo, nombre, cantidad, costo):

		self.codigo = codigo
		self.nombre = nombre
		self.cantidad = cantidad
		self.costo = costo
		self.actualizar_valores()

	def actualizar_valores(self):
		self.total = self.cantidad * self.costo
		self.valor_unitario = self.costo * 1.3