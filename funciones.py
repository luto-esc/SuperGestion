#importamos la libreria 'os' para limpiar la pantalla de la consola
import os
from registros import Producto, Descuento

def mostrarlogin(estado):
	
	with open('usuarios.txt', 'r') as f:
		contenido = f.read().splitlines()

		usuario = str(input('Ingrese el usuario: '))
		contraseña = str(input('Ingrese la contraseña: '))

		for us in contenido:
			if us == 'admin':
				for con in contenido:
					if con == 'admin123':
						return 'a'
					else:
						print('contraseña incorrecta')
			elif us == 'operador':
				for con in contenido:
					if con == 'operador123':
						return 'o'
					else:
						print('contraseña incorrecta')




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
	elif caracter == '6':
		caracter = 6
	elif caracter == '7':
        carácter = 7
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
		'2) Cargar descuento',
		'3) Buscar producto',
		'4) Calcular total de venta',
		'5) Productos mas vendidos',
		'6) Estadisticas de ventas',
		'7) Promocion maorista y minorista',
		'0) Salir')
	for i in menuprincial:
		print(i)

def PedirleOpcionUsuario(opcion):
	opcion = input('Ingrese una opcion: ')
	return opcion

def ValidadorOpcion(opcion):
	opcionesInt = (1,2,3,4,5,6,7,0)
	opcionesStr = ('1','2','3','4','5','6','7','0')

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


#--- descuentos ---
def CargarDescuento():
	coddesc = PedirInt('Ingrese el codigo del descuento: ')
	valor = PedirFloat('Ingrese el porcentaje del descuento (ej: 10 = 10%): ')
	descuento = Descuento(coddesc, valor)
	return descuento

def GuardarDescuento(descuento, archivo='descuentos.txt'):
	with open(archivo, 'a') as f:
		f.write('///\n')
		f.write(str(descuento.coddesc) + '\n')
		f.write(str(descuento.valor) + '\n')
		f.write('///\n')

def BuscarDescuentoPorCodigo(codigo, archivo='descuentos.txt'):
	try:
		with open(archivo, 'r') as f:
			contenido = f.read()
	except FileNotFoundError:
		return None

	bloques = contenido.split('///')
	for bloque in bloques:
		lineas = [linea for linea in bloque.split('\n') if linea.strip() != '']
		if len(lineas) == 2:
			coddesc, valor = lineas
			if int(coddesc) == codigo:
				return Descuento(int(coddesc), float(valor))
	return None


#--- calculo de total de venta (varios productos) ---
def CalcularTotal():
	items = []   #cada item: [codprod, nombre, cantidad, subtotal]
	continuar = 's'

	while continuar.lower() == 's':
		codprod = PedirInt('Ingrese el codigo del producto: ')
		producto = BuscarProductoPorCodigo(codprod)

		if producto is None:
			print('No existe un producto con ese codigo.')
		else:
			cantidad = PedirInt('Ingrese la cantidad: ')
			if cantidad > producto.stock:
				print('No hay stock suficiente. Stock disponible: ' + str(producto.stock))
			else:
				subtotal = producto.precio * cantidad
				items.append([producto.codprod, producto.nombre, cantidad, subtotal])
				print(producto.nombre + ' x' + str(cantidad) + ' -> $' + str(subtotal))

		continuar = input('¿Desea agregar otro producto? (s/n): ')

	if len(items) == 0:
		print('No se cargo ningun producto en la venta.')
		return

	total = 0
	for item in items:
		total = total + item[3]

	print('\nSubtotal de la venta: $' + str(total))

	descuento_frac = 0
	aplicar = input('¿Desea aplicar un descuento? (s/n): ')
	if aplicar.lower() == 's':
		coddesc = PedirInt('Ingrese el codigo del descuento: ')
		descuento = BuscarDescuentoPorCodigo(coddesc)
		if descuento is None:
			print('No existe un descuento con ese codigo. No se aplicara descuento.')
		else:
			descuento_frac = descuento.valor / 100
			print('Descuento aplicado: ' + str(descuento.valor) + '%')

	total_final = total * (1 - descuento_frac)
	print('TOTAL A PAGAR: $' + str(round(total_final, 2)))

	#registramos cada producto vendido, con el % de descuento ya aplicado
	for item in items:
		codprod, nombre, cantidad, subtotal = item
		monto_final = subtotal * (1 - descuento_frac)
		GuardarRegistroVenta(codprod, nombre, cantidad, monto_final)


#--- registro de ventas (para futuras estadisticas) ---
def GuardarRegistroVenta(codprod, nombre, cantidad, monto, archivo='ventas.txt'):
	with open(archivo, 'a') as f:
		f.write('///\n')
		f.write(str(codprod) + '\n')
		f.write(nombre + '\n')
		f.write(str(cantidad) + '\n')
		f.write(str(monto) + '\n')
		f.write('///\n')

# promociones mayorista y minorista 
def CalcularPromociones():
	items = []   # [cada item: codprod, nombre, cantidad, subtotal, descuento aplicado]
	continuar = 's'

	while continuar.lower() == 's':
		codprod = PedirInt('Ingrese el codigo del producto: ')
		producto = BuscarProductoPorCodigo(codprod)

		if producto is None:
			print('No existe un producto con ese codigo.')
		else:
			cantidad = PedirInt('Ingrese la cantidad: ')
			if cantidad > producto.stock:
				print('No hay stock suficiente. Stock disponible: ' + str(producto.stock))
			else:
				print('\nSeleccione el tipo de promocion a aplicar para este producto:')
				print('1) Minorista (2x1 o 3x2)')
				print('2) Mayorista (43% desc. llevando 4 o mas unidades)')
				print('0) Ninguna promocion')
				
				tipo_promo = input('Ingrese una opcion: ')
				
				subtotal_original = producto.precio * cantidad
				descuento_promo = 0

				if tipo_promo == '1':
					print('1) Aplicar 2x1')
					print('2) Aplicar 3x2')
					opc_min = input('Ingrese opcion: ')
					if opc_min == '1':
						# 2x1 Se descuenta 1 por cada 2
						unidades_gratis = cantidad // 2
						descuento_promo = unidades_gratis * producto.precio
						print('Promo 2x1 aplicada.')
					elif opc_min == '2':
						# 3x2 Se descuenta 1 por cada 3
						unidades_gratis = cantidad // 3
						descuento_promo = unidades_gratis * producto.precio
						print('Promo 3x2 aplicada.')
				
				elif tipo_promo == '2':
					if cantidad >= 4:
						# 43% de descuento por unidad
						descuento_promo = subtotal_original * 0.43
						print('Promo Mayorista aplicada (43% de descuento).')
					else:
						print('No cumple con el requisito de 4 unidades para la promo mayorista. Se cobra precio regular.')

				subtotal_final = subtotal_original - descuento_promo
				items.append([producto.codprod, producto.nombre, cantidad, subtotal_final])
				print(producto.nombre + ' x' + str(cantidad) + ' -> Subtotal con promo: $' + str(subtotal_final))

		continuar = input('¿Desea agregar otro producto a la venta? (s/n): ')

	if len(items) == 0:
		print('No se cargo ningun producto.')
		return

	total = 0
	for item in items:
		total = total + item[3]

	print('\n-----------------------------------------')
	print('TOTAL FINAL DE LA VENTA (CON PROMOS): $' + str(round(total, 2)))
	print('-----------------------------------------')

	for item in items:
		codprod, nombre, cantidad, monto_final = item
		GuardarRegistroVenta(codprod, nombre, cantidad, monto_final)
