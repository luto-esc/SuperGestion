#importamos la libreria 'os' para limpiar la pantalla de la consola y verificar archivos
#importamos 'datetime' para obtener la fecha del sistema al registrar una venta
import os
import datetime
from registros import Producto, Descuento

def mostrarlogin(estado):
	usuario = str(input('Ingrese el usuario: '))
	contrasena = str(input('Ingrese la contraseña: '))

	if usuario == 'admin':
		if contrasena == 'admin123':
			estado = 'a'
		else:
			print('contraseña incorrecta')
	elif usuario == 'operador':
		if contrasena == 'operador123':
			estado = 'o'
		else:
			print('contraseña incorrecta')
	elif usuario == 'salir':
		estado = 's'
	else:
		print('usuario incorrecto')

	return estado

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
		caracter = 7
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
		'7) Promocion mayorista y minorista',
		'0) Salir')
	for i in menuprincial:
		print(i)

def PedirleOpcionUsuario(opcion):
	opcion = input('Ingrese una opcion: ')
	return opcion


#--- FIX: busqueda secuencial sobre la lista de opciones validas ---
#(reemplaza el uso de 'in' sobre tuplas, que no es un operador de la catedra)
def EsOpcionValida(opcion):
	opciones_validas = ['1', '2', '3', '4', '5', '6', '7', '0']
	i = 0
	total = len(opciones_validas)
	encontrado = False

	# ARR(opciones_validas) / MIENTRAS no se encuentre y no se llegue al FDS
	while i < total and encontrado == False:
		if opcion == opciones_validas[i]:
			encontrado = True
		i = i + 1

	return encontrado

def ValidadorOpcion(opcion):
	valido = EsOpcionValida(opcion)

	while valido == False:
		opcion = input('Ingresa una opcion valida: ')
		valido = EsOpcionValida(opcion)

	opcion = StraInt(opcion)
	return opcion


#--- FIX: validacion de datos numericos SIN try/except (no es estructura de catedra) ---
#se usa un esquema REPETIR...HASTA QUE sea valido

def EsEnteroValido(texto):
	texto = texto.strip()

	if texto == '':
		return False

	if texto[0] == '-':
		texto = texto[1:]

	if texto == '':
		return False

	return texto.isdigit()

def PedirInt(mensaje):
	valor_texto = input(mensaje)

	while EsEnteroValido(valor_texto) == False:
		print('Error: debe ingresar un numero entero. Intente nuevamente.')
		valor_texto = input(mensaje)

	valor = int(valor_texto)
	return valor

def EsRealValido(texto):
	texto = texto.strip()

	if texto == '':
		return False

	if texto[0] == '-':
		texto = texto[1:]

	partes = texto.split('.')

	if len(partes) == 1:
		return partes[0] != '' and partes[0].isdigit()
	elif len(partes) == 2:
		return partes[0].isdigit() and partes[1].isdigit()
	else:
		return False

def PedirFloat(mensaje):
	valor_texto = input(mensaje)

	while EsRealValido(valor_texto) == False:
		print('Error: debe ingresar un valor numerico. Intente nuevamente.')
		valor_texto = input(mensaje)

	valor = float(valor_texto)
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

#Esquema: cada PRODUCTO se graba como una SUBSECUENCIA IMPURA
#delimitada por la marca de fin '///' (no se conoce de antemano su fin,
#se reconoce por la marca, tal como vimos en Nocion de Secuencia)
def GuardarProducto(producto, archivo='archivo.txt'):
	# Abrir S/(Arch): abrimos el archivo para grabar (modo 'a' = agregar al final)
	f = open(archivo, 'a')
	f.write('///\n')
	f.write(producto.nombre + '\n')
	f.write(str(producto.precio) + '\n')
	f.write(str(producto.stock) + '\n')
	f.write(str(producto.codprod) + '\n')
	f.write('///\n')
	# CERRAR(Arch): fundamental, si no se hace se puede perder lo grabado en el buffer
	f.close()

#FIX: en vez de leer todo el archivo y hacer split('///') + comprension de listas,
#tratamos el archivo como una SECUENCIA de lineas y la recorremos con ARR/AVZ,
#reconociendo cada PRODUCTO como una subsecuencia delimitada por la marca '///'
def BuscarProductoPorCodigo(codigo, archivo='archivo.txt'):
	if os.path.exists(archivo) == False:
		return None

	f = open(archivo, 'r')
	lineas = f.readlines()
	f.close()

	total = len(lineas)
	i = 0
	productoEncontrado = None

	# ARR(lineas): arrancamos el recorrido de la secuencia
	while i < total and productoEncontrado is None:
		marca = lineas[i].strip()

		if marca == '///':
			# inicio de subsecuencia: AVZ por cada campo del producto
			i = i + 1
			nombre = lineas[i].strip()
			i = i + 1
			precio = lineas[i].strip()
			i = i + 1
			stock = lineas[i].strip()
			i = i + 1
			codprod = lineas[i].strip()
			i = i + 1
			i = i + 1   # saltamos la marca de FDS de cierre '///'

			if int(codprod) == codigo:
				productoEncontrado = Producto(nombre, float(precio), int(stock), int(codprod))
		else:
			i = i + 1

	return productoEncontrado


#--- descuentos ---
def CargarDescuento():
	coddesc = PedirInt('Ingrese el codigo del descuento: ')
	valor = PedirFloat('Ingrese el porcentaje del descuento (ej: 10 = 10%): ')
	descuento = Descuento(coddesc, valor)
	return descuento

#Mismo esquema que GuardarProducto: subsecuencia impura delimitada por '///'
def GuardarDescuento(descuento, archivo='descuentos.txt'):
	# Abrir S/(Arch)
	f = open(archivo, 'a')
	f.write('///\n')
	f.write(str(descuento.coddesc) + '\n')
	f.write(str(descuento.valor) + '\n')
	f.write('///\n')
	# CERRAR(Arch)
	f.close()

#Mismo esquema de recorrido ARR/AVZ que BuscarProductoPorCodigo
def BuscarDescuentoPorCodigo(codigo, archivo='descuentos.txt'):
	if os.path.exists(archivo) == False:
		return None

	f = open(archivo, 'r')
	lineas = f.readlines()
	f.close()

	total = len(lineas)
	i = 0
	descuentoEncontrado = None

	while i < total and descuentoEncontrado is None:
		marca = lineas[i].strip()

		if marca == '///':
			i = i + 1
			coddesc = lineas[i].strip()
			i = i + 1
			valor = lineas[i].strip()
			i = i + 1
			i = i + 1   # saltamos la marca de FDS de cierre '///'

			if int(coddesc) == codigo:
				descuentoEncontrado = Descuento(int(coddesc), float(valor))
		else:
			i = i + 1

	return descuentoEncontrado


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
	GenerarTicket(items, total, round(descuento_frac * 100, 2), total_final)

	#registramos cada producto vendido, con el % de descuento ya aplicado
	for item in items:
		codprod = item[0]
		nombre = item[1]
		cantidad = item[2]
		subtotal = item[3]
		monto_final = subtotal * (1 - descuento_frac)
		GuardarRegistroVenta(codprod, nombre, cantidad, monto_final)


#--- registro de ventas (para futuras estadisticas) ---
#Mismo esquema de subsecuencia impura, delimitada por '///'.
#Ahora la venta tiene un campo mas: la fecha en que se registro.
def GuardarRegistroVenta(codprod, nombre, cantidad, monto, archivo='ventas.txt'):
	hoy = datetime.date.today()

	# armamos la fecha en formato dd/mm/aaaa, con cero a la izquierda si hace falta
	dia = str(hoy.day)
	if hoy.day < 10:
		dia = '0' + dia

	mes = str(hoy.month)
	if hoy.month < 10:
		mes = '0' + mes

	fecha_texto = dia + '/' + mes + '/' + str(hoy.year)

	# Abrir S/(Arch)
	f = open(archivo, 'a')
	f.write('///\n')
	f.write(str(codprod) + '\n')
	f.write(nombre + '\n')
	f.write(str(cantidad) + '\n')
	f.write(str(monto) + '\n')
	f.write(fecha_texto + '\n')
	f.write('///\n')
	# CERRAR(Arch)
	f.close()

#Recorrido de TODA la secuencia (a diferencia de Buscar..PorCodigo, que corta
#al encontrar el primero). Cada venta es una subsecuencia delimitada por '///'.
#Devuelve una secuencia (lista) de ventas: [codprod, nombre, cantidad, monto, fecha]
def LeerVentas(archivo='ventas.txt'):
	if os.path.exists(archivo) == False:
		return []

	f = open(archivo, 'r')
	lineas = f.readlines()
	f.close()

	total = len(lineas)
	i = 0
	ventas = []

	# ARR(lineas): recorremos toda la secuencia, no nos detenemos al primer match
	while i < total:
		marca = lineas[i].strip()

		if marca == '///':
			i = i + 1
			codprod = lineas[i].strip()
			i = i + 1
			nombre = lineas[i].strip()
			i = i + 1
			cantidad = lineas[i].strip()
			i = i + 1
			monto = lineas[i].strip()
			i = i + 1
			fecha = lineas[i].strip()
			i = i + 1
			i = i + 1   # saltamos la marca de FDS de cierre '///'

			ventas.append([int(codprod), nombre, int(cantidad), float(monto), fecha])
		else:
			i = i + 1

	return ventas


#--- opcion 5: productos mas vendidos ---
def ProductosMasVendidos():
	ventas = LeerVentas()

	if len(ventas) == 0:
		print('Todavia no se registraron ventas.')
		return

	acumulado = []   # cada item: [codprod, nombre, cantidad_acumulada]

	# recorremos la secuencia de ventas y acumulamos por producto
	for venta in ventas:
		codprod_venta = venta[0]
		nombre_venta = venta[1]
		cantidad_venta = venta[2]

		# busqueda secuencial dentro de 'acumulado' (Cap. 9 - busqueda lineal)
		i = 0
		encontrado = False
		while i < len(acumulado) and encontrado == False:
			if acumulado[i][0] == codprod_venta:
				acumulado[i][2] = acumulado[i][2] + cantidad_venta
				encontrado = True
			i = i + 1

		if encontrado == False:
			acumulado.append([codprod_venta, nombre_venta, cantidad_venta])

	# ordenamos de mayor a menor cantidad vendida con burbuja (Cap. 9 - O(n^2))
	n = len(acumulado)
	i = 0
	while i < n - 1:
		j = 0
		while j < n - i - 1:
			if acumulado[j][2] < acumulado[j + 1][2]:
				aux = acumulado[j]
				acumulado[j] = acumulado[j + 1]
				acumulado[j + 1] = aux
			j = j + 1
		i = i + 1

	print('\n--- PRODUCTOS MAS VENDIDOS ---')
	for item in acumulado:
		print(item[1] + ' (codigo ' + str(item[0]) + '): ' + str(item[2]) + ' unidades vendidas')

	print('\nEl producto mas vendido es: ' + acumulado[0][1] + ' con ' + str(acumulado[0][2]) + ' unidades.')


#--- opcion 6: estadisticas de ventas ---
def EstadisticasDeVentas():
	ventas = LeerVentas()

	if len(ventas) == 0:
		print('Todavia no se registraron ventas.')
		return

	total_facturado = 0
	total_unidades = 0
	cantidad_ventas = len(ventas)

	# recorrido secuencial acumulando totales
	for venta in ventas:
		total_unidades = total_unidades + venta[2]
		total_facturado = total_facturado + venta[3]

	promedio_por_venta = total_facturado / cantidad_ventas

	#como GuardarRegistroVenta siempre agrega (append) al final del archivo,
	#el primer elemento de la secuencia es la venta mas antigua y el ultimo
	#es la mas reciente. No hace falta ordenar para saber esto.
	primera_fecha = ventas[0][4]
	ultima_fecha = ventas[len(ventas) - 1][4]

	print('\n--- ESTADISTICAS DE VENTAS ---')
	print('Cantidad de ventas registradas: ' + str(cantidad_ventas))
	print('Total de unidades vendidas: ' + str(total_unidades))
	print('Total facturado: $' + str(round(total_facturado, 2)))
	print('Promedio facturado por venta: $' + str(round(promedio_por_venta, 2)))
	print('Primera venta registrada: ' + primera_fecha)
	print('Ultima venta registrada: ' + ultima_fecha)


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
	GenerarTicket(items, total, 0, total)

	for item in items:
		codprod = item[0]
		nombre = item[1]
		cantidad = item[2]
		monto_final = item[3]
		GuardarRegistroVenta(codprod, nombre, cantidad, monto_final)

#--- generacion de tickets ---

#Llevamos un numero correlativo de tiket en un archivo aparte.
#Es una SECUENCIA de un solo valor: lo leemos, lo usamos, y grabamos el siguiente.
def ObtenerNumeroTicket(archivo='numeroticket.txt'):
	if os.path.exists(archivo) == False:
		numero = 1
	else:
		f = open(archivo, 'r')
		numero = int(f.read().strip())
		f.close()

	# Abrir S/(Arch): grabamos el proximo numero a usar la siguiente vez
	f = open(archivo, 'w')
	f.write(str(numero + 1))
	f.close()

	return numero

#Arma la fecha y hora actual en formato dd/mm/aaaa hh:mm
def ObtenerFechaHoraTexto():
	hoy = datetime.datetime.now()

	dia = str(hoy.day)
	if hoy.day < 10:
		dia = '0' + dia

	mes = str(hoy.month)
	if hoy.month < 10:
		mes = '0' + mes

	hora = str(hoy.hour)
	if hoy.hour < 10:
		hora = '0' + hora

	minuto = str(hoy.minute)
	if hoy.minute < 10:
		minuto = '0' + minuto

	return dia + '/' + mes + '/' + str(hoy.year) + ' ' + hora + ':' + minuto

#Genera un archivo .txt con el tiket de la compra.
#items: lista de [codprod, nombre, cantidad, subtotal]
#subtotal: suma de todos los items sin descuento
#descuentoPorc: porcentaje de descuento aplicado (0 si no hubo)
#totalFinal: total a pagar ya con el descuento aplicado
def GenerarTicket(items, subtotal, descuentoPorc, totalFinal):
	numero = ObtenerNumeroTicket()
	numeroTexto = str(numero).zfill(4)
	archivo = 'ticket_' + numeroTexto + '.txt'
	fechaTexto = ObtenerFechaHoraTexto()

	# Abrir S/(Arch)
	f = open(archivo, 'w')
	f.write('==========================================\n')
	f.write('             SUPERGESTION\n')
	f.write('           Ticket de compra\n')
	f.write('==========================================\n')
	f.write('Ticket Nro: ' + numeroTexto + '\n')
	f.write('Fecha: ' + fechaTexto + '\n')
	f.write('------------------------------------------\n')
	f.write('Producto             Cant.     Importe\n')
	f.write('------------------------------------------\n')

	for item in items:
		nombre = item[1]
		cantidad = item[2]
		importe = item[3]
		linea = nombre.ljust(20) + 'x' + str(cantidad).rjust(3) + '   $' + str(round(importe, 2)).rjust(8)
		f.write(linea + '\n')

	f.write('------------------------------------------\n')
	f.write('Subtotal:'.ljust(30) + '$' + str(round(subtotal, 2)).rjust(8) + '\n')

	if descuentoPorc > 0:
		f.write('Descuento aplicado:'.ljust(30) + str(descuentoPorc) + '%\n')

	f.write('TOTAL:'.ljust(30) + '$' + str(round(totalFinal, 2)).rjust(8) + '\n')
	f.write('==========================================\n')
	f.write('         Gracias por su compra!\n')
	f.write('==========================================\n')
	# CERRAR(Arch)
	f.close()

	print('\nTiket generado correctamente: ' + archivo)
