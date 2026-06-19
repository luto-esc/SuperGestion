#importamos la libreria 'os' para limpiar la pantalla de la consola
import os

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
	elif caracter == '8':
		caracter = 8
	elif caracter == '9':
		caracter = 9
	elif caracter == '0':
		caracter = 0

	return caracter

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
	opcionesInt = (1,2,3,4,5,6,7,8,9,0)
	opcionesStr = ('1','2','3','4','5','6','7','8','9','0')
	
	#si opcion en opcionesStr
	if opcion in opcionesStr:
		opcion = StraInt(opcion)
		if opcion in opcionesInt:
			bandera = True
	#sino
	else:
		bandera = False

	#mientras bandera = F hacer
	while bandera == False:
		#esc('ingrese una opcion valida: ') leer(opcion)
		opcion = input('Ingresa una opcion valida: ')
		#si opcion en opcinesStr
		if opcion in opcionesStr:
			opcion = StraInt(opcion)
			if opcion in opcionesInt:
				bandera = True

	if bandera == True:
		return opcion