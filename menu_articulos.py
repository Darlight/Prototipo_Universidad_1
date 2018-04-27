#menu_articulos.py
#Fecha de creacion: 27/04/2018
#Michele Benvenutoo 18232
#Mario Perdomo 18029 
#Josue Sagastume 18173
#Funcion: menu de los articulos
import random
import pymongo
opcion = 0
conexion = pymongo.MongoClient()
db = conexion.proyecto
#Parte del modulo
coleccion = db.articulos_guatemala

#for articulo in guatemala_lista_de_articulos:
 # coleccion.insert(articulo)

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
        resultado = coleccion.find({"Titulo":"TABACO FRENA EL DESARROLLO en Guatemala"},{"_id": 0, "Titulo": 1, "Contenido": 1})
        for i in resultado:
          print(i)
      elif opcion2 == 2:
        resultado = coleccion.find({"Titulo":"IMPULSAN MEJORES CONTROLES"},{"_id": 0, "Titulo": 1, "Contenido": 1})
        for i in resultado:
          print(i)
      else:
        print("#")
  elif opcion == 2:
    print("#")
  elif opcion == 3:
    print("#")
  elif opcion == 4:
    print("#")
  elif opcion == 5:
    print("#")
  else:
    print("LEA ESTUPIDO")

