#ordenarImagen.py
#Fecha de creacion: 5/19/2018
#Mario Perdomo 18029 Michele Benvenuto 18232 Josue Sagastume 18173
#Funcion: Juego de ordenar la imagen
from funcionesOrdenarImagen import *
import random
#[0 0
# 0 0
# 0 0 ]
desea_jugar = True
rendirse = False
print("Bienvenido al OrdenaImagenes! \n")
print("Debe ordenar la imagen desorientada cambiando las posiciones de cada pedazo. \n")
print("Si no lográ el ordenamiento, puede rendirse despues de 5 intentos.")
while desea_jugar != False:
	num_generado = random.sample(range(6),6)
	mapa = [[0,0],[0,0],[0,0]]
	mapa_usuario = [[65,66],[67,68],[69,70]]
	posicion = 0
	imagen = [["",""],["",""],["",""]]
	mostrar = ""
	for i in range(3):
		for j in range(2):
			mapa[i][j] = num_generado[posicion]
			posicion += 1
#Imprime los cuadros
	while rendirse != True:
		intentos = 0
		for i in range(3):
			for j in range(2):
				imagen[i][j] = dibujo1[mapa[i][j]]
		mostrar = ""
		mostrar += "{0:<30},{1:>30}".format(imagen[0][0],imagen[0][1])
		mostrar += "{0:<30},{1:>30}".format(imagen[1][0],imagen[1][1])
		mostrar += "{0:<30},{1:>30}".format(imagen[2][0],imagen[2][1])
		print(mostrar)
		print("Posiciones en letras")
		print(chr(mapa_usuario[0][0]) + "   " + chr(mapa_usuario[0][1]))
		print(chr(mapa_usuario[1][0]) + "   " + chr(mapa_usuario[1][1]))
		print(chr(mapa_usuario[2][0]) + "   " + chr(mapa_usuario[2][1]))
		print(mapa)
		posicion_escogida = ord(input("Ingrese la posicion que desea mover: ")) - 65
		fila_escogida = posicion_escogida % 2
		columna_escogida = posicion_escogida // 2
		cambiar_posicion = ord(input("¿Cuál posición desea intercambiar?: ")) - 65
		fila_cambio = cambiar_posicion % 2
		columna_cambio = cambiar_posicion // 2
		guardar_cambio = mapa[columna_escogida][fila_escogida]
		mapa[columna_escogida][fila_escogida] = mapa[columna_cambio][fila_cambio]
		mapa[columna_cambio][fila_cambio] = guardar_cambio
		print(mapa)
		rendirse = True
	desea_jugar = False




