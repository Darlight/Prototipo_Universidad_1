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

