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
campos_a_mostrar = ["Titulo","Contenido"]

total_correctas = 0
total_incorrectas = 0

total_incorrectas=0
total_correctas=0
total_incorrectas=0
total_correctas=0

mensajeBienvenida="*******************************************************************************\nBIENVENIDO\n******************************************************************************* "
menuInicio="Elija una de las sigueintes opciones:\n 1)Leer articulo\n 2)Mini-Juegos\n 3)Comprobacion de lectura\n 4)Ver estadisticas\n 5)Salir"
print(mensajeBienvenida)
print(menuInicio)
opcionInicio=int(input())
while(opcionInicio !=5):
       if(opcionInicio==1):
              #Menu de mario
              coleccion = db.articulos_guatemala
              opcion = 0
              while opcion != 6:
                     opcion =  int(input("""
1. Tabaco frena el desarrollo de Guatemala
2. Impulsan mejores controles
6. salir
"""))
                     if opcion == 1:
                            #Resultado consigue el articulo con titulo y contenido sin el id para que sea mas presentable
                            resultado = coleccion.find_one({"Titulo":"Tabaco frena el desarrollo en Guatemala"},{"_id": 0, "Titulo": 1, "Contenido": 1})
                            for campo in campos_a_mostrar:
                                   print(str(resultado[campo]))
                     elif opcion == 2:
                            resultado = coleccion.find_one({"Titulo":"Impulsan mejores controles"},{"_id": 0, "Titulo": 1, "Contenido": 1})
                            for campo in campos_a_mostrar:
                                   print(str(resultado[campo]) + "\n")
                            else:
                                   print("En desarrollo...")
                     elif opcion == 3:
                            print("En desarrollo")
                     elif opcion == 4:
                            print("En desarrollo")
                     elif opcion == 5:
                            print("En desarrollo")
                     elif opcion == 6:
                            opcion = 6
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

                        print("Gano! la palabra correcta fue: " + palabra_elegida)
                        #De lo contrario, perdio el juego y se muestra la palabra
                      elif oportunidades == 7 and ("".join(palabra_en_guiones)) != palabra_elegida:
                        print ("usted ha perdido, la palabra correcta era: ", palabra_elegida)
                        #Se pregunta si desea jugar otra vez

                        print("Gano! la palabra correcta fue: " + palabra_elegida)
                        #De lo contrario, perdio el juego y se muestra la palabra
                      elif oportunidades == 7 and ("".join(palabra_en_guiones)) != palabra_elegida:
                        print ("usted ha perdido, la palabra correcta era: ", palabra_elegida)
                        #Se pregunta si desea jugar otra vez

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
                        

                        print("Palabras usadas: " + str(palabras_usadas[0::1]))
                      if oportunidades == 0:
                        print("Ha perdido!")
                        print("Su puntaje fue de: " + str(puntaje) + " palabras!")

                        desea_jugar = input("Desea jugar de nuevo? (si/no) \n")
                elif opcionJuegos == 3:
                  #Se crean un booleano para la repetición del juego
                  #Se crea una opcion de rendirse despues de 8 intentos
                  #P.D: Los ciclos pueden ser creados en funciones
                  #Pero lo deje asi para que entiendan la logica del programa - Mario
                  desea_jugar = True
                  print("Bienvenido al OrdenaImagenes! \n")
                  print("Debe ordenar la imagen desorientada cambiando las posiciones de cada pedazo. \n")
                  print("Despues de 6 intentos, el juego le mostrará la solución ya hecha. \n")
                  #Se comienza el juego
                  while desea_jugar == True:
                    #Esta variable es una lista que crea una lista de 6 elementos con diferentes valores sin repetición
                    num_generado = random.sample(range(6),6)
                    #Saca un dibujo aleatorio de la lista de dibujos proporcionado por el modulo
                    dibujo_aleatorio = random.choice(lista_dibujos)
                    #Se crea la variable con la condicion de ganar del juego
                    intentos = 6
                    #Se crea una matriz de 3 filas por 2 columnas
                    mapa = [[0,0,0],[0,0,0]]
                    #Este sirve como posición A B C D E F solo que en números.
                    #Su funcion es como identidad de las posiciones de los cuadros de dibujo
                    mapa_usuario = [[65,66,67],[68,69,70]]
                    #Esta variable sirve para revisar cada elemento de la lista de num_generado.
                    posicion = 0
                    #Esto guarda los cuadrados de un dibujo por cada matriz
                    #En este caso los dibujos son separados por 2 columnas y 3 filas
                    imagen = [["","",""],["","",""]]
                    #En este ciclo sea jala un elemento de la lista random de num_generado
                    #Colocando el valor de una matriz en la lista de lista de mapa
                    #Cualquier duda con esto sugiero que hagan print(mapa) para ver
                    #Como esta la variable mapa y como trabja con los otros ciclos
                    for i in range(2):
                      for j in range(3):
                        #Aqui se usa un acumulador, la posicion, hasta llegar a 6,
                        #pues todos los dibujos contiene 6 elementos
                        mapa[i][j] = num_generado[posicion]
                        posicion += 1
                    #Se comienza el juego aqui
                    while intentos != 0:
                      #Lo mismo que el ciclo anterior, solo que se pone el valor
                      #del elemento de un dibujo aleatorio en la matriz de strings
                      #Cualquier duda impriman imagen[i][j] adentro del ciclo j
                      for i in range(2):
                        for j in range(3):
                          imagen[i][j] = dibujo_aleatorio[mapa[i][j]]
                      #Este fue el desafio del proyecto en mi caso - Mario
                      #Siendo apoyado por Tomas, nos arreglemos la manera correcta para
                      #imprimir cada cuadro con su valor desde la variable de matriz
                      #de los strings
                      #El ciclo l representa la longitud, osea la altura maxima de un
                      #pedazo de dibujo, en este caso es 11 por cada cuadro
                      for l in range(11):
                        #Se crea un acumulador que contenga la primera linea
                        #de caracteres de los dos primeras columnas de la primera fila
                        primera_fila = ""
                        #Ciclo i significa la fila de la matriz de dibujos
                        #Osea [0,0,0] ---> primra fila
                        #   [0,0,0] ----> segunda fila
                        for i in range(2):
                        #Ciclo j significa la colummna de la matriz de dibujos
                        #osea [0,0,0]
                        #    0 1 2
                        #   [0,0,0]
                        #    0 1 2
                        #Range(n) ---> (0,n) --> range(1) --> (0,1) -- range(2) --> (0,2)
                          for j in range(1):
                        #El acumulador de strings guardara cada linea por la cantidad
                        #de lineas de altura.
                        #imagen[i][j] ---> Valor de un pedazo de dibujo
                        #[l*31:l*31+30] ---> [l = altura actual * posicion inicial del string]
                        #----> l*31+30 [l = altura actual * posicion inical del string + 30 ]
                        #Se le suma 30 al final por que si l = 0, entonces terminara con los
                        #primeros 30 caracteres de un cuadro
                        #Cada cuadro tiene 11 filas y 60 caracteres
                        #Al final se suma un string con valor de un espacio porque
                        #para que se separen por un espacio, indicando en la interfaz
                        #los diferentes cuadros en pantalla
                            primera_fila += imagen[i][j][l*31:l*31+30]+" "
                        print(primera_fila)

                      #Lo mismo que el anterior, solo que el rango es diferente
                      #Range(n,m) ---> (n,m) ---> Range(1,2) ---> (desde 1, hasta 2)
                      for l in range(11):
                        segunda_fila = ""
                        for i in range(2):
                          for j in range(1,2):
                            segunda_fila += imagen[i][j][l*31:l*31+30]+" "
                        print(segunda_fila)
                      for l in range(11):
                        tercera_fila = ""
                        for i in range(2):
                          for j in range(2,3):
                            tercera_fila += imagen[i][j][l*31:l*31+30]+" "
                        print(tercera_fila)
                      #Utilizando posiciones por letras mayusculas para obtener
                      #la posicion de una posicion dentro de las matrices
                      #Use mayusculas para poder operar en otras funciones mas adelantes
                      #chr(numero) ---> un valor string por orden cronologico
                      print("Posiciones en letras: ")
                      #Aqui se imprimen las posiciones para que el usuario
                      #entienda que la primera colummna en pantalla valen A, B y C
                      #La seguna colummna vale D, E y F
                      print("Cuadro 1: " + chr(mapa_usuario[0][0]) + "   " +"Cuadro 4: " +  chr(mapa_usuario[1][0]))
                      print("Cuadro 2: " + chr(mapa_usuario[0][1]) + "   " +"Cuadro 5: " +  chr(mapa_usuario[1][1]))
                      print("Cuadro 3: " + chr(mapa_usuario[0][2]) + "   " +"Cuadro 6: " +  chr(mapa_usuario[1][2]))
                      print("Intentos: " + str(intentos) + '\n')
                      print("Advertencia: No coloque otras letras aparte de las mostradas.\n Detendría el programa en general. \n")
                      #Aqui se convierte la letra mayuscula en un numero
                      #Se podria utilizar minusculas, pero los valores seran mas grandes
                      #Del 99 o algo para adelante son las letras minusculas, pero
                      #No funciono al sacar el modulo % y la division de piso //
                      posicion_escogida = ord(input("Ingrese la posicion que desea mover: ").upper()) - 65
                      #Saco el modulo del valor anterior, para sacar el residuo de un valor
                      #El residuo indica la fila de una matriz.
                      #Ejemplos: 3%3 = 0; 4%3 = 1
                      fila_escogida = posicion_escogida % 3
                      #La colummna se saca al no tomar en cuenta el residuo
                      #El valor posible de ser divisible es el valor de la columna
                      #Ejemplo: 9//2 = 4; 10//4 = 2
                      columna_escogida = posicion_escogida // 3
                      #Se pide lo mismo y el mismo metodo con la posicion que desea intercambiar
                      cambiar_posicion = ord(input("¿Cuál posición desea intercambiar?: ").upper()) - 65
                      fila_cambio = cambiar_posicion % 3
                      columna_cambio = cambiar_posicion // 3
                      #En una variable se guarda el dato actual del valor de la posicion actual
                      #de una matriz de la variable mapa
                      guardar_cambio = mapa[columna_escogida][fila_escogida]
                      #Se intercambian los valores de las variables para cambiar su posicion
                      #en las matrices
                      mapa[columna_escogida][fila_escogida] = mapa[columna_cambio][fila_cambio]
                      mapa[columna_cambio][fila_cambio] = guardar_cambio
                      intentos -= 1
                      #La forma de ganar depende de cada dibujo
                      #En este caso, todo los dibujos utilizan el metodo de ganar al tener:
                      #[0,2,4]
                      #[1,3,5]---> si lo voltean 90 grados a la derecha, es lo mismo que se muestra en pantalla.
                      #se usa esta condicion
                      if mapa[0][0] == 0 and mapa[0][1] == 2 and mapa[0][2] == 4 and mapa[1][0] == 1 and mapa[1][1] == 3 and mapa[1][2] == 5:
                        print("HA GANADO! \n")
                        for i in range(2):
                          for j in range(3):
                            imagen[i][j] = dibujo_aleatorio[mapa[i][j]]
                        for l in range(11):
                          primera_fila = ""
                          for i in range(2):
                            for j in range(1):
                              primera_fila += imagen[i][j][l*31:l*31+30]+" "
                          print(primera_fila)
                        for l in range(11):
                          segunda_fila = ""
                          for i in range(2):
                            for j in range(1,2):
                              segunda_fila += imagen[i][j][l*31:l*31+30]+" "
                          print(segunda_fila)
                        for l in range(11):
                          tercera_fila = ""
                          for i in range(2):
                            for j in range(2,3):
                              tercera_fila += imagen[i][j][l*31:l*31+30]+" "
                          print(tercera_fila)
                        terminar = True
                      elif intentos == 0:
                        print("Ha Perdido... \n")
                        print("La respuesta final era: ")
                        #Solo cambio los valores de las matrices para que coinciden la manera de ganar.
                        mapa[0][0] = 0
                        mapa[0][1] = 2
                        mapa[0][2] = 4
                        mapa[1][0] = 1
                        mapa[1][1] = 3
                        mapa[1][2] = 5
                        for i in range(2):
                          for j in range(3):
                            imagen[i][j] = dibujo_aleatorio[mapa[i][j]]
                        for l in range(11):
                          primera_fila = ""
                          for i in range(2):
                            for j in range(1):
                              primera_fila += imagen[i][j][l*31:l*31+30]+" "
                          print(primera_fila)
                        for l in range(11):
                          segunda_fila = ""
                          for i in range(2):
                            for j in range(1,2):
                              segunda_fila += imagen[i][j][l*31:l*31+30]+" "
                          print(segunda_fila)
                        for l in range(11):
                          tercera_fila = ""
                          for i in range(2):
                            for j in range(2,3):
                              tercera_fila += imagen[i][j][l*31:l*31+30]+" "
                          print(tercera_fila)
                        terminar = True
                    #Se preugunta si desea jugar de nuevo.
                    pregunta = input("Desea jugar de nuevo? Escriba si para jugar, escriba otra cosa para terminar el juego.  \n").lower()
                    if pregunta == "si":
                      desea_jugar = True
                    else:
                      desea_jugar = False

                else:
                  print("Por favor ingrese las opciones del menu. \n")
              print(mensajeBienvenida)
              print(menuInicio)
              opcionInicio=int(input())
       if(opcionInicio==3):
              #Comprenseion lectora mich
              questionario= int(input("Que articulo leyo?\n1)Tabaco frena el desarrollo en Guatemala\n2)Impulsan mejores contorles\n3)Efecto del tabaco en la salud\n4)Contaminación por colillas de cigarro\n5)Reciclando colillas de cigarro\n6)Salir\n"))
              correctas=0
              incorrectas=0
              coleccion = db.Preguntas
              while(questionario !=6):
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
                    questionario= int(input("Que articulo leyo?\n1)Tabaco frena el desarrollo en Guatemala\n2)Impulsan mejores contorles\n3)Efecto del tabaco en la salud\n4)Contaminación por colillas de cigarro\n5)Reciclando colillas de cigarro\n6)Salir\n"))
                    
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
                    questionario= int(input("Que articulo leyo?\n1)Tabaco frena el desarrollo en Guatemala\n2)Impulsan mejores contorles\n3)Efecto del tabaco en la salud\n4)Contaminación por colillas de cigarro\n5)Reciclando colillas de cigarro\n6)Salir\n"))
                 if(questionario==3): 
                    preguntas=coleccion.find({"Articulo":"Efecto del tabaco en la salud"},{"_id":0,"Articulo":0})
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
                    if(respuesta2=="1"):
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
                    questionario= int(input("Que articulo leyo?\n1)Tabaco frena el desarrollo en Guatemala\n2)Impulsan mejores contorles\n3)Efecto del tabaco en la salud\n4)Contaminación por colillas de cigarro\n5)Reciclando colillas de cigarro\n6)Salir\n"))
                 if(questionario==4): 
                    preguntas=coleccion.find({"Articulo":"Contaminación por colillas de cigarro"},{"_id":0,"Articulo":0})
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
                    if(respuesta2=="1"):
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
                    questionario= int(input("Que articulo leyo?\n1)Tabaco frena el desarrollo en Guatemala\n2)Impulsan mejores contorles\n3)Efecto del tabaco en la salud\n4)Contaminación por colillas de cigarro\n5)Reciclando colillas de cigarro\n6)Salir\n"))
                 if(questionario==5): 
                    preguntas=coleccion.find({"Articulo":"Reciclando colillas de cigarro"},{"_id":0,"Articulo":0})
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
                    questionario= int(input("Que articulo leyo?\n1)Tabaco frena el desarrollo en Guatemala\n2)Impulsan mejores contorles\n3)Efecto del tabaco en la salud\n4)Contaminación por colillas de cigarro\n5)Reciclando colillas de cigarro\n6)Salir\n"))   
                 if(questionario>6):
                        print("Esa no es una opcion del menu")
                        questionario= int(input("Que articulo leyo?\n1)Tabaco frena el desarrollo en Guatemala\n2)Impulsan mejores contorles\n3)Efecto del tabaco en la salud\n4)Contaminación por colillas de cigarro\n5)Reciclando colillas de cigarro\n6)Salir\n"))
              print("Total de respuestas correctas: "+str(total_correctas))
              print("Total de respuestas incorrectas: "+str(total_incorrectas))
              print(mensajeBienvenida)
              print(menuInicio)
              opcionInicio=int(input())
       if(opcionInicio==4):
              #Estadisticas Josue
              coleccion=db.estadisticas
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
