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




