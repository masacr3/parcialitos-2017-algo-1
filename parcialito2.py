#Leonel R.
#Facultad de Ingenieria Universidad de Buenos Aires

#1.
def juntada_amigos(amigos):
	""" retorna un diccionario de que dias pueden juntarse 
		 dicc = {1 .. 31 : numero, ...}

		pre: amigos es un diccionario se asume que amigos tendra el siguiente formato 
			amigos = {"nombre":lista, ..}  la [lista] puede contener los dias que no pueden juntarse en formato numerico del 1 al 31
	"""
	if amigos == {}:
		return

	dias = {}

	for fecha in amigos.values():

		for dia in range(1,32):

			if dia not in fecha:
				dias[dia] = dias.get(dia,0) + 1

	return dias

#2.

class LIBRO:
	def __init__(self,nombre,autor):
		self.nombre = nombre
		self.autor = autor

class BIBLIOTECA:
	def __init__(self,max_libros):
		self.capacidad_maxima = max_libros
		self.len = 0 
		self.libros = []
	
	def agregar(self,libro):
		#Pregunta si puedo guardad un libro
		if not ( self.len < self.capacidad_maxima ):
			return 
		
		self.libros.append(libro)
		self.len += 1
	
	def sacar_libro(self,nombre_libro):
		for i,libro in enumerate(self.libros):
			if libro.nombre == nombre_libro:
				return self.libro.pop(i).nombre
		return "libro no se encuentra en la biblioteca"
	
	def obtener_libros_autor(self,autor):
		return [ libro.nombre for libro in self.libros if libro.autor == autor ]
		
		


