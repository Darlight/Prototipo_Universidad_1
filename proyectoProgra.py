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
from time import sleep
from funcionesEncadenaPalabras import *
from funcionesOrdenarImagen import *
opcion = 0
conexion = pymongo.MongoClient()
db = conexion.proyecto
#Parte del modulo
coleccion = db.articulos_guatemala
estadisticas = db.estadisticas
campos_a_mostrar = ["Titulo","Contenido"]


mensajeBienvenida="*******************************************************************************\nBIENVENIDO\n******************************************************************************* "
menuInicio="Elija una de las sigueintes opciones:\n 1)Leer articulo\n 2)Mini-Juegos\n 3)Comprobacion de lectura\n 4)Ver estadisticas\n 5)Salir"
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
*******************************************************************************
1. Articulos relacionados al pais de Guatemala
2. #
3. #
4. #
5. Salir
*******************************************************************************
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
                                                 print(str(resultado[campo]))
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
*******************************************************************************
1. Ahorcado
2. Palabras encadenadas
3. Reordenamiento de Imagenes
4. Salir
*******************************************************************************
"""))
                if opcionJuegos == 1:
                  print("Bienvenido al Ahorcado \n")
                  print("Simplemente adivine la palabra, tiene 7 oportunidades para no ser Ahorcado\n")
                  desea_jugar = True
                  # usar "letra" in "palabra" para que el juego funcione.
                  # crear el stickman con: "O", "I", "/", "\" y el palo.
                  while desea_jugar == True:
                    #Escoge una palabra aleatorio por la lista que proporciona el modulo
                    palabra_elegida = random.choice(lista_de_palabras)
                    oportunidades = 0
                    #Extra: Crear una lista donde todas las letras ingresadas
                    #por el usuario se muestren en pantalla
                    letras_usadas = []
                    #las letras que proporciona la lista se convierten en guiones
                    palabra_en_guiones = palabra_Enguiones(palabra_elegida)
                    #El estado es falso, quiere decir que no ha perdido vidas
                    while oportunidades != 7:
                      estado = False
                      #la funcion join convierte los elementos de la lista
                      #en string, separado por el espacio anterior ya escrito
                      #ejemplo: [a,b,c] entonces " ".join([a,b,c]) ==> a b c en print
                      print(" ".join(palabra_en_guiones))
                      print("\n")
                      print(mostrar_LetrasUsadas(letras_usadas))
                      print("\n")
                      letra_ingresada = input("Ingrese la letra deseada: ")
                      #Si la letra ingresada se encuentra en la palabra
                      #escogia aleatoriamente entonces se intercambia el guion
                      #por la la letra
                      if letra_ingresada in palabra_elegida:
                        for i in range(len(palabra_elegida)):
                          #Se convierte el str en un numero
                          if ord(palabra_elegida[i]) == ord(letra_ingresada):
                            palabra_en_guiones[i] = letra_ingresada
                        letras_usadas.append(letra_ingresada)
                      else:
                        #Si falla el estado es true, definiendo que perdio una vida
                        estado = True
                        oportunidades += 1
                        #Se imprime el dibujo
                        print(dibujo(estado,oportunidades))
                        vueltas = 7 - oportunidades
                        print("Numero de oportunidades = " + str(vueltas))
                        letras_usadas.append(letra_ingresada)
                      #Nueva forma de ganar
                      if ("".join(palabra_en_guiones)) == palabra_elegida:
                        oportunidades = 7
<<<<<<< HEAD
#<<<<<<< HEAD
                        print("Gano! la palabra correcta es: " + palabra_elegida)

                        correctas = 1
                        incorrectas = 0
                        usuario = input("Ingrese su nombre: ")
                        punteo = {"Nombre": usuario, "Correctas":correctas, "Incorrectas":incorrectas}
                        r = agregar_estadisticas(db, usuario, punteo, correctas, incorrectas)

                        if r == 1:
                               print("Las puntuaciones se agregaron con exito")
                               print(" ")
                               sleep(1)
                        else:
                               print("Las puntuaciones no se agregaron")
                               print(" ")
                               sleep(1)
                               
                      #De lo contrario, perdio el juego y se muestra la palabra
                      elif oportunidades == 7 and ganador!= len(palabra_elegida):
                        print ("usted ha perdido, la palabra correcta era: ", palabra_elegida)
                        
                        correctas = 0
                        incorrectas = 1
                        usuario = input("Ingrese su nombre: ")
                        punteo = {"Nombre": usuario, "Correctas":correctas, "Incorrectas":incorrectas}
                        r = agregar_estadisticas(db, usuario, punteo, correctas, incorrectas)

                        if r == 1:
                               print("Las puntuaciones se agregaron con exito")
                               print(" ")
                               sleep(1)
                        else:
                               print("Las puntuaciones no se agregaron")
                               print(" ")
                               sleep(1)
                        
                    #Se pregunta si desea jugar otra vez
#=======
                        print("Gano! la palabra correcta fue: " + palabra_elegida)
                        #De lo contrario, perdio el juego y se muestra la palabra
                      elif oportunidades == 7 and ("".join(palabra_en_guiones)) != palabra_elegida:
                        print ("usted ha perdido, la palabra correcta era: ", palabra_elegida)
                        #Se pregunta si desea jugar otra vez
#>>>>>>> d9dbc92bdf4c46710d99fa6e2ebdb85be3a57f2e
=======
                        print("Gano! la palabra correcta fue: " + palabra_elegida)
                        #De lo contrario, perdio el juego y se muestra la palabra
                      elif oportunidades == 7 and ("".join(palabra_en_guiones)) != palabra_elegida:
                        print ("usted ha perdido, la palabra correcta era: ", palabra_elegida)
                        #Se pregunta si desea jugar otra vez
>>>>>>> d9dbc92bdf4c46710d99fa6e2ebdb85be3a57f2e
                    respuesta = input("Desea jugar de nuevo? : si o no ")
                    if respuesta == "si":
                      desea_jugar = True
                      letras_usadas = []
                    else:
                      desea_jugar = False

                elif opcionJuegos == 2:
                  print("Bienvenido al Encadena Palabras! \n")
                  print("Debera generar una nueva palabra utilizando la última letra de la palabra proporcionada. \n")
                  print("Tendrá 3 oportunidades\n")
                  desea_jugar = True
                  while  desea_jugar == True:
                    oportunidades = 3
                    puntaje = 0
                    palabras_usadas = []
                    while oportunidades != 0:
                      palabra_random = (random.choice(lista_palabras)).lower()
                      print("Palabra escogida: " + palabra_random + "\n")
                      nueva_palabra = (input("Ingrese la nueva palabra tomando en cuenta la última letra: \n").lower())
                      ultima_letra = (palabra_random[-1:])
                      if ord(nueva_palabra[0]) == ord(ultima_letra):
                        if nueva_palabra in palabras_usadas:
                          oportunidades -= 1
                          print("Ya uso esa palabra, pierde un punto. \n")
                          print("Vidas: " + str(oportunidades))
                          print("Palabras usadas: " + (", ".join(palabras_usadas)))
                        else:
                          palabras_usadas.append(nueva_palabra) 
                          puntaje += 1
                          print("Lo logro! \n")
                          print("Vidas: " + str(oportunidades))
                      else:
                        oportunidades -= 1
                        print(oportunidades)
                        print("Fallaste! Pierdes una vida. \n")
                        print("Vidas: " + str(oportunidades))
<<<<<<< HEAD
                        print("Palabras usadas: " + str(palabras_usadas[0::1]))
                      if oportunidades == 0:
                        print("Ha perdido!")
                        print("Su puntaje fue de: " + str(puntaje) + " palabras!")

                        incorrectas = 0
                        usuario = input("Ingrese su nombre: ")
                        punteo = {"Nombre": usuario, "Correctas":puntaje, "Incorrectas":incorrectas}
                        r = agregar_estadisticas(db, usuario, punteo, puntaje, incorrectas)

                        if r == 1:
                               print("Las puntuaciones se agregaron con exito")
                               print(" ")
                               sleep(1)
                        else:
                               print("Las puntuaciones no se agregaron")
                               print(" ")
                               sleep(1)
                        
=======
                        print("Palabras usadas: " + palabras_usadas[0::1])
                      if oportunidades == 0:
                        print("Ha perdido!")
                        print("Su puntaje fue de: " + str(puntaje) + " palabras!")
>>>>>>> d9dbc92bdf4c46710d99fa6e2ebdb85be3a57f2e
                        desea_jugar = input("Desea jugar de nuevo? (si/no) \n")
                elif opcionJuegos == 3:
                  print("Casi terminado. P.D: Extra! \n")
                else:
                  print("Por favor ingrese las opciones del menu. \n")
              print(mensajeBienvenida)
              print(menuInicio)
              opcionInicio=int(input())
       if(opcionInicio==3):
              #Comprenseion lectora mich
              questionario= int(input("Que articulo leyo?\n1)Tabaco frena el desarrollo en Guatemala\n2)Impulsan mejores contorles\n3)Salir\n"))
              correctas=0
              incorrectas=0
              coleccion = db.Preguntas
              while(questionario !=3):
                 if(questionario==1): 
                    preguntas=coleccion.find({"Articulo":"Tabaco frena el desarrollo en Guatemala"},{"_id":0,"Articulo":0})
                    for item in preguntas:
                           a= item
                    for objeto in a:
                           print(objeto)
                           respuestas=a[objeto]
                           for item in respuestas:
                                  print (item)
                    respuesta1=input("Ingrese la respuesta de la pregunta 1\n")
                    respuesta2=input("Ingrese la respuesta de la pregunta 2\n")
                    if(respuesta1=="2"):
                        correctas+=1
                        total_correctas+=1
                    else:
                        incorrectas+=1
                        total_incorrectas+=1
                    if(respuesta2=="2"):
                        correctas+=1
                        total_correctas+=1
                    else:
                        incorrectas+=1
                        total_incorrectas+=1
                    print("Respuestas correctas: "+str(correctas))
                    print("Respuestas incorrectas: "+str(incorrectas))
                    
                     
                    
                    usuario = input("Ingrese su nombre: ")
                    punteo = {"Nombre": usuario, "Correctas":correctas, "Incorrectas":incorrectas}
                    r = agregar_estadisticas(db, usuario, punteo, correctas, incorrectas)

                    if r == 1:
                           print("Las puntuaciones se agregaron con exito")
                           print(" ")
                           sleep(1)
                    else:
                           print("Las puntuaciones no se agregaron")
                           print(" ")
                           sleep(1)
 
                    correctas=0
                    incorrectas=0
                    questionario= int(input("Que articulo leyo?\n1)Tabaco frena el desarrollo en Guatemala\n2)Impulsan mejores contorles\n3)Salir\n"))
                    
                 if(questionario==2):
                    preguntas=coleccion.find({"Articulo":"Impulsan mejores contorles"},{"_id":0,"Articulo":0})
                    for item in preguntas:
                           a= item
                    for objeto in a:
                           print(objeto)
                           respuestas=a[objeto]
                           for item in respuestas:
                                  print (item)
                    respuesta1=input("Ingrese la respuesta de la pregunta 1\n")
                    respuesta2=input("Ingrese la respuesta de la pregunta 2\n")
                    if(respuesta1=="1"):
                        correctas+=1
                        total_correctas+=1
                    else:
                        incorrectas+=1
                        total_incorrectas+=1
                    if(respuesta2=="2"):
                        correctas+=1
                        total_correctas+=1
                    else:
                        incorrectas+=1
                        total_incorrectas+=1
                    print("Respuestas correctas: "+str(correctas))
                    print("Respuestas incorrectas: "+str(incorrectas))
                    

                    usuario = input("Ingrese su nombre: ")
                    punteo = {"Nombre": usuario, "Correctas":correctas, "Incorrectas":incorrectas}
                    r = agregar_estadisticas(db, usuario, punteo, correctas, incorrectas)

                    if r == 1:
                           print("Las puntuaciones se agregaron con exito")
                           print(" ")
                           sleep(1)
                    else:
                           print("Las puntuaciones no se agregaron")
                           print(" ")
                           sleep(1)
                           
                    correctas=0
                    incorrectas=0
                    questionario= int(input("Que articulo leyo?\n1)Tabaco frena el desarrollo en Guatemala\n2)Impulsan mejores contorles\n3)Salir\n"))
                 if(questionario>3):
                        print("Esa no es una opcion del menu")
                        questionario= int(input("Que articulo leyo?\n1)Tabaco frena el desarrollo en Guatemala\n2)Impulsan mejores contorles\n3)Salir\n"))
              print("Total de respuestas correctas: "+str(total_correctas))
              print("Total de respuestas incorrectas: "+str(total_incorrectas))
              print(mensajeBienvenida)
              print(menuInicio)
              opcionInicio=int(input())
       if(opcionInicio==4):
              #Estadisticas Josue
              sleep(0.5)
              print("*******************************************************************************")
              print("                                  PROMEDIOS                                    ")
              print("*******************************************************************************")
              promedio_correctas = promedio_estadisticas(db, "Correctas")
              for i in promedio_correctas:
                     print(str(i))
              
              promedio_incorrectas = promedio_estadisticas(db, "Incorrectas")
              for i in promedio_incorrectas:
                     print(str(i))

              print(" ")
              print(" ")
              sleep(0.5)
              print("*******************************************************************************")
              print("                                     MODA                                      ")
              print("*******************************************************************************")
              moda_correctas = moda_estadisticas(db, "Correctas")
              for i in moda_correctas:
                     print("Moda de correctas: " + str(i))
              print(" ")
              moda_incorrectas = moda_estadisticas(db, "Incorrectas")
              for i in moda_incorrectas:
                     print("Moda de incorrectas: " + str(i))

              print(" ")
              print(" ")
              sleep(0.5)
              print("*******************************************************************************")
              print("                                  RESULTADOS                                   ")
              print("*******************************************************************************")
              resultado = ver_estadisticas(db)
              for i in resultado:
                     print(i)
                     sleep(0.03)

              sleep(1)
              print(mensajeBienvenida)
              print(menuInicio)
              opcionInicio=int(input())
       if(opcionInicio==5):
              opcionInicio = 5
