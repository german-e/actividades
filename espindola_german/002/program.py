from Actividad2 import segundos_en_hhmmss, hhmmss_en_segundos, minutos_en_hhmmss

def main():
	
	print("My Time program")
	print("***************")
	print("\nPasar segundos a horas, minutos y segundos: ")
	seg = int( input ('Cantidad de Segundos: ') )
	h,m,s = segundos_en_hhmmss(seg)  #segundos_en-hhmmss devuelve tupla (h,m,s)

	print("{}:{}:{}".format(h,m,s))

	#Convertir segundos en horas, minutos y segundos

	print("--------------------")
	print("\nPasar a segundos: ")
	
	# Convertir una cantidad de minutos en horas, min, y seg.
	minutos = int(input("Minutos -> "))
	
	print("---------------------------")
	minutos_en_segundos = hhmmss_en_segundos(minutos=minutos)
	hh,mm,ss = segundos_en_hhmmss(minutos_en_segundos)
	print("{}:{}:{}".format(hh,mm,ss))
	

	#Ingresar una cadena de caracteres y mostrar la hora	

	hhmmss = input("Escribir tiempo en formato hh:mm:ss ")
	horas,minut,segundos = hhmmss.split(':')

	print("---------------------------")
	visulizar_hora(int(horas),int(minut),int(segundos))

		
	print("-----------------------------F I N-------------------------------")
		
	
		

def visulizar_hora(h,m,s):

	print("Horas: ", h)
	print("Minutos: ",m)
	print("Segundos: ",s)
	print("Equivale a: {} segundos ".format(hhmmss_en_segundos(h,m,s)))




if __name__ == '__main__':
	main()
