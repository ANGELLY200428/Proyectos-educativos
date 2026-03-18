from vendedor import Vendedor
from datetime import date, datetime


class Tienda():

	def __init__(self):
		self.vendedores = []
		self.clientes = []
		self.productos = []
		self.ventas = []
		

	def buscar_vendedor(self, codigo):
		for i in range(len(self.vendedores)):
			if codigo == self.vendedores[i].codigo:
				return i
		return -1

	def adicionar_vendedor(self, vendedor):
		if self.buscar_vendedor(vendedor.codigo) == -1:
			self.vendedores.append(vendedor)
			return True
		return False

	def modificar_vendedor(self, codigo_vendedor):
		pos_vendedor = self.buscar_vendedor(codigo_vendedor)
		if pos_vendedor != -1:
			if self.vendedores[pos_vendedor].codigo == codigo_vendedor:
				try:
					print("==========================================")
					print("Seleccione la opción que desea modificar: ")
					print("1. Modificar el nombre")
					print("2. Modificar el teléfono")
					print("3. Modificar el domicilio")
					print("4. Modificar el edad")
				
					opcion = int(input("Digite la opción que desea modificar: "))
					print("======================================")

					if opcion == 1:
						nuevo_nombre = input("Digite el nuevo nombre del vendedor: ")
						self.vendedores[pos_vendedor].nombre = nuevo_nombre
						return True

					elif opcion == 2:
						nuevo_telefono = int(input("Digite el nuevo teléfono del vendedor: "))
						self.vendedores[pos_vendedor].telefono = nuevo_telefono
						return True

					elif opcion == 3:
						nuevo_domicilio = input("Digite el nuevo domicilio del vendedor: ")
						self.vendedores[pos_vendedor].domicilio = nuevo_domicilio
						return True

					elif opcion == 4:
						nueva_edad = input("Digite la nueva edad del vendedor: ")
						self.vendedores[pos_vendedor].edad = nueva_edad
						return True

					else:
						print("Error - Opción no válida")

				except ValueError:
					print("Error - Debe ingresar un valor entero")

			else:
				return False

		else:
			return False


	def eliminar_vendedor(self, codigo_vendedor):
		pos_vendedor = self.buscar_vendedor(codigo_vendedor)
		if pos_vendedor != -1:
			if self.vendedores[pos_vendedor].codigo == codigo_vendedor:
				del self.vendedores[pos_vendedor]
				return True
			else:
				return False


	def buscar_cliente(self, codigo):
		for i in range(len(self.clientes)):
			if codigo == self.clientes[i].codigo:
				return i
		return -1

	def adicionar_cliente(self, cliente):
		if self.buscar_cliente(cliente.codigo) == -1:
			self.clientes.append(cliente)
			return True
		return False


	def modificar_cliente(self, codigo_cliente):
		pos_cliente = self.buscar_cliente(codigo_cliente)
		if pos_cliente != -1:
			if self.clientes[pos_cliente].codigo == codigo_cliente:
				try:
					print("==========================================")
					print("Seleccione la opción que desea modificar: ")
					print("1. Modificar el nombre")
					print("2. Modificar el teléfono")
					print("3. Modificar el domicilio")
				
					opcion = int(input("Digite la opción que desea modificar: "))
					print("======================================")

					if opcion == 1:
						nuevo_nombre = input("Digite el nuevo nombre del cliente: ")
						self.clientes[pos_cliente].nombre = nuevo_nombre
						return True

					elif opcion == 2:
						nuevo_telefono = int(input("Digite el nuevo teléfono del cliente: "))
						self.clientes[pos_cliente].telefono = nuevo_telefono
						return True

					elif opcion == 3:
						nuevo_domicilio = input("Digite el nuevo domicilio del cliente: ")
						self.clientes[pos_cliente].domicilio = nuevo_domicilio
						return True

					else:
						print("Error - Opción no válida")

				except ValueError:
					print("Error - Debe ingresar un valor entero")

			else:
				return False

		else:
			return False


	def eliminar_cliente(self, codigo_cliente):
		pos_cliente = self.buscar_cliente(codigo_cliente)
		if pos_cliente != -1:
			if self.clientes[pos_cliente].codigo == codigo_cliente:
				del self.clientes[pos_cliente]
				return True
			else:
				return False


	def buscar_producto(self, codigo):
		for i in range(len(self.productos)):
			if codigo == self.productos[i].codigo:
				return i
		return -1

	def adicionar_producto(self, producto):
		if self.buscar_producto(producto.codigo) == -1:
			self.productos.append(producto)
			return True
		return False

	def modificar_producto(self, codigo_producto):
		pos_producto = self.buscar_producto(codigo_producto)
		if pos_producto != -1:
			if self.productos[pos_producto].codigo == codigo_producto:
				try:
					print("==========================================")
					print("Seleccione la opción que desea modificar: ")
					print("1. Modificar el nombre del producto")
					print("2. Modificar el costo del producto")
				
					opcion = int(input("Digite la opción que desea modificar: "))
					print("======================================")

					if opcion == 1:
						nuevo_nombre = input("Digite el nuevo nombre del producto: ")
						self.productos[pos_producto].nombre = nuevo_nombre
						return True

					elif opcion == 2:
						nuevo_costo = float(input("Digite el nuevo costo del producto: "))
						while nuevo_costo < 1:
							print("==================================")
							print("Error - El costo debe ser positivo")
							print("==================================")
							nuevo_costo = float(input("Digite el nuevo costo del producto: "))
							
						self.productos[pos_producto].costo = nuevo_costo
						self.productos[pos_producto].actualizar_valores()
						return True

					else:
						print("Error - Opción no válida")

				except ValueError:
					print("Error - Debe ingresar un valor entero")

			else:
				return False

		else:
			return False

	def eliminar_producto(self, codigo_producto):
		pos_producto = self.buscar_producto(codigo_producto)
		if pos_producto != -1:
			if self.productos[pos_producto].codigo == codigo_producto:
				del self.productos[pos_producto]
				return True
			else:
				return False

	def buscar_venta(self, codigo):
		for i in range(len(self.ventas)):
			if codigo == self.ventas[i].codigo:
				return i
		return -1

	def adicionar_venta(self, venta):
		if self.buscar_venta(venta.codigo) == -1:
			self.ventas.append(venta)
			return True
		return False


	def modificar_venta(self, codigo_venta):
		pos_venta = self.buscar_venta(codigo_venta)
		if pos_venta != -1:
			if self.ventas[pos_venta].codigo == codigo_venta:
				try:
					print("==========================================")
					print("Seleccione la opción que desea modificar: ")
					print("1. Modificar la fecha de la venta")
					print("2. Modificar la cantidad de la venta")
					print("==========================================")

					opcion = int(input("Digite la opción que desea modificar: "))

					if opcion == 1:
						nuevo_dia = int(input("Digite el nuevo día de la venta: "))
						nuevo_mes = int(input("Digite el nuevo mes de la venta: "))
						nuevo_anio = int(input("Digite el nuevo año de la venta: "))

						try:
							nueva_fecha = date(nuevo_anio, nuevo_mes, nuevo_dia)  # Valida días y bisiestos
							hoy = date.today()

							fecha_minima = date(2020, 1, 1)

							if nueva_fecha < fecha_minima:
								print("===========================================")
								print("Error - La fecha no puede ser menor al 2020")
								print("===========================================")
								return False

							if nueva_fecha > hoy:
								print("====================================")
								print("Error - La fecha no puede ser futura")
								print("====================================")
								return False

							self.ventas[pos_venta].dia = nuevo_dia
							self.ventas[pos_venta].mes = nuevo_mes
							self.ventas[pos_venta].anio = nuevo_anio
							print("=======================================")
							print("Fecha de venta modificada correctamente")
							print("=======================================")
							return True

						except ValueError:
							print("=======================================")
							print("Error - La fecha ingresada no es válida")
							print("=======================================")
							return False

					elif opcion == 2:
						nueva_cantidad = int(input("Digite la nueva cantidad de la venta: "))


						if nueva_cantidad <= 0:
							print("======================================")
							print("Error - La cantidad debe ser mayor a 0")
							print("======================================")
							return False

						venta = self.ventas[pos_venta]
						pos_producto = self.buscar_producto(venta.codigo_producto)

						if pos_producto != -1:
							producto = self.productos[pos_producto]

							# Devolver al stock la cantidad anterior
							producto.cantidad += venta.cantidad  

							
							if nueva_cantidad > producto.cantidad:
								print("==========================================")
								print("Error - No hay suficiente stock disponible")
								print("==========================================")
								# Revertimos el stock (como estaba antes de devolverlo)
								producto.cantidad -= venta.cantidad
								return False

							# Actualizar la venta con la nueva cantidad
							venta.cantidad = nueva_cantidad

							# Descontar del stock la nueva cantidad
							producto.cantidad -= nueva_cantidad  

							# Recalcular total
							venta.total = venta.cantidad * venta.valor_unitario 
							
							print("==========================================")
							print("Cantidad de venta modificada correctamente")
							print("==========================================")
							return True

					else:
						print("Error - Opción no válida")

				except ValueError:
					print("Error - Debe ingresar un valor entero")

			else:
				return False
		else:
			return False


	def ventas_producto(self, codigo_producto):
		pos_producto = self.buscar_producto(codigo_producto)
		if pos_producto == -1:
			return False

		ventas_producto = []
		monto_total = 0
		total_ganancia = 0

		for venta in self.ventas:
			if venta.codigo_producto == codigo_producto:

				monto = venta.cantidad * venta.valor_unitario
				ganancia = venta.cantidad * (venta.valor_unitario - (venta.valor_unitario / 1.3))

				monto_total += monto
				total_ganancia += ganancia
				ventas_producto.append(venta)

		return ventas_producto, monto_total, total_ganancia


	def ventas_fecha(self, dia, mes, anio):
		ventas_fecha = []
		monto_total = 0
		total_ganancia = 0

		for venta in self.ventas:
			if venta.dia == dia and venta.mes == mes and venta.anio == anio:
				monto = venta.cantidad * venta.valor_unitario
				ganancia = venta.cantidad * (venta.valor_unitario - (venta.valor_unitario / 1.3))

				monto_total += monto
				total_ganancia += ganancia
				ventas_fecha.append(venta)

		return ventas_fecha, monto_total, total_ganancia


	def ventas_vendedor(self, codigo_vendedor):
		pos_vendedor = self.buscar_vendedor(codigo_vendedor)
		if pos_vendedor == -1:
			return False

		ventas_vendedor = []
		monto_total = 0
		total_ganancia = 0

		for venta in self.ventas:
			if venta.codigo_vendedor == codigo_vendedor:

				monto = venta.cantidad * venta.valor_unitario
				ganancia = venta.cantidad * (venta.valor_unitario - (venta.valor_unitario / 1.3))

				monto_total += monto
				total_ganancia += ganancia
				ventas_vendedor.append(venta)

		return ventas_vendedor, monto_total, total_ganancia

	def ventas_cliente(self, codigo_cliente):
		pos_cliente = self.buscar_cliente(codigo_cliente)
		if pos_cliente == -1:
			return False

		ventas_cliente = []
		monto_total = 0
		total_ganancia = 0

		for venta in self.ventas:
			if venta.codigo_cliente == codigo_cliente:

				monto = venta.cantidad * venta.valor_unitario
				ganancia = venta.cantidad * (venta.valor_unitario - (venta.valor_unitario / 1.3))

				monto_total += monto
				total_ganancia += ganancia
				ventas_cliente.append(venta)

		return ventas_cliente, monto_total, total_ganancia



	def ganancias_totales(self):
		total_ganancia = 0

		for venta in self.ventas:
			
			ganancia = venta.cantidad * (venta.valor_unitario - (venta.valor_unitario / 1.3))

			total_ganancia += ganancia

		return total_ganancia


	def ganancias_producto(self, codigo_producto):
		pos_producto = self.buscar_producto(codigo_producto)
		if pos_producto == -1:
			return False

		total_ganancia = 0

		for venta in self.ventas:
			if venta.codigo_producto == codigo_producto:

				ganancia = venta.cantidad * (venta.valor_unitario - (venta.valor_unitario / 1.3))

				total_ganancia += ganancia

		return total_ganancia






		

