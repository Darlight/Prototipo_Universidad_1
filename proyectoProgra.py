#Proyecto
#27/04/2018
#Josue Sagastume: 18173
#Mario Perdomo:18029
#Michele Benvenuto: 18232
import random
import pymongo
from FuncionesEstadisticas import *
from funcionesAhorcado import *
from palabras import lista_de_palabras
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
                      Menu de Articulos
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
                            print("Porfavor ingrese las opciones del menu")

              print(mensajeBienvenida)
              print(menuInicio)
              opcionInicio=int(input())
       if(opcionInicio==2):
              #Mini-jUEGOS 
              opcionJuegos = 0
              while opcionJuegos != 4:
                opcionJuegos = int(input("""
                  Menu de Juegos
*************************************************************************************************
1. Ahorcado
2. Palabras encadenadas
3. Pictionary
4. Salir
*************************************************************************************************
"""))
                if opcionJuegos == 1:
                  print ("Bienvenido al Ahorcado \n")
                  print("Simplemente adivine la palabra, tiene 7 oportunidades para no ser Ahorcado\n")
                  desea_jugar = True

                  # usar "letra" in "palabra" para que el juego funcione.
                  # crear el stickman con: "O", "I", "/", "\" y el palo.
                  while desea_jugar == True:
                    #Escoge una palabra aleatorio por la lista que proporciona el modulo
                    palabra_elegida = random.choice(lista_de_palabras)
                    oportunidades = 0
                    ganador = 0
                    #La palabra que es elegida la convierto como una lista para
                    #clasificar cada letra en una posicion de la lista
                    #ejemplo: list("palabra") ==> ["p","a","l","a","b","r","a"]
                    letras_separadas = list(palabra_elegida)
                    #las letras que proporciona la lista se convierten en guiones
                    for guion in range(len(letras_separadas)):
                      letras_separadas[guion] = "_"
                    while oportunidades != 7:
                      #El estado es falso, quiere decir que no ha perdido vidas
                      estado = False
                      #la funcion join convierte los elementos de la lista
                      #en string, separado por el espacio anterior ya escrito
                      #ejemplo: [a,b,c] entonces " ".join([a,b,c]) ==> a b c en print
                      print(" ".join(letras_separadas))
                      #Solucion temporal que se cambiara para el producto final
                      print("Porfavor no ingrese ñ o vocales con tildes. El programa todavia no los reconoce.")
                      letra_ingresada = input("Ingrese la letra deseada: ")
                      #Si la letra ingresada se encuentra en la palabra
                      #escogia aleatoriamente entonces se intercambia el guion
                      #por la la letra
                      if letra_ingresada in palabra_elegida:
                      #Extra: Crear una lista donde todas las letras ingresadas
                      #por el usuario se muestren en pantalla
                        for i in range(len(palabra_elegida)):
                          if palabra_elegida[i] == letra_ingresada:
                            letras_separadas[i] = letra_ingresada
                            ganador += 1
                      else:
                        #Si falla el estado es true, definiendo que perdio una vida
                        estado = True
                        oportunidades += 1
                        #Se imprime el dibujo
                        print(dibujo(estado,oportunidades))
                        vueltas = 7 - oportunidades
                        print("Numero de oportunidades = " + str(vueltas))
                      #Si el acumalor de ganador vale lo mismo que la letra
                      #el jugador gana
                      if ganador == len(palabra_elegida):
                        oportunidades = 7
                        print("Gano! la palabra correcta es: " + palabra_elegida)
                      #De lo contrario, perdio el juego y se muestra la palabra
                      elif oportunidades == 7 and ganador!= len(palabra_elegida):
                        print ("usted ha perdido, la palabra correcta era: ", palabra_elegida)
                    #Se pregunta si desea jugar otra vez
                    respuesta = input("Desea jugar de nuevo? : si o no ")
                    if respuesta == "si":
                      desea_jugar = True
                    else:
                      desea_jugar = False

                elif opcionJuegos == 2:
                  print("En desarrollo \n")
                elif opcionJuegos == 3:
                  print("En desarrollo \n")
                else:
                  print("Por favor ingrese las opciones del menu. \n")
                
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
