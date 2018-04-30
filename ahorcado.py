import random
from palabras import lista_de_palabras
from funciones import dibujo
print ("Bienvenido al Ahorcado \n")
print("Simplemente adivine la palabra, tiene 7 oportunidades para no ser Ahorcado\n")
desea_jugar = True

# usar "letra" in "palabra" para que el juego funcione.
# crear el stickman con: "O", "I", "/", "\" y el palo.
while desea_jugar == True:
	palabra_elegida = random.choice(lista_de_palabras)
	oportunidades = 0
	ganador = 0
	letras_separadas = list(palabra_elegida)
	for guion in range(len(letras_separadas)):
		letras_separadas[guion] = "_"
	while oportunidades != 7:
		estado = False
		print(" ".join(letras_separadas))

		letra_ingresada = input("Ingrese la letra deseada: ")
		if letra_ingresada in palabra_elegida:
			for i in range(len(palabra_elegida)):
				if palabra_elegida[i] == letra_ingresada:
					letras_separadas[i] = letra_ingresada
					ganador += 1
		else:
			estado = True
			oportunidades += 1
			print(dibujo(estado,oportunidades))
			vueltas = 7 - oportunidades
			print("Numero de oportunidades = " + str(vueltas))
		if ganador == len(palabra_elegida):
			oportunidades = 7
			print("Gano! la palabra correcta es: " + palabra_elegida)
		elif oportunidades == 7 and ganador!= len(palabra_elegida):
			print ("usted ha perdido, la palabra correcta era: ", palabra_elegida)
	respuesta = input("Desea jugar de nuevo? : si o no ")
	if respuesta == "si":
		desea_jugar = True
	else:
		desea_jugar = False





