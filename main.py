#de funciones.py importamos las funciones a utilizar
from funciones import (LimpiarConsola, MostrarMenuPrincipal, PedirleOpcionUsuario,
	ValidadorOpcion, CargarProducto, GuardarProducto, CargarDescuento,
	GuardarDescuento, BuscarProductoPorCodigo, CalcularTotal, PedirInt, Login,
	CalcularPromociones, ProductosMasVendidos, EstadisticasDeVentas)

LimpiarConsola()
print('BIENVENIDO A GESTIONSUPER')

opcion = 9
ejecucion = True
estado = 'n'

while ejecucion == True:
	print('ingrese _salir_ para terminar el programa')

	estado = Login(estado)

	if estado == 'o' or estado == 'a':

		LimpiarConsola()

		MostrarMenuPrincipal()

		while opcion != 0:
			opcion = PedirleOpcionUsuario(opcion)
			opcion = ValidadorOpcion(opcion)

			#si la opcion que recibe es 1: cargar producto
			if opcion == 1:
				if estado == 'a':
					finalizar = 1
					while finalizar == 1:
						producto = CargarProducto()
						GuardarProducto(producto)
						print('Producto guardado correctamente.')

						print('\n¿Desea cargar otro producto?')
						print('1) Si')
						print('0) No')
						finalizar = PedirleOpcionUsuario(finalizar)
						finalizar = ValidadorOpcion(finalizar)
				elif estado == 'o':
					print('No tiene permiso de administrador')

			#Si la opcion que recibe es 2: cargar descuento
			elif opcion == 2:
				if estado == 'a':
					finalizar = 1
					while finalizar == 1:
						descuento = CargarDescuento()
						GuardarDescuento(descuento)
						print('Descuento guardado correctamente.')

						print('\n¿Desea cargar otro descuento?')
						print('1) Si')
						print('0) No')
						finalizar = PedirleOpcionUsuario(finalizar)
						finalizar = ValidadorOpcion(finalizar)
				elif estado == 'o':
					print('No tinee permisos de administrador')
			elif opcion == 3:
				codprod = PedirInt('Ingrese el codigo del producto a buscar: ')
				producto = BuscarProductoPorCodigo(codprod)
				if producto is None:
					print('No existe un producto con ese codigo.')
				else:
					print('Nombre: ' + producto.nombre)
					print('Precio: $' + str(producto.precio))
					print('Stock: ' + str(producto.stock))
					print('Codigo: ' + str(producto.codprod))

			#si la opcion que recibe es 4: calcular total de venta
			elif opcion == 4:
				CalcularTotal()

			elif opcion == 5:
				ProductosMasVendidos()

			elif opcion == 6:
				EstadisticasDeVentas()

			#FIX: la opcion 7 ya estaba en el menu pero nunca se llamaba a la funcion
			elif opcion == 7:
				CalcularPromociones()

	elif estado == 's':
		#FIX: era "ejecucion == False" (comparacion, no hacia nada). Debe ser asignacion.
		ejecucion = False

LimpiarConsola()
print('Gracias por elegir att:GESTIONSUPER!')
