#menu_articulos.py
#Fecha de creacion: 27/04/2018
#Michele Benvenutoo 18232
#Mario Perdomo 18029 
#Josue Sagastume 18173
#Funcion: menu de los articulos
import random
import pymongo
guatemala_articulo1 = {
  "Titulo": "Tabaco frena el desarrollo en Guatemala",
  "Fuente": "Prensa Libre",
  "Contenido": """
El 2017, el mensaje de la Organización Mundial de la Salud (OMS) se enfoca en las 
repercusiones que tiene el consumo de tabaco en el desarrollo de los países, y parte de 
que siete millones de personas mueren al año por enfermedades asociadas al consumo del 
tabaco.

La OMS calcula que las familias y gobiernos invierten unos US$1 mil 400 millones al año 
(unos Q10 mil 287 millones) por gastos médicos y pérdidas de productividad, además de los 
efectos contra el ambiente, porque el residuo del tacaco contiene unas siete mil sustancias 
químicas y tóxicas, además del humo con altos contenidos de cancerígenos.

“Hay una meta que incluye la reducción de las enfermedades crónicas no transmisibles como 
cardiovasculares y el cáncer. Esas enfermedades van en aumento y están asociadas al consumo 
del tabaco,  lo que afecta a las poblaciones más desprotegidas”, resaltó Óscar Barreneche, 
representante de la OMS y Organización Panamericana de la Salud.

El informe de la OMS añade que unos 860 millones de fumadores viven en países de ingresos 
medianos o bajos y que gastan más del 10% para mantenimiento de su adicción a la nicotina, 
y le dan prioridad a ese gasto sobre necesidades básicas como la alimentación y la salud.

Berreneche reiteró la preocupación por la temprana edad en la que los niños guatemaltecos 
empiezan a consumir cigarrillos  y apoya que se endurezca la legislación contra el consumo 
de tabaco.

"""
}
guatemala_articulo2 = {
  "Titulo": "Impulsan mejores controles",
  "Fuente": "Prensa Libre",
  "Contenido": """
La Universidad de San Carlos de Guatemala impulsa una nueva iniciativa de Ley Integral 
para el Control de Tabaco que aglutina recomendaciones de la representación de la OMS y 
otras instituciones afines a la salud, cuya principal razón es que se protejan las políticas 
públicas de salud, que se regule las relaciones entre las empresas tabacaleras y las 
Instituciones del Estado, y que se mejoren los controles en la venta del producto.

“La ley se resume en proteger la salud de los guatemaltecos. La sociedad civil siempre ha 
apoyado las acciones para el control tabaco, pero el Ministerio de Salud es el responsable 
de la salud de la población y de la implementación de la Ley”, resaltó Miguel Garcés, 
integrante del Consejo Nacional Contra el Tabaco de la Universidad de San Carlos.

El viceministro de Salud, Adrián Chávez, resaltó que desde el Ejecutivo revisarán la 
iniciativa y de ser favorable para la población la apoyarían, y aseguró que no se trata 
de una acción contra las empresas, sino a favor de la personas.

"""
}
guatemala_lista_de_articulos = [guatemala_articulo1,guatemala_articulo2]
#Generador de la base de datos
#Cada lista representa artiuclos por continente
opcion = 0
conexion = pymongo.MongoClient()
db = conexion.proyecto
#Parte del modulo
coleccion = db.articulos_guatemala

for articulo in guatemala_lista_de_articulos:
  coleccion.insert(articulo)

#for articulo in guatemala_lista_de_articulos:
 # coleccion.insert(articulo)
