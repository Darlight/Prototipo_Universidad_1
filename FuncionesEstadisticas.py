#FUNCIONES ESTADISTICAS

def ver_estadisticas(db):
    s = []
    m = []
    col = db["proyecto"]
    estadisticas = col.find()
    for i in estadisticas:
        s.append(i)
    for i in s:
        for j in i:
            usuario = i.get(j)
            resultado = (str(j) + ": " + str(usuario))
            m.append(resultado)
    return(m)

def agregar_estadisticas(db, usuario):
    exito = -1
    col = db["proyecto"]
    if (buscar_estadisticas(db, usuario) == False):
        col.insert(usuario)
        exito = 1
    return(exito)

def buscar_estadisticas(db, nombre):
    col = db["proyecto"]
    resultado = col.find({"Nombre":nombre}).count() > 0
    return resultado

def modificar_estadisticas(db, nombre, cambios):
    exito = -1
    col = db["proyecto"]
    if (buscar_estadisticas(db, nombre) == True):
        col.update({"Nombre":nombre}, {"$set":cambios})
        exito = 1
    return(exito)
