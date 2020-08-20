


def segundos_en_hhmmss(segundos:int):
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



def hhmmss_en_segundos(horas=0,minutos=0,segundos=0):
	"""
	Función que reciba como parámetros cantidades de horas, minutos y/o segundos. 
	Retorna la suma de estos expresanda en segundos. 
	arg:
		horas: numero entero que representa la hora 
		minutos:número entero 
		segundos:número entero
	return:
		Entero = Entero que representa los segundos
	"""
	seg_horas = horas * 3600 #pasa horas a segundos -> 1 h = 3600 seg 
	seg_min = minutos * 60   #pasa minutos a segundos -> 1m = 60 seg. 
	seg = segundos

	return seg_horas + seg_min + seg




if __name__ == '__main__':
	print(minutos_en_hhmmss(121))
	
