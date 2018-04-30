#Proyecto
#27/04/2018
#Josue Sagastume: 18173
#Mario Perdomo:18029
#Michele Benvenuto: 18232
import random
import pymongo


opcion = 0
conexion = pymongo.MongoClient()
db = conexion.proyecto
#Parte del modulo
coleccion = db.articulos_guatemala
campos_a_mostrar = ["Titulo","Contenido"]

mensajeBienvenida="*******************************************************************************\nBIENVENIDO\n******************************************************************************* "
menuInicio="Elija una de las sigueintes opciones:\n 1)Leer articulo\n 2)@\n 3)Comprobacion de lectura\n 4)@\n 5)Salir"
print(mensajeBienvenida)
print(menuInicio)
opcionInicio=int(input())
while(opcionInicio !=5):
	if(opcionInicio==1):
		#Menu de mario
		opcion = 0
		while opcion != 5:
			opcion = int(input("""
*************************************************************************************************
1. Articulos relacionados al pais de Guatemala
2. #
3. #
4. #
5. Salir
*************************************************************************************************
				"""))
			if opcion == 1:
				opcion2 = 0

				while  opcion2 != 3:
					opcion2 = int(input("""
1. Tabaco frena el desarrollo de Guatemala
2. Impulsan mejores controles
3. salir
"""))
					if opcion2 == 1:
						#Resultado consigue el articulo con titulo y contenido sin el id para que sea mas presentable
						resultado = coleccion.find_one({"Titulo":"Tabaco frena el desarrollo en Guatemala"},{"_id": 0, "Titulo": 1, "Contenido": 1})
						for campo in campos_a_mostrar:
							print(str(resultado[campo]) + "\n")
					elif opcion2 == 2:
						resultado = coleccion.find_one({"Titulo":"Impulsan mejores controles"},{"_id": 0, "Titulo": 1, "Contenido": 1})
						for campo in campos_a_mostrar:
							print(str(resultado[campo]) + "\n")
					else:
						print("En desarrollo...")
			elif opcion == 2:
				print("En desarrollo")
			elif opcion == 3:
				print("En desarrollo")
			elif opcion == 4:
				print("En desarrollo")
			elif opcion == 5:
				opcion = 5
			else:
				print("LEA ESTUPIDO")
		print(mensajeBienvenida)
		print(menuInicio)
		opcionInicio=int(input())