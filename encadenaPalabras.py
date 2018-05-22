#encadenaPalabras.py
#Fecha de creacion: 5/19/2018
#Mario Perdomo 18029 Michele Benvenuto 18232 Josue Sagastume 18173
#Funcion: Juego de encadenar palabras con la ultima letra

#Se importa las funciones 
from funcionesEncadenaPalabras import *
import random
print("Bienvenido al Encadena Palabras! \n")
print("Debera generar una nueva palabra utilizando la última letra de la palabra proporcionada. \n")
print("Tendrá 3 oportunidades\n")
desea_jugar = True
#Se comienza el juego
while  desea_jugar == True:
	#Se crea el valor de oportunidades, puntaje y una lista que guarde palabras
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
			print("Palabras usadas: " + palabras_usadas[0::1])
		if oportunidades == 0:
			print("Ha perdido!")
			print("Su puntaje fue de: " + str(puntaje) + " palabras!")
			desea_jugar = input("Desea jugar de nuevo? (si/no) \n")