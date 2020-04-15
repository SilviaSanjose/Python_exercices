import re

expresion_titulo = "^[a-zA-Z0-9 ñNÁÉÍÓÚáéíó]{2,40}$"
expresion_artista = "^[a-zA-Z0-9 ñNÁÉÍÓÚáéíó]{2,40}$"
expresion_album = "^[a-zA-Z0-9 -¿?ñNÁÉÍÓÚáéíó]{2,40}$"
expresion_estilo = "^[a-zA-Z0-9 ñNÁÉÍÓÚáéíó]{2,40}$"

def validacion(campo, expresion):
    validador = re.compile(expresion)
    return validador.match(campo)

