#Proyecto
#27/04/2018
#Josue Sagastume: 18173
#Mario Perdomo:18029
#Michele Benvenuto: 18232
import random
import pymongo
from FuncionesEstadisticas import ver_estadisticas
from FuncionesEstadisticas import agregar_estadisticas
from FuncionesEstadisticas import buscar_estadisticas
from FuncionesEstadisticas import modificar_estadisticas


opcion = 0
conexion = pymongo.MongoClient()
db = conexion.proyecto
#Parte del modulo
coleccion = db.articulos_guatemala
estadisticas = db.estadisticas
campos_a_mostrar = ["Titulo","Contenido"]


mensajeBienvenida="*******************************************************************************\nBIENVENIDO\n******************************************************************************* "
menuInicio="Elija una de las sigueintes opciones:\n 1)Leer articulo\n 2)Mini-Juegos\n 3)Comprobacion de lectura\n 4)Estadisticas\n 5)Salir"
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
       if(opcionInicio==2):
              #Mini-jUEGOS mar
              print("En desarrollo")
              print(mensajeBienvenida)
              print(menuInicio)
              opcionInicio=int(input())
       if(opcionInicio==3):
              #Comprenseion lectora mich
              print("En desarrollo")
              print(mensajeBienvenida)
              print(menuInicio)
              opcionInicio=int(input())
       if(opcionInicio==4):
              #Estadisticas Josue
               menuEstadisticas = "Que deseas hacer?\n1. Agregar un usuario\n2. Ver las estadisticas\n3. Salir"
               opcionE = 0
               while opcionE != 3:
                       print(menuEstadisticas)
                       opcionE = int(input())
                       if opcionE == 1:
                               nombre = input("Ingrese el nombre del usuario: ")
                               correctas = int(input("Ingrese el numero de aciertos que ha obtenido: "))
                               incorrectas = int(input("Ingrese el numero de malas que ha obtenido: "))
                               usuario = {"Nombre":nombre, "Correctas":correctas, "Incorrectas":incorrectas}
                               r = agregar_estadisticas(db, usuario)
                               if r == 1:
                                       print("Se han agregado los datos con exito")
                               else:
                                       print("No se agregaron los datos")
                       elif opcionE == 2:
                               resultado = ver_estadisticas(db)
                               for i in resultado:
                                       print(i)
                               print(menuEstadisticas)
                               opcionE = int(input()) 
                       elif opcionE == 3:
                               opcionE = 3
                       else:
                               print("La opcion que ingreso no se encuentra en la lista")
                               print(menuEstadisticas)
                               opcionE = int(input())
               print(mensajeBienvenida)
               print(menuInicio)
               opcionInicio=int(input())
       if(opcionInicio==5):
              opcionInicio = 5
