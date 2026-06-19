#dateclasses es un modulo de la biblioteca estandar de python, su objetivo es facilitar la creacion de clases 
#de dateclasesses importamos la funcion/decorador dateclass
from dataclasses import dataclass

#dataclass nos sirve para sustituir todo lo que vendriamos a tener que declarar para la clase que vamos a crear
#sea valida, osea sustituye los metodos principales
# = Producto = Registro
@dataclass
class Producto:
	#nombre = alfanumerico
	nombre: str
	#precio = real
	precio: float
	#nrostock = entero
	nrostock: int
	#codprod = entero
	codprod: int
