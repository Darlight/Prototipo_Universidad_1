#funcionesAhorcado.py
#Fecha de creacion: 29/04/2018
#Mario Perdomo 18029 Michele Benvenuto 18232 Josue Sagastume 18173
#Funcion: dibujo del ahorcado visualmente mas otras funciones

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

def palabra_Enguiones(palabra):
  #La palabra que es elegida la convierto como una lista para
  #clasificar cada letra en una posicion de la lista
  #ejemplo: list("palabra") ==> ["p","a","l","a","b","r","a"]
  letras_en_lista = list(palabra)
  for letra in range(len(letras_en_lista)):
    letras_en_lista[letra] = "_"
  return letras_en_lista
def mostrar_LetrasUsadas(lista):
  letras_usadas = "Letras usadas:"
  #Forma elegante para mostrar las letras ya ingresadas
  for letra in range(len(lista)):
    letras_usadas += lista[letra] + ", "
  return letras_usadas

