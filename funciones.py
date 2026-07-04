#importamos la libreria 'os' para limpiar la pantalla de la consola
import os
from registros import Producto

def StraInt(caracter):
	if caracter == '1':
		caracter = 1
	elif caracter == '2':
		caracter = 2
	elif caracter == '3':
		caracter = 3
	elif caracter == '4':
		caracter = 4
	elif caracter == '5':
		caracter = 5
	elif caracter == '0':
		caracter = 0
	return caracter

#limpia la consola dependiendo si el os es windows o linux/mac
def LimpiarConsola():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

def MostrarMenuPrincipal():
	menuprincial = (
		'1) Cargar producto',
		'2) Buscar producto',
		'3) Calcular total de venta',
		'4) Productos mas vendidos',
		'5) Estadisticas de ventas',
		'0) Salir')
	for i in menuprincial:
		print(i)

def PedirleOpcionUsuario(opcion):
	opcion = input('Ingrese una opcion: ')
	return opcion

def ValidadorOpcion(opcion):
	opcionesInt = (1,2,3,4,5,0)
	opcionesStr = ('1','2','3','4','5','0')

	if opcion in opcionesStr:
		opcion = StraInt(opcion)
		if opcion in opcionesInt:
			bandera = True
	else:
		bandera = False

	while bandera == False:
		opcion = input('Ingresa una opcion valida: ')
		if opcion in opcionesStr:
			opcion = StraInt(opcion)
			if opcion in opcionesInt:
				bandera = True

	if bandera == True:
		return opcion


#--- FIX: validacion de datos numericos para que no se rompa el programa ---
def PedirFloat(mensaje):
	valido = False
	while valido == False:
		try:
			valor = float(input(mensaje))
			valido = True
		except ValueError:
			print('Error: debe ingresar un valor numerico. Intente nuevamente.')
	return valor

def PedirInt(mensaje):
	valido = False
	while valido == False:
		try:
			valor = int(input(mensaje))
			valido = True
		except ValueError:
			print('Error: debe ingresar un numero entero. Intente nuevamente.')
	return valor


#--- productos ---
def CargarProducto():
	nombre = input('Ingrese el nombre del producto: ')
	while nombre.strip() == '':
		nombre = input('El nombre no puede estar vacio. Ingrese el nombre del producto: ')

	precio = PedirFloat('Ingrese el precio del producto: ')
	stock = PedirInt('Ingrese el nro de stock del producto: ')
	codprod = PedirInt('Ingrese el codigo del producto: ')

	producto = Producto(nombre, precio, stock, codprod)
	return producto

#FIX: convertir todo a str antes de escribir (antes tiraba TypeError)
def GuardarProducto(producto, archivo='archivo.txt'):
	with open(archivo, 'a') as f:
		f.write('///\n')
		f.write(producto.nombre + '\n')
		f.write(str(producto.precio) + '\n')
		f.write(str(producto.stock) + '\n')
		f.write(str(producto.codprod) + '\n')
		f.write('///\n')

def BuscarProductoPorCodigo(codigo, archivo='archivo.txt'):
	try:
		with open(archivo, 'r') as f:
			contenido = f.read()
	except FileNotFoundError:
		return None

	bloques = contenido.split('///')
	for bloque in bloques:
		lineas = [linea for linea in bloque.split('\n') if linea.strip() != '']
		if len(lineas) == 4:
			nombre, precio, stock, codprod = lineas
			if int(codprod) == codigo:
				return Producto(nombre, float(precio), int(stock), int(codprod))
	return None
