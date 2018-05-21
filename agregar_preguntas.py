import pymongo
diccionario1={"Articulo":"Tabaco frena el desarrollo en Guatemala","1)Cuantas personas mueren al año por efermedades asosiadas al tabaco?": ["  1)6 millones","  2)7 millones "],"2)Cuanto porciento de su ingreso gastan los fumadores en cigarros?":["  1)20%","  2)10%"]}
diccionario2={"Articulo":"Impulsan mejores contorles","1)Que institucion esta impulsando la nueva iniciativa?":["  1)USAC","  2)IGGS"],"2)Cual de las siguientes NO es una razon por la cual se esta creando esta ley?":["  1)Proteger las politicas publicas de salud","  2)Disminuir la cantidad de fumadores"]}
diccionario3={"Articulo":"Efecto del tabaco en la salud","1)Cuantas personas mueren al año por efermedades asosiadas al tabaco?": ["  1)6 millones","  2)7 millones "," 3)5 millones"],"2)En que siglo se muestaran los primeros informes de enfermedades por tabaco?":["  1)XX","  2)XV","3)XI"]}
diccionario4={"Articulo":"Contaminación por colillas de cigarro","1)Que sustncias nosivas tienen las colillas?": ["  1)nicotina y alquitran","  2)cocaina y derivados del petroleo "],"2)De que están hechas las colillas biodegradables?":["  1)algodón","  2)Productos reciclados","3)Papel"]}
diccionario5={"Articulo":"Reciclando colillas de cigarro","1)Cuantos litros de agua puede contaminar una colilla?": ["  1)9","  2)8","3)7"],"2)Para que pueden servir las colillas recicladas?":["1)Papel de baño","2)Rollos de pelicula","3)Botellas para bebidas"]}
lista_preguntas= [diccionario1, diccionario2, diccionario3, diccionario4, diccionario5]
conexion= pymongo.MongoClient()
db = conexion.proyecto
coleccion = db.Preguntas

for preguntas in lista_preguntas:
    coleccion.insert(preguntas)
