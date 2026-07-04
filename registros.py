#dataclasses es un modulo de la biblioteca estandar de python, su objetivo es facilitar la creacion de clases
#de dataclasses importamos la funcion/decorador dataclass
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
	#stock = entero          <-- FIX: antes se llamaba "nrostock" y rompia con producto.stock
	stock: int
	#codprod = entero
	codprod: int


#Descuento = Registro
@dataclass
class Descuento:
	#coddesc = entero (codigo del descuento)
	coddesc: int
	#valor = real (porcentaje a descontar, ej: 10 = 10%)
	valor: float
