#funciones.py
#Fecha de creacion: 29/04/2018
#Mario Perdomo 18029 Michele Benvenuto 18232 Josue Sagastume 18173
#Funcion: dibujo del ahorcado visualmente

#
def dibujo(condicion,turnos):
  #Cada dibujo es un string y elemento de la lista muneco
	muneco = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    ========= Se murio...''']
    #Si el estado es verdadero
    #Retorna el dibujo con base
    #a cuantas oportunidades
    #contiene el usuario
	if condicion == True:
		return muneco[turnos-1]


