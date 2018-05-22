#ordenarImagen.py
#Fecha de creacion: 5/19/2018
#Mario Perdomo 18029 Michele Benvenuto 18232 Josue Sagastume 18173
#Funcion: Juego de ordenar la imagen

#Se importa las funciones
from funcionesOrdenarImagen import *
import random
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
			#	  [0,0,0] ----> segunda fila
			for i in range(2):
			#Ciclo j significa la colummna de la matriz de dibujos
			#osea [0,0,0]
			#	   0 1 2
			#	  [0,0,0]
			#	   0 1 2
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


