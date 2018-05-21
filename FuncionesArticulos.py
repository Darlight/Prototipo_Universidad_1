#MODULO ARTICULOS
import pymongo
conexion = pymongo.MongoClient()
db = conexion.proyecto
coleccion = db.articulos


mundial_articulo1 = {"Titulo":"Efectos del tabaco en la salud",
                     "Contenido":"""
El consumo de tabaco es la principal causa de enfermedad, discapacidad y muerte en el mundo. 
Cada año mueren más de 5 millones de personas en el mundo a causa del tabaquismo y si no se 
toman medidas adecuadas en el año 2030 serian 10 millones de muertes; 7 millones de ellas 
en países pobres. Se estima que la mitad de los fumadores muere de una enfermedad 
relacionada al consumo de tabaco y que viven en promedio 10-15 años menos que los no 
fumadores.

El consumo de tabaco afecta la salud de fumadores y de no fumadores expuestos. En 
esta sección nos vamos a enfocar en los efectos del consumo en los fumadores. Los 
primeros informes que mostraban que el consumo de tabaco es causa de enfermedad 
aparecieron a principios del siglo XX. Hasta la fecha, se han publicado miles de 
artículos y revisiones sobre el tema que muestran que el tabaquismo se asocia con 
alteraciones en todos los órganos y sistemas.

Las causas de muerte más importantes relacionadas con el consumo de tabaco son: enfermedades 
del corazón, cáncer y enfermedades respiratorias. La mayoría de los efectos adversos del 
tabaquismo son dosis dependientes, pero también es cierto que no hay un nivel de consumo 
“seguro para la salud”. El Informe del Cirujano General de los Estados Unidos de 2004 
describe con detalle las consecuencias del consumo de tabaco en la salud. El informe del 
2010 describe los mecanismos biológicos por los cuales se produce el daño.
"""}

coleccion.insert(mundial_articulo1)

coleccion = db.articulos
mundial_articulo2 = {"Titulo":"Contaminacion por colillas de cigarro",
                     "Contenido":"""
Los filtros de las colillas son un residuo bastante contaminante, pues están formados 
por acetato de celulosa, un material derivado del petroleo que, en contra de lo que 
pudiera parecer, no es biodegradable y puede llegar a tardar hasta diez años en 
descomponerse.

Hoy en día las colillas son desechadas en cualquier parte, desde aceras hasta playas o 
estaciones de sky, lo cual además de ensuciar nuestro entorno, afecta el medio ambiente, 
pues no debemos olvidar que el filtro sirve para acumular ciertas sustancias nocivas del 
tabaco, como la nicotina o el alquitrán, que con el paso del tiempo se transferirán al 
suelo o al agua, contaminándolos y afectando a la biota del entorno. De hecho, hay estudios 
que indican que una sola colilla puede llegar a contaminar ocho litros de agua.

La solución a este problema está en nuestras manos, pues debemos concienciarnos de que las 
colillas no deben tirarse al suelo ya que las papeleras de nuestras ciudades no están sólo 
para depositar bolsas o papeles, si no que de hecho, la mayoría de ellas cuentan con un 
cenicero donde poder apagar los cigarros y depositar las colillas en su interior.

Es cierto que hay algunos lugares donde deshacerse de las colillas no resulta tan sencillo, 
como las playas o la montaña, para lo cual muchos ayuntamientos han optado por repartir 
ceniceros portátiles, que no son más que un cucurucho de plástico resistente, que puede 
clavarse en la arena para ir depositando las colillas a lo largo del día de playa. En 
cualquier caso, si no disponemos de estos recursos, siempre podemos ir guardándolas dentro 
de una lata o cualquier otro recipiente que tiraremos posteriormente a una papelera.

Sin embargo, también se está innovando mucho en este campo, ya que se han desarrollado 
los filtros biodegradables, un invento novedoso que ya se usa y comercializa en muchos 
sitios, y que pude ayudar a paliar parte del problema. Están formados por una mezcla de 
cáñamo y algodón que los hace 100% biodegradables, llegando a servir como un abono natural 
para todo tipo de plantas.
"""}

coleccion.insert(mundial_articulo2)

coleccion = db.articulos
mundial_articulo3 = {"Titulo":"Reciclando colillas de cigarro",
                     "Contenido":"""
En la actualidad es importante el desarrollo de proyectos que fomenten un impacto positivo 
al ambiente y así crear conciencia a la sociedad sobre el daño que se le hace al planeta. 
Esta investigación tiene como objetivo enfocarse en ayudar a minimizar los daños que se 
hacen al ambiente por medio del reciclaje de las colillas de cigarro, ya que una sola 
colilla puede llegar a contaminar 8 litros de agua cuando son tiradas en el suelo, por los 
componentes nocivos que se encuentran en el filtro.

Las colillas de cigarro se encuentran impregnadas de un conjunto de sustancias que son 
producto de la combustión de los componentes del cigarro. Esta mezcla de alrededor de 300 
compuestos se conoce como alquitrán, y se compone de sustancias polares y apolares; la 
investigación se basa en la obtención de un polímero (filtro del cigarro llamado acetato 
de celulosa), el cual es purificado por medio de un sistema de reflujo y extracción soxhlet. 
El acetato de celulosa es un compuesto que tiene grandes características, tales como gran 
resistencia, transparencia y buena textura, parecida al algodón.

El método consiste en utilizar un balón con un solvente caliente, una cámara con las 
colillas de cigarro y un tubo refrigerante. Para favorecer la extracción completa de los 
componentes, se emplean dos solventes de extracción, etanol como un solvente polar y éter 
dietílico como un solvente no polar. Luego de realizar el proceso de purificación de las 
colillas, estas pasan a tener un tono amarillento pero al realizar varias extracciones se 
tornan de color blanco. El acetato de celulosa recuperado por sus propiedades puede 
emplearse en la fabricación de una amplia variedad de productos, entre los cuales cabe 
mencionar rollos de película, aislantes térmicos, fibras textiles, ya que estas fibras 
son moldeables y porosas.

En el proceso de la investigación se analiza el uso de nuevos solventes que sean más 
económicos pero igual de efectivos. Esto aportaría un beneficio para que el proceso de 
extracción sea viable al obtener el polímero, el cual podrá ser utilizado para fabricar 
fibras textiles.

Esta investigación también busca crear conciencia en las personas que desechan las colillas 
de cigarro en el suelo sin percatarse del daño y contaminación que están causando, ya que 
las colillas tardan en degradarse 15 años aproximadamente pero los efectos del alquitrán 
permanecen durante mucho más tiempo, por lo que al darle un uso como el descrito 
anteriormente podría evitarse significativamente el daño al ambiente.
"""}

coleccion.insert(mundial_articulo3)

coleccion = db.articulos
mundial_articulo3 = {"Titulo":"Reciclando colillas de cigarro",
                     "Contenido":"""
En la actualidad es importante el desarrollo de proyectos que fomenten un impacto positivo 
al ambiente y así crear conciencia a la sociedad sobre el daño que se le hace al planeta. 
Esta investigación tiene como objetivo enfocarse en ayudar a minimizar los daños que se 
hacen al ambiente por medio del reciclaje de las colillas de cigarro, ya que una sola 
colilla puede llegar a contaminar 8 litros de agua cuando son tiradas en el suelo, por los 
componentes nocivos que se encuentran en el filtro.

Las colillas de cigarro se encuentran impregnadas de un conjunto de sustancias que son 
producto de la combustión de los componentes del cigarro. Esta mezcla de alrededor de 300 
compuestos se conoce como alquitrán, y se compone de sustancias polares y apolares; la 
investigación se basa en la obtención de un polímero (filtro del cigarro llamado acetato 
de celulosa), el cual es purificado por medio de un sistema de reflujo y extracción soxhlet. 
El acetato de celulosa es un compuesto que tiene grandes características, tales como gran 
resistencia, transparencia y buena textura, parecida al algodón.

El método consiste en utilizar un balón con un solvente caliente, una cámara con las 
colillas de cigarro y un tubo refrigerante. Para favorecer la extracción completa de los 
componentes, se emplean dos solventes de extracción, etanol como un solvente polar y éter 
dietílico como un solvente no polar. Luego de realizar el proceso de purificación de las 
colillas, estas pasan a tener un tono amarillento pero al realizar varias extracciones se 
tornan de color blanco. El acetato de celulosa recuperado por sus propiedades puede 
emplearse en la fabricación de una amplia variedad de productos, entre los cuales cabe 
mencionar rollos de película, aislantes térmicos, fibras textiles, ya que estas fibras 
son moldeables y porosas.

En el proceso de la investigación se analiza el uso de nuevos solventes que sean más 
económicos pero igual de efectivos. Esto aportaría un beneficio para que el proceso de 
extracción sea viable al obtener el polímero, el cual podrá ser utilizado para fabricar 
fibras textiles.

Esta investigación también busca crear conciencia en las personas que desechan las colillas 
de cigarro en el suelo sin percatarse del daño y contaminación que están causando, ya que 
las colillas tardan en degradarse 15 años aproximadamente pero los efectos del alquitrán 
permanecen durante mucho más tiempo, por lo que al darle un uso como el descrito 
anteriormente podría evitarse significativamente el daño al ambiente.
"""}

coleccion.insert(mundial_articulo3)

coleccion = db.articulos
guatemala_articulo1 = {"Titulo":"Tabaco frena el desarrollo en Guatemala",
                     "Contenido":"""
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
"""}

coleccion.insert(guatemala_articulo1)

coleccion = db.articulos
guatemala_articulo2 = {"Titulo":"Impulsan mejores controles",
                     "Contenido":"""
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
"""}

coleccion.insert(guatemala_articulo2)


