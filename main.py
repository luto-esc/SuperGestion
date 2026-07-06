#de funciones.py importamos las funciones a utilizar
from funciones import (LimpiarConsola, MostrarMenuPrincipal, PedirleOpcionUsuario,
	ValidadorOpcion, CargarProducto, GuardarProducto, CargarDescuento,
	GuardarDescuento, BuscarProductoPorCodigo, CalcularTotal, PedirInt, mostrarlogin, CalcularPromociones)

LimpiarConsola()
print('BIENVENIDO A GESTIONSUPER')

opcion = 9
ejecucion = True
estado = 'n'

while ejecucion == True:

	estado = mostrarlogin(estado)

	if estado == 'o' or 'a':

		MostrarMenuPrincipal()

		while opcion != 0:
			opcion = PedirleOpcionUsuario(opcion)
			opcion = ValidadorOpcion(opcion)

			#si la opcion que recibe es 1: cargar producto
			if opcion == 1:
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

			#si la opcion que recibe es 2: cargar descuento (NUEVO)
			elif opcion == 2:
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

			#si la opcion que recibe es 4: calcular total de venta (NUEVO)
			elif opcion == 4:
				CalcularTotal()

			elif opcion == 5:
				print('Pendiente: productos mas vendidos')

			elif opcion == 6:
				print('Pendiente: estadisticas de ventas')
				
			elif opcion == 7:
				CalcularPromociones()
				
            elif opcion != 0:
				print('\n')
				MostrarMenuPrincipal()

LimpiarConsola()
print('Gracias por elegir att:GESTIONSUPER!')
