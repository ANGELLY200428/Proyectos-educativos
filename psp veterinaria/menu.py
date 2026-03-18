from os import system
from veterinaria import Veterinaria
from cliente import Cliente
from mascota import Mascota

class Menu:

	def __init__(self):
		self.veterinaria = Veterinaria()

	def login(self):
		intentos = 3

		while intentos > 0:
			system("cls")
			print("==================================")
			print("===== INICIO DE SESIÓN ADMIN =====")
			print("==================================")

			usuario = input("Usuario: ")
			clave = input("Contraseña: ")

			if usuario == "admin" and clave == "1234":
				print("================")
				print("Acceso concedido")
				input()
				return True
			else:
				intentos -= 1
				print("=========================")
				print("Credenciales incorrectas")
				print("Intentos restantes:", intentos)
				input()

		return False

	def registrar_cliente(self):
		system("cls")
		print("==============================")
		print("==== REGISTRO DE CLIENTE =====")
		print("==============================")
		codigo = input("Código cliente: ")
		while codigo == "":
			codigo = input("Código cliente: ")

		nombre = input("Digite el nombre: ")
		while nombre == "":
			nombre = input("Digite el nombre: ")

		try:
			telefono = int(input("Digite el teléfono: "))
		except:
			print("=============================================")
			print("Error: el teléfono solo debe contener números")
			input()
			return

		cliente = Cliente(codigo, nombre, telefono)
		if self.veterinaria.adicionar_cliente(cliente):
			print("================================")
			print("Cliente registrado correctamente")
		else:
			print("====================")
			print("El cliente ya existe")
		input()

	def listar_clientes(self):
		system("cls")
		print("==============================")
		print("====== LISTA DE CLIENTE ======")
		print("==============================")
		for c in self.veterinaria.clientes:
			print("============================")
			print("Código cliente: %s" % (c.codigo))
			print("Nombre cliente: %s" % (c.nombre))
			print("Teléfono cliente: %s" % (c.telefono))
			print("============================")
		input()


	def modificar_cliente(self):
		system("cls")
		print("============================")
		print("=== MODIFICACIÓN CLIENTE ===")
		print("============================")
		codigo = input("Código del cliente: ")
		if self.veterinaria.modificar_cliente(codigo):
			print("==================")
			print("Cliente modificado")
		else:
			print("=====================")
			print("Cliente no encontrado")
		input()

	def eliminar_cliente(self):
		system("cls")
		print("===========================")
		print("=== ELIMINACIÓN CLIENTE ===")
		print("===========================")
		codigo = input("Código del cliente: ")
		if self.veterinaria.eliminar_cliente(codigo):
			print("=================")
			print("Cliente eliminado")
		else:
			print("=====================")
			print("Cliente no encontrado")
		input()

	def registrar_mascota(self):
		system("cls")
		print("============================")
		print("=== REGISTRO DE MASCOTAS ===")
		print("============================")
		codigo = input("Código mascota: ")
		while codigo == "":
			codigo = input("Código mascota: ")

		nombre = input("Nombre: ")
		while nombre == "":
			nombre = input("Nombre: ")

		especie = input("Especie: ")
		while especie == "":
			especie = input("Especie: ")

		try:
			edad = int(input("Edad: "))
		except:
			print("=========================================")
			print("Error: La edad solo debe contener números")
			input()
			return
		dueno = input("Código dueño: ")

		mascota = Mascota(codigo, nombre, especie, edad, dueno)
		resultado = self.veterinaria.adicionar_mascota(mascota)
		if resultado == "OK":
			print("================================")
			print("Mascota registrada correctamente")
		elif resultado == "NO_DUENO":
			print("=========================")
			print("Error: el dueño no existe")
		else:
			print("====================")
			print("La mascota ya existe")
		input()

	def listar_mascotas(self):
		system("cls")
		print("===========================")
		print("==== LISTA DE MASCOTAS ====")
		for m in self.veterinaria.mascotas:
			print("Código mascota: %s" % (m.codigo))
			print("Nombre mascota: %s" % (m.nombre))
			print("Especie mascota: %s" % (m.edad))
			print("Código dueño mascota: %s" % (m.codigo_dueno))
			print("===================================")
		input()

	def modificar_mascota(self):
		system("cls")
		print("===============================")
		print("=== MODIFICACIÓN DE MASCOTA ===")
		print("===============================")
		codigo = input("Código mascota: ")
		if self.veterinaria.modificar_mascota(codigo):
			print("==========================")
			print("Mascota modificada")
		else:
			print("==========================")
			print("Mascota no encontrada")
		input()

	def eliminar_mascota(self):
		system("cls")
		print("==============================")
		print("=== ELIMINACIÓN DE MASCOTA ===")
		print("==============================")
		codigo = input("Código mascota: ")
		if self.veterinaria.eliminar_mascota(codigo):
			print("==========================")
			print("Mascota eliminada")
		else:
			print("=====================")
			print("Mascota no encontrada")
		input()

	def mostrar_menu(self):
		while True:
			system("cls")
			print("===== VETERINARIA =====")
			print("1. Registrar cliente")
			print("2. Listar clientes")
			print("3. Modificar cliente")
			print("4. Eliminar cliente")
			print("5. Registrar mascota")
			print("6. Listar mascotas")
			print("7. Modificar mascota")
			print("8. Eliminar mascota")
			print("9. Salir")

			op = input("Opción: ")

			if op == "1": self.registrar_cliente()
			elif op == "2": self.listar_clientes()
			elif op == "3": self.modificar_cliente()
			elif op == "4": self.eliminar_cliente()
			elif op == "5": self.registrar_mascota()
			elif op == "6": self.listar_mascotas()
			elif op == "7": self.modificar_mascota()
			elif op == "8": self.eliminar_mascota()
			elif op == "9": break

if __name__ == "__main__":
	menu = Menu()

	if menu.login():
		menu.mostrar_menu()
	else:
		print("Acceso denegado")