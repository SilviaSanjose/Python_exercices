#SQl tabla de canciones
SQL_INSERT_SONG = "INSERT INTO `tabla_canciones` (`id`, `titulo`, `artista`, `album`, `año`,`estilo`) VALUES (NULL, %s, %s, %s, %s, %s);"
SQL_LIST_SONGS = "SELECT * FROM tabla_canciones;"
SQL_BORRAR_CANCION = "DELETE FROM tabla_canciones WHERE ID = %s;"
SQL_OBTENER_CANCION_ID = "SELECT * FROM tabla_canciones WHERE ID = %s;"
SQL_GUARDAR_CAMBIOS = "UPDATE tabla_canciones SET titulo = %s, artista = %s, album = %s, año = %s, estilo = %s WHERE ID = %s;"

#SQl tabla de usuarios
SQL_INSERT_USER = "INSERT INTO `tabla_usuarios` (`id`, `usuario`, `email`, `newsletter`, `eventos`) VALUES (NULL, %s, %s, %s, %s);"
SQL_LIST_USER = "SELECT usuario FROM tabla_usuarios;"

SQL_OBTENER_USER = "SELECT * FROM tabla_usuarios WHERE usuario = %s;"