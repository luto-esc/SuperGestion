#de funciones.py importamos las funciones a utilizar
from funciones import (LimpiarConsola, MostrarMenuPrincipal, PedirleOpcionUsuario,
	ValidadorOpcion, CargarProducto, GuardarProducto, BuscarProductoPorCodigo, PedirInt)

LimpiarConsola()
print('BIENVENIDO A GESTIONSUPER')

opcion = 9
MostrarMenuPrincipal()

while opcion != 0:
	opcion = PedirleOpcionUsuario(opcion)
	opcion = ValidadorOpcion(opcion)

	#si la opcion que recibe es 1: cargar producto
	if opcion == 1:
		#FIX: "finaliar" -> "finalizar", antes rompia el control del bucle
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

	elif opcion == 2:
		codprod = PedirInt('Ingrese el codigo del producto a buscar: ')
		producto = BuscarProductoPorCodigo(codprod)
		if producto is None:
			print('No existe un producto con ese codigo.')
		else:
			print('Nombre: ' + producto.nombre)
			print('Precio: $' + str(producto.precio))
			print('Stock: ' + str(producto.stock))
			print('Codigo: ' + str(producto.codprod))

	elif opcion == 3:
		print('Pendiente: calculo de total de venta')

	elif opcion == 4:
		print('Pendiente: productos mas vendidos')

	elif opcion == 5:
		print('Pendiente: estadisticas de ventas')

	if opcion != 0:
		print('\n')
		MostrarMenuPrincipal()

LimpiarConsola()
print('Gracias por elegir att:GESTIONSUPER!')
