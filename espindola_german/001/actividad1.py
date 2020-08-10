import os

def ventas():
	"""
	Programa que pregunte al usuario, el precio del producto y la cantidad de unidades vendidas.
    Informar el total de ventas.
    arg:
    	None
    
	"""

	print("***************************")
	print("VENTAS POR ARTICULOS")
	print("**************************")
	producto = []

	total_ventas = 0

	seguir = True
	encontrado = False

	while seguir:
		if os.name == "posix":
			os.system ("clear")
		elif os.name == "nt" or os.name == "dos":
   			os.system ("cls")

		print(producto)
		try:
			descripcion = input("Producto: ")
			precio = float(input("precio $: "))	
			cant = int(input("Cantidad: "))

			tupla_productos = (descripcion,precio, cant) 
			producto.append(tupla_productos)

			#calculos
			esta_venta = precio * cant
			total_ventas += esta_venta  #Acumulador: Guarda todas las ventas realizadas

			bandera = input("Cargar otro (S / N)")

			if bandera.lower() == "n":
				seguir = False


		except ValueError as e:
			print("Error en el ingreso de datos, ingrese nuevamente...")
			
			input()


		
		


	#Informe
	print("-----------------------".center(30))
	print("Detalle de venta diaria".center(30))
	print("-----------------------".center(30))
	print("Producto                Precio    Cantidad	Subtotal")
	print("*****************************************************")
	
	for item in producto:
		subtotal = item[2]*item[1]
		
		print("{0:<25}{1:<10}{2:<10}  {3:<8}".format(item[0],item[1],item[2], subtotal)

	print()
	print("-------------------------------")
	print("Total de ventas: ", total_ventas)
	print("-------------------------------")


if __name__ == '__main__':
	ventas()




