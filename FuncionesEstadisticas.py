#FUNCIONES ESTADISTICAS

def ver_estadisticas(db):
    s = []
    m = []
    contador = 0
    col = db["estadisticas"]
    estadisticas = col.find()
    for i in estadisticas:
        s.append(i)
    for i in s:
        for j in i:
            usuario = i.get(j)
            resultado = (str(j) + ": " + str(usuario))
            m.append(resultado)
            contador += 1
            if (contador % 4) == 0:
                x = "\n"
                m.append(x)
    return(m)

def buscar_estadisticas(db, nombre):
    col = db["estadisticas"]
    resultado = col.find({"Nombre":nombre}).count() > 0
    return resultado

def agregar_estadisticas(db, usuario, punteo, total_correctas, total_incorrectas):
    exito = -1
    col = db["estadisticas"]

    if (buscar_estadisticas(db, usuario) == False):
        col.insert(punteo)
        exito = 1
    elif (buscar_estadisticas(db, usuario) == True):
        datos_usuario = col.find({"Nombre": usuario})
        for i in datos_usuario:
            incorrectas = i["Incorrectas"] + total_incorrectas
            correctas = i["Correctas"] + total_correctas
            cambios = {"Correctas":correctas, "Incorrectas":incorrectas}
            col.update({"Nombre":usuario}, {"$set":cambios})
        exito = 1
    return(exito)

def promedio_estadisticas(db, tipo):
    coleccion = db["estadisticas"]
    datos = []
    total = 0
    contador = 0
    x = range(0, 1000)
    for j in x:
        cantidad = coleccion.find({tipo:j})
        for i in cantidad:
            total += i[tipo]
            contador += 1
    if contador == 0:
        contador = 1
    promedio = (total/contador)
    datos.append("Promedio de " + tipo.lower() + ": " + str(promedio))
    
    return datos

def moda_estadisticas(db, correcta_incorrecta):
    coleccion = db["estadisticas"]
    x = range(0,1000)
    datos = []
    
    for i in x:
        valores_correctos = coleccion.find({correcta_incorrecta:i})
        for j in valores_correctos:
            correctas = j[correcta_incorrecta]
            datos.append(correctas)

    repeticiones = 0
    for i in datos:
        apariciones = datos.count(i)
        if apariciones > repeticiones:
            repeticiones = apariciones

    modas = []
    for i in datos:
        apariciones = datos.count(i)
        if apariciones == repeticiones and i not in modas:
            modas.append(i)
    return modas




    
    

