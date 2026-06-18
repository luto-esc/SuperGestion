#importamos la libreria 'os' para limpiar la pantalla de la consola
import os

#limpia la consola dependiendo si el os es windows o linux/mac
def LimpiarConsola():
	#si el usuario tiene windows (os.name = nt),entonces ejecutamos el comando 'cls' 
	if os.name == "nt":
		os.system("cls")
	#sino en cualquier otro caso ejecutamos el comando 'clear'
	else:
		os.system("clear")

def MostrarMenuPrincipal():
	#lista en la que guardamos un conjunto de caracteres
	menuprincial = (
		'1) Cargar producto',
		'2) Buscar producto',
		'3) Promociones activas',
		'4) Productos mas vendidos',
		'5) Estadisticas de ventas',
		'0) Salir')
	#para cada i en la lista, lo imprime o escribe por pantalla
	for i in menuprincial:
		print(i)

#funcion que le pide al usuaraio una opcion y retorna un entero, lo que el usuario ingreso
def PedirleOpcionUsuario(opcion):
	#pide un valor, lo transfroma en entero
	opcion = input('Ingrese una opcion: ')
	#retorna ese valor
	return opcion

def ValidadorOpcion(opcion):
	bandera = True
	opciones = (1,2,3,4,5,6,7,8,9,0)
	if opcion in opciones:
		return opcion
	else:
		bandera = False

	while bandera == False:
		opcion = input('Ingresa una opcion valida: ')
		if opcion in opciones:
			bandera = True