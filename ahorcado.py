#ahorcado.py
#Fecha de creacion: 30/04/2018
#Mario Perdomo 18029 Michele Benvenuto 18232 Josue Sagastume 18173
#Funcion: El juego del ahorcado

import random
from palabras import lista_de_palabras
from funcionesAhorcado import *
print ("Bienvenido al Ahorcado \n")
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