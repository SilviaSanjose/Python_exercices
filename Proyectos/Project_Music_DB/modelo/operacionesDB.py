import mysql.connector
from modelo import constantes



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
    my_db.disconnect()
    
def listar_canciones_lista():
    sql = constantes.SQL_LIST_SONGS
    my_db = conectar()
    cursor = my_db.cursor()    
    cursor.execute(sql)
    res_list = cursor.fetchall()    #fetchall transforma el resultado de las canciones en forma de lista
    my_db.disconnect()
    return res_list
