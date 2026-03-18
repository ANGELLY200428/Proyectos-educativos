class Veterinaria:

	def __init__(self):
		self.clientes = []
		self.mascotas = []

	# ---------- CLIENTES ----------

	def buscar_cliente(self, codigo):
		for i in range(len(self.clientes)):
			if self.clientes[i].codigo == codigo:
				return i
		return -1

	def adicionar_cliente(self, cliente):
		if self.buscar_cliente(cliente.codigo) == -1:
			self.clientes.append(cliente)
			return True
		return False

	def modificar_cliente(self, codigo):
		pos = self.buscar_cliente(codigo)
		if pos != -1:
			print("============================")
			print("=== MODIFICACIÓN CLIENTE ===")
			print("============================")
			print("1. Modificar nombre")
			print("2. Modificar teléfono")
			op = int(input("Opción: "))

			if op == 1:
				self.clientes[pos].nombre = input("Nuevo nombre: ")
				while self.clientes[pos].nombre == "":
					self.clientes[pos].nombre = input("Nuevo nombre: ")

			elif op == 2:
				try:
					self.clientes[pos].telefono = int(input("Nuevo teléfono: "))
				except:
					print("Error: el teléfono solo debe contener números")
					input()
					return False
			return True
		return False



	def eliminar_cliente(self, codigo):
		pos = self.buscar_cliente(codigo)
		if pos != -1:

			for mascota in self.mascotas[:]: #crea una copia de la lista para evitar errores
				if mascota.codigo_dueno == codigo:
					self.mascotas.remove(mascota)

			del self.clientes[pos]
			return True
		return False



	# ---------- MASCOTAS ----------

	def buscar_mascota(self, codigo):
		for i in range(len(self.mascotas)):
			if self.mascotas[i].codigo == codigo:
				return i
		return -1

	def adicionar_mascota(self, mascota):
		if self.buscar_cliente(mascota.codigo_dueno) == -1:
			return "NO_DUENO"

		if self.buscar_mascota(mascota.codigo) == -1:
			self.mascotas.append(mascota)
			return "OK"

		return "EXISTE"

	def modificar_mascota(self, codigo):
		pos = self.buscar_mascota(codigo)
		if pos != -1:
			print("============================")
			print("=== MODIFICACIÓN MASCOTA ===")
			print("============================")
			print("1. Modificar nombre")
			print("2. Modificar especie")
			print("3. Modificar edad")
			op = int(input("Opción: "))

			if op == 1:
				self.mascotas[pos].nombre = input("Nuevo nombre: ")
				while self.mascotas[pos].nombre == "":
					self.mascotas[pos].nombre = input("Nuevo nombre: ")

			elif op == 2:
				self.mascotas[pos].especie = input("Nueva especie: ")
				while self.mascotas[pos].especie == "":
					self.mascotas[pos].especie = input("Nueva especie: ")

			elif op == 3:
				try:
					self.mascotas[pos].edad = int(input("Nueva edad: "))
				except:
					print("Error: La edad solo deben ser números")
					input()
					return False
			return True
		return False

	def eliminar_mascota(self, codigo):
		pos = self.buscar_mascota(codigo)
		if pos != -1:
			del self.mascotas[pos]
			return True
		return False