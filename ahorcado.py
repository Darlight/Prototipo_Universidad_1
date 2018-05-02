#ahorcado.py
#Fecha de creacion: 30/04/2018
#Mario Perdomo 18029 Michele Benvenuto 18232 Josue Sagastume 18173
#Funcion: El juego del ahorcado

import random
from palabras import lista_de_palabras
from funciones import dibujo
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





