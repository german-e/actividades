


def tiempo(segundos):
	"""
	Función que reciba como parámetro una cantidad de
    segundos, y devuelva una tupla con la cantidad de segundos
    expresada en hh,mm,ss.
	arg:
		segundos: int que representa los segundos a ser convertido
	return:
		tupla de (hh,mm,ss)
	"""

	#Hora = 3600 segundos 
	#Minutos = 60 segundos

	hh = segundos//(3600)
	mm = (segundos-hh*3600) // 60
	ss = (segundos-hh*3600) - (mm*60)

	return (hh,mm,ss)

if __name__ == '__main__':
	seg = int( input ('Cantidad de Segundos: ') )
	h,m,s = tiempo(seg)
	print("{}:{}:{}".format(h,m,s))
