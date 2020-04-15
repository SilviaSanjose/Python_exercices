import mysql.connector
from modelo import constantes, clases

def conectar():   #conectar con la bbdd
    my_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "db_musical"
    )
    return my_db

def registro_canciones_db(cancion):
    sql = constantes.SQL_INSERT_SONG
    my_db = conectar()
    cursor = my_db.cursor()
    val = (cancion.titulo, cancion.artista, cancion.album, cancion.anio, cancion.estilo)
    cursor.execute(sql, val)
    my_db.commit()
    id_cancion = cursor.lastrowid   #guarda el id del último registro
    my_db.disconnect()
    return id_cancion
    
def listar_canciones_lista():
    sql = constantes.SQL_LIST_SONGS
    my_db = conectar()
    cursor = my_db.cursor()    
    cursor.execute(sql)
    res_list = cursor.fetchall()    #fetchall transforma el resultado de las canciones en forma de lista
    my_db.disconnect()
    return res_list

def borrar_cancion(val_id):
    sql = constantes.SQL_BORRAR_CANCION
    my_db = conectar()
    cursor = my_db.cursor()
    val =(val_id,)
    cursor.execute(sql,val)
    my_db.commit()
    my_db.disconnect()
    
def obtener_cancion_por_id(id_editar):
    sql = constantes.SQL_OBTENER_CANCION_ID
    my_db = conectar()
    cursor = my_db.cursor()
    val = (id_editar,)
    cursor.execute(sql,val)
    res_cancion = cursor.fetchone()     #fetchone al ser solo una, no aparece como tupla, dentro de lista, solo una tupla
    my_db.disconnect()
    objeto_cancion = clases.Cancion(id = res_cancion[0], titulo = res_cancion[1], artista = res_cancion[2], album = res_cancion[3], anio = res_cancion[4], estilo = res_cancion[5])
    return objeto_cancion

def guardar_cambios_cancion_db(cancion_editada):
    sql = constantes.SQL_GUARDAR_CAMBIOS
    my_db = conectar()
    cursor = my_db.cursor()
    val = (cancion_editada.titulo, cancion_editada.artista, cancion_editada.album, cancion_editada.anio, cancion_editada.estilo, cancion_editada.id)
    cursor.execute(sql,val)
    my_db.commit()
    my_db.disconnect()

#Operación registro en tabla de usuarios
def registro_usuario_db(usuario):
    sql = constantes.SQL_INSERT_USER
    my_db = conectar()
    cursor = my_db.cursor()
    val = (usuario.usuario, usuario.email, usuario.newsletter, usuario.eventos)
    cursor.execute(sql, val)
    my_db.commit()
    my_db.disconnect()

def mostrar_usuarios():
    sql = constantes.SQL_LIST_USER
    my_db = conectar()
    cursor = my_db.cursor()
    cursor.execute(sql)
    res_user = cursor.fetchall()
    my_db.disconnect()
    return res_user

def buscar_usuario(user_name):
    sql = constantes.SQL_OBTENER_USER
    my_db = conectar()
    cursor = my_db.cursor()
    us = (user_name,)
    cursor.execute(sql,us)
    res_user = cursor.fetchone()
    my_db.disconnect()
    return res_user
    
  
