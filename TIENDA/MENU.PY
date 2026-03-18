from os import system
from vendedor import Vendedor
from tienda import Tienda
from cliente import Cliente
from producto import Producto
from datetime import datetime
from venta import Venta 

class Menu():

	def __init__(self):
		self.tienda = Tienda()
		self.vendedor = Vendedor
		self.producto = Producto

	def registrar_vendedor(self):
		system ("cls")
		print("===========================")
		print("     REGISTRAR VENDEDOR    ")
		print("===========================")

		codigo_vendedor = str(input("Digite el código del vendedor: "))
		while codigo_vendedor == "":
			codigo_vendedor = str(input("Digite el código del vendedor: "))

		nombre_vendedor = str(input("Digite el nombre del vendedor: "))
		while nombre_vendedor == "":
			nombre_vendedor = str(input("Digite el nombre del vendedor: "))

		telefono_vendedor = int(input("Digite el teléfono del vendedor: "))
		while telefono_vendedor < 1:
			telefono_vendedor = int(input("Digite el teléfono del vendedor: "))

		domicilio_vendedor = str(input("Digite el domicilio del vendedor: "))
		while telefono_vendedor == "":
			domicilio_vendedor = str(input("Digite el domicilio del vendedor: "))


		edad_vendedor = int(input("Digite la edad del vendedor(entre 18 y 59 años): "))
		if edad_vendedor <16 or edad_vendedor >59:
			print("===================================")
			print("Error - La edad está fuera de rango")
			print("===================================")
			input()
			return

		vendedor = Vendedor(codigo_vendedor, nombre_vendedor, telefono_vendedor, domicilio_vendedor, edad_vendedor)

		if self.tienda.adicionar_vendedor(vendedor) == True:
			print("==================================================")
			print("Información - El Vendedor fue creado correctamente")
			print("==================================================")
			input()

		else:
			print("=========================================")
			print("Error - El Vendedor no se puede adicionar")
			print("=========================================")
			input()


	def listar_vendedor(self):
		system ("cls")
		print("==========================")
		print("     LISTAR VENDEDORES    ")
		print("==========================")

		for vendedor in self.tienda.vendedores:
			print("========================================")
			print("Código: %s" % (vendedor.codigo))
			print("Nombre: %s" % (vendedor.nombre))
			print("Teléfono: %s" % (vendedor.telefono))
			print("Domicilio: %s" % (vendedor.domicilio))
			print("Edad: %s" % (vendedor.edad))
			print("========================================")
		input()

	def modificar_vendedor(self):
		system ("cls")
		print("===========================")
		print("     MODIFICAR VENDEDOR    ")
		print("===========================")

		codigo_vendedor = str(input("Ingrese el código del vendedor que desea modificar: "))
		if self.tienda.modificar_vendedor(codigo_vendedor) == True:
			print("====================================================")
			print("Info - El Vendedor fue modificado satisfactoriamente")
			print("====================================================")
			input()

		else:
			print("===========================================")
			print("Error - El Vendedor no puede ser modificado")
			print("===========================================")
			input()

	def eliminar_vendedor(self):
		system ("cls")
		print("==========================")
		print("     ELIMINAR VENDEDOR    ")
		print("==========================")

		codigo_vendedor = str(input("Ingrese el código del vendedor que desea eliminar: "))
		if self.tienda.eliminar_vendedor(codigo_vendedor) == True:
			print("===================================================")
			print("Info - El Vendedor fue eliminado satisfactoriamente")
			print("===================================================")
			input()

		else:
			print("==========================================")
			print("Error - El Vendedor no puede ser eliminado")
			print("==========================================")
			input()


	def registrar_cliente(self):
		system ("cls")
		print("===========================")
		print("     REGISTRAR CLIENTE    ")
		print("===========================")
		codigo_cliente = str(input("Digite el código del cliente: "))
		while codigo_cliente == "":
			codigo_cliente = str(input("Digite el código del cliente: "))

		nombre_cliente = str(input("Digite el nombre del cliente: "))
		while nombre_cliente == "":
			nombre_cliente = str(input("Digite el nombre del cliente: "))

		telefono_cliente = int(input("Digite el teléfono del cliente: "))
		while telefono_cliente < 1:
			telefono_cliente = int(input("Digite el teléfono del cliente: "))

		domicilio_cliente = str(input("Digite el domicilio del cliente: "))
		while domicilio_cliente == "":
			domicilio_cliente = str(input("Digite el domicilio del cliente: "))
		cliente = Cliente(codigo_cliente, nombre_cliente, telefono_cliente, domicilio_cliente)

		if self.tienda.adicionar_cliente(cliente) == True:
			print("=================================================")
			print("Información - El Cliente fue creado correctamente")
			print("=================================================")
			input()

		else:
			print("========================================")
			print("Error - El Cliente no se puede adicionar")
			print("========================================")
			input()


	def modificar_cliente(self):
		system ("cls")
		print("==========================")
		print("     MODIFICAR CLIENTE    ")
		print("==========================")

		codigo_cliente = str(input("Ingrese el código del cliente que desea modificar: "))
		if self.tienda.modificar_cliente(codigo_cliente) == True:
			print("===================================================")
			print("Info - El Cliente fue modificado satisfactoriamente")
			print("===================================================")
			input()

		else:
			print("==========================================")
			print("Error - El Cliente no puede ser modificado")
			print("==========================================")
			input()


	def listar_cliente(self):
		system ("cls")
		print("========================")
		print("     LISTAR CLIENTES    ")
		print("========================")

		for cliente in self.tienda.clientes:
			print("========================================")
			print("Código: %s" % (cliente.codigo))
			print("Nombre: %s" % (cliente.nombre))
			print("Teléfono: %s" % (cliente.telefono))
			print("Domicilio: %s" % (cliente.domicilio))
			print("========================================")
		input()


	def eliminar_cliente(self):
		system ("cls")
		print("=========================")
		print("     ELIMINAR CLIENTE    ")
		print("=========================")

		codigo_cliente = str(input("Ingrese el código del cliente que desea eliminar: "))
		if self.tienda.eliminar_cliente(codigo_cliente) == True:
			print("==================================================")
			print("Info - El Cliente fue eliminado satisfactoriamente")
			print("==================================================")
			input()

		else:
			print("=========================================")
			print("Error - El Cliente no puede ser eliminado")
			print("=========================================")
			input()

	def registrar_producto(self):
		system ("cls")
		print("===========================")
		print("     REGISTRAR PRODUCTO    ")
		print("===========================")
		codigo_producto = str(input("Digite el código del producto: "))
		while codigo_producto == "":
			codigo_producto = str(input("Digite el código del producto: "))

		nombre_producto = str(input("Digite el nombre del producto: "))
		while nombre_producto == "":
			nombre_producto = str(input("Digite el nombre del producto: "))

		cantidad_producto = int(input("Digite la cantidad del producto: "))
		if cantidad_producto <= 0:
			print("==========================================")
			print("Error: la cantidad debe ser mayor que cero")
			print("==========================================")
			input()
			return
		
		costo_producto = float(input("Digite el costo del producto: "))
		while costo_producto < 1:
			costo_producto = float(input("Digite el costo del producto: "))

		producto = Producto(codigo_producto, nombre_producto, cantidad_producto, costo_producto)

		if self.tienda.adicionar_producto(producto) == True:
			print("==================================================")
			print("Información - El Producto fue creado correctamente")
			print("==================================================")
			input()

		else:
			print("=========================================")
			print("Error - El Producto no se puede adicionar")
			print("=========================================")
			input()

	def listar_producto(self):
		system ("cls")
		print("=========================")
		print("     LISTAR PRODUCTOS    ")
		print("=========================")

		for producto in self.tienda.productos:
			print("========================================")
			print("Código: %s" % (producto.codigo))
			print("Nombre: %s" % (producto.nombre))
			print("Cantidad: %s" % (producto.cantidad))
			print("Costo compra (unidad)): %s" % (producto.costo))
			print("Total: %s" % (producto.total))
			print("Valor unitario: %s" % (producto.valor_unitario))
			print("========================================")
		input()

	def listar_producto_stock(self):
		system ("cls")
		print("===================================")
		print("     LISTAR PRODUCTOS CON STOCK    ")
		print("===================================")

		for producto in self.tienda.productos:
			if producto.cantidad >= 1:
				print("========================================")
				print("Código: %s" % (producto.codigo))
				print("Nombre: %s" % (producto.nombre))
				print("Cantidad: %s" % (producto.cantidad))
				print("========================================")

		input()

	def listar_producto_sin_stock(self):
		system ("cls")
		print("===================================")
		print("     LISTAR PRODUCTOS SIN STOCK    ")
		print("===================================")

		for producto in self.tienda.productos:
			if producto.cantidad <= 0:
				print("========================================")
				print("Código: %s" % (producto.codigo))
				print("Nombre: %s" % (producto.nombre))
				print("========================================")

		input()

	def modificar_producto(self):
		system ("cls")
		print("===========================")
		print("     MODIFICAR PRODUCTO    ")
		print("===========================")

		codigo_producto = str(input("Ingrese el código del producto que desea modificar: "))
		if self.tienda.modificar_producto(codigo_producto) == True:
			print("====================================================")
			print("Info - El Producto fue modificado satisfactoriamente")
			print("====================================================")
			input()

		else:
			print("===========================================")
			print("Error - El Producto no puede ser modificado")
			print("===========================================")
			input()

	def eliminar_producto(self):
		system ("cls")
		print("==========================")
		print("     ELIMINAR PRODUCTO    ")
		print("==========================")

		codigo_producto = str(input("Ingrese el código del producto que desea eliminar: "))
		if self.tienda.eliminar_producto(codigo_producto) == True:
			print("==================================================")
			print("Info - El Producto fue eliminado satisfactoriamente")
			print("==================================================")
			input()

		else:
			print("=========================================")
			print("Error - El Producto no puede ser eliminado")
			print("=========================================")
			input()

	def registrar_venta(self):
		system ("cls")
		print("========================")
		print("     REGISTRAR VENTA    ")
		print("========================")
		codigo_venta = str(input("Digite el código de la venta: "))

		fecha_actual = datetime.now()
		dia = fecha_actual.day
		mes = fecha_actual.month
		anio = fecha_actual.year

		codigo_vendedor = str(input("Digite el código del vendedor: "))

		pos_vendedor = self.tienda.buscar_vendedor(codigo_vendedor)
		if pos_vendedor == -1:
			print("============================")
			print("Error: El vendedor no existe")
			print("============================")
			input()
			return

		vendedor = self.tienda.vendedores[pos_vendedor]
		print("Nombre del vendedor: ", vendedor.nombre)
		nombre_vendedor = vendedor.nombre

		codigo_cliente = str(input("Digite el codigo del cliente: "))

		pos_cliente = self.tienda.buscar_cliente(codigo_cliente)
		if pos_cliente == -1:
			print("===========================")
			print("Error: El cliente no existe")
			print("===========================")
			input()
			return

		cliente = self.tienda.clientes[pos_cliente]
		print("Nombre del cliente: ", cliente.nombre)
		nombre_cliente = cliente.nombre

		codigo_producto = str(input("Digite el codigo del producto: "))

		pos_producto = self.tienda.buscar_producto(codigo_producto)
		if pos_producto == -1:
			print("============================")
			print("Error: El producto no existe")
			print("============================")
			input()
			return
			

		producto = self.tienda.productos[pos_producto]
		print("Nombre del producto: ", producto.nombre)
		print("Valor unitario de producto: ", producto.valor_unitario)
		nombre_producto = producto.nombre
		valor_unitario = producto.valor_unitario

		if producto.cantidad == 0:
			print("=======================================")
			print("Error: El producto se encuentra agotado")
			print("=======================================")
			input()
			return
			


		cantidad_producto = int(input("Ingrese la cantidad del producto: "))

		if cantidad_producto > 0:

			if producto.cantidad < cantidad_producto:
				print("==================================================")
				print("Error: No están disponibles las unidades que desea")
				print("==================================================")
				input()
				return
				

			total = cantidad_producto * producto.valor_unitario
			print("TOTAL DE LA VENTA:", total)
			producto.cantidad -= cantidad_producto

			venta = Venta(codigo_venta, dia, mes, anio, codigo_vendedor, nombre_vendedor, codigo_cliente, nombre_cliente, codigo_producto, nombre_producto, valor_unitario, cantidad_producto, total)

			if self.tienda.adicionar_venta(venta) == True:
				print("===============================================")
				print("Información - La Venta fue creada correctamente")
				print("===============================================")
				input()

			else:
				print("======================================")
				print("Error - La Venta no se puede adicionar")
				print("======================================")
				input()

		else:
			print("======================================")
			print("Error - La cantidad debe ser mayor a 0")
			print("======================================")
			input()


	def listar_todas_ventas(self):
		system ("cls")
		print("================================")
		print("     LISTAR TODAS LAS VENTAS    ")
		print("================================")

		for venta in self.tienda.ventas:
			print("========================================")
			print("Código venta: %s" % (venta.codigo))
			print("FECHA VENTA: Día: %s / Mes: %s / Año: %s" %(venta.dia, venta.mes, venta.anio))
			print("Código vendedor: %s" % (venta.codigo_vendedor))
			print("Nombre vendedor: %s" % (venta.nombre_vendedor))
			print("Código cliente: %s" % (venta.codigo_cliente))
			print("Nombre cliente: %s" % (venta.nombre_cliente))
			print("Código producto: %s" % (venta.codigo_producto))
			print("Nombre producto: %s" % (venta.nombre_producto))
			print("Valor unitario: %s" % (venta.valor_unitario))
			print("Cantidad del producto: %s" % (venta.cantidad))
			print("Total de la venta: %s" % (venta.total))
			print("========================================")
		input()

	def modificar_venta(self):
		system ("cls")
		print("========================")
		print("     MODIFICAR VENTA    ")
		print("========================")

		codigo_venta = str(input("Ingrese el código de la venta que desea modificar: "))
		if self.tienda.modificar_venta(codigo_venta) == True:
			print("=================================================")
			print("Info - La venta fue modificada satisfactoriamente")
			print("=================================================")
			input()

		else:
			print("========================================")
			print("Error - La venta no puede ser modificada")
			print("========================================")
			input()


	def listar_venta_producto(self):
		system("cls")
		print("===================================")
		print("     LISTAR VENTAS POR PRODUCTO    ")
		print("===================================")

		codigo_producto = str(input("Ingrese el código del producto: "))
		resultado = self.tienda.ventas_producto(codigo_producto)

		if resultado == False:
			print("==============================================")
			print("Error - El producto no se encuentra registrado")
			print("==============================================")
			input()
			return

		ventas_producto, total_monto, total_ganancia = resultado

		if ventas_producto: # Si existe en la lista entonces
			for venta in ventas_producto:
				print("========================================")
				print("Código venta: %s" % (venta.codigo))
				print("FECHA VENTA: Día: %s / Mes: %s / Año: %s" % (venta.dia, venta.mes, venta.anio))
				print("Código vendedor: %s" % (venta.codigo_vendedor))
				print("Nombre vendedor: %s" % (venta.nombre_vendedor))
				print("Código cliente: %s" % (venta.codigo_cliente))
				print("Nombre cliente: %s" % (venta.nombre_cliente))
				print("Código producto: %s" % (venta.codigo_producto))
				print("Nombre producto: %s" % (venta.nombre_producto))
				print("Valor unitario: %s" % (venta.valor_unitario))
				print("Cantidad del producto: %s" % (venta.cantidad))
				print("Total de la venta: %s" % (venta.total))
				print("========================================")

			print("\n======== TOTAL Y GANANCIA =========")
			print(f"Monto total: ${total_monto} pesos")
			print(f"Ganancia total: ${total_ganancia} pesos")
			print("=====================================")
		else: 
			print("==============================================")
			print("No existen ventas registradas de este producto")
			print("==============================================")

		input()


	def listar_venta_fecha(self):
		system("cls")
		print("================================")
		print("     LISTAR VENTAS POR FECHA    ")
		print("================================")

		dia = int(input("Ingrese el día  de la venta: "))
		mes = int(input("Ingrese el mes  de la venta: "))
		anio = int(input("Ingrese el año  de la venta: "))

		ventas_fecha, total_monto, total_ganancia = self.tienda.ventas_fecha(dia, mes, anio)

		if ventas_fecha:
			for venta in ventas_fecha:
				print("========================================")
				print("Código venta: %s" % (venta.codigo))
				print("FECHA VENTA: Día: %s / Mes: %s / Año: %s" % (venta.dia, venta.mes, venta.anio))
				print("Código vendedor: %s" % (venta.codigo_vendedor))
				print("Nombre vendedor: %s" % (venta.nombre_vendedor))
				print("Código cliente: %s" % (venta.codigo_cliente))
				print("Nombre cliente: %s" % (venta.nombre_cliente))
				print("Código producto: %s" % (venta.codigo_producto))
				print("Nombre producto: %s" % (venta.nombre_producto))
				print("Valor unitario: %s" % (venta.valor_unitario))
				print("Cantidad del producto: %s" % (venta.cantidad))
				print("Total de la venta: %s" % (venta.total))
				print("========================================")

			print("\n============= TOTAL Y GANANCIA ============")
			print(f"Monto total de la fecha: ${total_monto} pesos")
			print(f"Ganancia total de la fecha: ${total_ganancia} pesos")
			print("=============================================")
		else: 
			print("===========================================")
			print("No existen ventas registradas de esta fecha")
			print("===========================================")

		input()


	def listar_venta_vendedor(self):
		system("cls")
		print("===================================")
		print("     LISTAR VENTAS POR VENDEDOR    ")
		print("===================================")

		codigo_vendedor = str(input("Ingrese el código del vendedor: "))
		resultado = self.tienda.ventas_vendedor(codigo_vendedor)

		if resultado == False:
			print("==============================================")
			print("Error - El vendedor no se encuentra registrado")
			print("==============================================")
			input()
			return

		ventas_vendedor, total_monto, total_ganancia = resultado

		if ventas_vendedor:
			for venta in ventas_vendedor:
				print("========================================")
				print("Código venta: %s" % (venta.codigo))
				print("FECHA VENTA: Día: %s / Mes: %s / Año: %s" % (venta.dia, venta.mes, venta.anio))
				print("Código vendedor: %s" % (venta.codigo_vendedor))
				print("Nombre vendedor: %s" % (venta.nombre_vendedor))
				print("Código cliente: %s" % (venta.codigo_cliente))
				print("Nombre cliente: %s" % (venta.nombre_cliente))
				print("Código producto: %s" % (venta.codigo_producto))
				print("Nombre producto: %s" % (venta.nombre_producto))
				print("Valor unitario: %s" % (venta.valor_unitario))
				print("Cantidad del producto: %s" % (venta.cantidad))
				print("Total de la venta: %s" % (venta.total))
				print("========================================")

			print("\n=============== TOTAL Y GANANCIA ===============")
			print(f"Monto total: ${total_monto} pesos")
			print(f"Ganancia total generadas del vendedor: ${total_ganancia} pesos")
			print("==================================================")
		else: 
			print("==============================================")
			print("No existen ventas registradas de este vendedor")
			print("==============================================")

		input()




	def listar_compra_cliente(self):
		system("cls")
		print("===================================")
		print("     LISTAR COMPRAS POR CLIENTE    ")
		print("===================================")

		codigo_cliente = str(input("Ingrese el código del cliente: "))
		resultado = self.tienda.ventas_cliente(codigo_cliente)

		if resultado == False:
			print("==============================================")
			print("Error - El cliente no se encuentra registrado")
			print("==============================================")
			input()
			return

		ventas_cliente, total_monto, total_ganancia = resultado

		if ventas_cliente:
			for venta in ventas_cliente:
				print("========================================")
				print("Código venta: %s" % (venta.codigo))
				print("FECHA VENTA: Día: %s / Mes: %s / Año: %s" % (venta.dia, venta.mes, venta.anio))
				print("Código vendedor: %s" % (venta.codigo_vendedor))
				print("Nombre vendedor: %s" % (venta.nombre_vendedor))
				print("Código cliente: %s" % (venta.codigo_cliente))
				print("Nombre cliente: %s" % (venta.nombre_cliente))
				print("Código producto: %s" % (venta.codigo_producto))
				print("Nombre producto: %s" % (venta.nombre_producto))
				print("Valor unitario: %s" % (venta.valor_unitario))
				print("Cantidad del producto: %s" % (venta.cantidad))
				print("Total de la venta: %s" % (venta.total))
				print("========================================")

			print("\n=============== TOTAL Y GANANCIA ===============")
			print(f"Monto total de las compras del cliente: ${total_monto} pesos")
			print(f"Ganancia total generadas por el cliente: ${total_ganancia} pesos")
			print("==================================================")
		else: 
			print("==============================================")
			print("No existen ventas registradas de este vendedor")
			print("==============================================")

		input()



	def reporte_inversion_total(self):
		system("cls")
		print("================================")
		print("   REPORTE DE INVERSIÓN TOTAL   ")	
		print("================================")

		suma = 0
		for inversion in self.tienda.productos:
			suma += inversion.total

		print("=================================================================")
		print("La inversión total de todos los productos es: $%s"%(suma), "PESOS")
		print("=================================================================")
		input()
		return

	def reporte_inversion_producto(self):
		system("cls")
		print("=============================================")
		print("   REPORTE DE INVERSIÓN TOTAL POR PRODUCTO   ")	
		print("=============================================")

		codigo_producto = input("Ingrese el código del producto: ")

		pos_producto = self.tienda.buscar_producto(codigo_producto)

		if pos_producto == -1:
			print("==============================================")
			print("Error - El producto no se encuentra registrado")
			print("==============================================")
			input()
			return

		producto = self.tienda.productos[pos_producto]

		print("======================================================")
		print("Nombre del producto: %s" %(producto.nombre))
		print("La inversión total del producto es: $%s "%(producto.total), "PESOS")
		print("======================================================")
		input()
		return


	def reporte_ganancias_totales(self):
		system("cls")
		print("==================================")
		print("   REPORTE DE GANANCIAS TOTALES   ")	
		print("==================================")

		total_ganancia = self.tienda.ganancias_totales()
		
		print("=====  GANANCIAS TOTALES  =====")
		print(f"Ganancia total: ${total_ganancia}")
		input()


	def reporte_ganancias_producto(self):
		system("cls")
		print("=======================================")
		print("   REPORTE DE GANANCIAS POR PRODUCTO   ")	
		print("=======================================")

		codigo_producto = input("Ingrese el código del producto: ")

		pos_producto = self.tienda.buscar_producto(codigo_producto)

		if pos_producto == -1:
			print("==============================================")
			print("Error - El producto no se encuentra registrado")
			print("==============================================")
			input()
			return

		producto = self.tienda.productos[pos_producto]

		resultado = self.tienda.ganancias_producto(codigo_producto)
		total_ganancia = resultado

		print("=====  GANANCIAS DEL PRODUCTO  =====")
		print(f"Nombre: {producto.nombre}")
		print(f"Ganancia total: ${total_ganancia}")
		input()



	def mostrar_menu(self):
		while True:
			system ("cls")
			print("=============================")
			print("          TIENDA POO         ")
			print("=============================")
			print("             MENÚ            ")
			print("=============================")
			print("=============================")
			print("a. Registrar vendedor")
			print("b. Listar vendedores")
			print("c. Modificar vendedor")
			print("d. Eliminar vendedor")
			print("e. Registrar cliente")
			print("f. Listar clientes")
			print("g. Modificar cliente")
			print("h. Eliminar cliente")
			print("i. Registrar producto")
			print("j. Listar productos")
			print("k. Listar productos con stock")
			print("l. Listar productos sin stock")
			print("m. modificar producto")
			print("n. Eliminar producto")
			print("o. Registrar venta")
			print("p. Listar todas las ventas de la tienda")
			print("q. Modificar venta")
			print("r. Mostrar ventas por producto")
			print("s. Mostrar ventas por fecha")
			print("t. Mostrar ventas por vendedor")
			print("u. Mostrar compras por cliente")
			print("v. Generar reporte de inversión total")
			print("w. Generar reporte de inversión por producto")
			print("x. Generar reporte de ganancias totales")
			print("y. Generar reporte de ganancias totales por producto")
			print("z. Salir del sistema")


			try:
				opcion = str(input("Ingrese la opción deseada: "))
				print("===================")

				if opcion == 'a' or opcion == 'A':
					self.registrar_vendedor()

				elif opcion == 'b' or opcion == 'B':
					self.listar_vendedor()

				elif opcion == 'c' or opcion == 'C':
					self.modificar_vendedor()

				elif opcion == 'd' or opcion == 'D':
					self.eliminar_vendedor()

				elif opcion == 'e' or opcion == 'E':
					self.registrar_cliente()

				elif opcion == 'f' or opcion == 'F':
					self.listar_cliente()

				elif opcion == 'g' or opcion == 'G':
					self.modificar_cliente()

				elif opcion == 'h' or opcion == 'H':
					self.eliminar_cliente()

				elif opcion == 'i' or opcion == 'I':
					self.registrar_producto()

				elif opcion == 'j' or opcion == 'J':
					self.listar_producto()

				elif opcion == 'k' or opcion == 'K':
					self.listar_producto_stock()

				elif opcion == 'l' or opcion == 'L':
					self.listar_producto_sin_stock()

				elif opcion == 'm' or opcion == 'M':
					self.modificar_producto()

				elif opcion == 'n' or opcion == 'N':
					self.eliminar_producto()

				elif opcion == 'o' or opcion == 'O':
					self.registrar_venta()

				elif opcion == 'p' or opcion == 'P':
					self.listar_todas_ventas()

				elif opcion == 'q' or opcion == 'Q':
					self.modificar_venta()

				elif opcion == 'r' or opcion == 'R':
					self.listar_venta_producto()

				elif opcion == 's' or opcion == 'S':
					self.listar_venta_fecha()

				elif opcion == 't' or opcion == 'T':
					self.listar_venta_vendedor()

				elif opcion == 'u' or opcion == 'U':
					self.listar_compra_cliente()

				elif opcion == 'v' or opcion == 'V':
					self.reporte_inversion_total()

				elif opcion == 'w' or opcion == 'W':
					self.reporte_inversion_producto()

				elif opcion == 'x' or opcion == 'X':
					self.reporte_ganancias_totales()

				elif opcion == 'y' or opcion == 'Y':
					self.reporte_ganancias_producto()

				elif opcion == 'z' or opcion == 'Z':
					break

				else:
					print("=======================")
					print("Error - Opción inválida")
					print("=======================")
					input()

			except ValueError:
				print("======================")
				print("Error - Dato no válido")
				print("======================")
				input()

if __name__ == '__main__':
	menu = Menu()
	menu.mostrar_menu()

