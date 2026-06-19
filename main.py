#de funciones.py importamos las funciones a utilizar
from funciones import LimpiarConsola, MostrarMenuPrincipal, PedirleOpcionUsuario, ValidadorOpcion
from registros import Producto

#limpiamos la consola antes de iniciar el programa
LimpiarConsola()

#titulo del programa
print('BIENVENIDO A GESTIONSUPER')

#establecemos la variable para el mientras que controla, que opcion tomara el usuario
#de este modo utilizaremos una estrucutra post-test, ya que la opcion nunca sera 0 en un inicio
#por lo tanto siempre se mostrara al menos una vez
opcion = 9

#la fucion muestra por pantalla las opciones
MostrarMenuPrincipal()

#Mientras opcion sea distinto de 0
while opcion != 0:
	#a la variable opcion le asignamos la funcion
	opcion = PedirleOpcionUsuario(opcion)

	opcion = ValidadorOpcion(opcion)

	#si la opcion que recibe es 1
	if opcion == 1:
		finalizar = 1
		while finalizar == 1:
			nombre = input('Ingrese el nombre del producto: ')
			precio = float(input('ingrese el precio del producto: '))
			stock = int(input('ingrese el nro de stock del producto: '))
			codprod = int(input('ingrese el codigo del producto: '))
			producto = Producto(nombre, precio, stock, codprod)
			#asignamos una variable para el archivo, este estara en modo READ
			with open('archivo.txt', 'a') as archivo:
				#agregar contendio al archivo
				archivo = archivo.write('\n',producto.nombre)
				archivo = archivo.write('\n',producto.precio)
				archivo = archivo.write('\n',producto.stock)
				archivo = archivo.write('\n',producto.codprod)
				archivo = archivo.write('\n','///')
			finaliar = PedirleOpcionUsuario(finalizar)
			finalizar = ValidadorOpcion(finalizar)

		with open('archivo.txt', 'r') as archivo:
			contenido = archivo.read()
			print(contenido)
	elif opcion == 2:
		print('aca buscariamos un producto')
	elif opcion == 3:
		print('aca veriamos promociones activas')
	elif opcion == 4:
		print('aca veriamos productos mas vendidos')
	elif opcion == 5:
		print('aca veriamos las estadisticas de ventas')


LimpiarConsola()

#mensaje final una vez salido del bucle
print('Gracias por elegir att:GESTIONSUPER!')