import mysql.connector
#from imaplib import host

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "bd_revistas"
    )

print("Conexión OK")

cursor = mydb.cursor()

sql = "INSERT INTO `tabla_revistas` (`id`, `titulo`, `precio`, `tema`) VALUES (NULL, 'Muy Interesante', '5.50', 'Curiosidades');"

cursor.execute(sql)  #ejecuta los valores de la variable sql a la base de datos

mydb.commit()   #esto lanza todos los execute anteriores

print("Registro OK")