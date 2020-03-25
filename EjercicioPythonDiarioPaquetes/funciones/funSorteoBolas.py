'''
módulo funciones ejercicio Sorteo de Bolas
'''
from random import choice

def obtenerDescuento(shopping):
    number = choice([0, 10, 20, 25, 50])
    if number == 0:
        ball = "BLANCA"
        print("")
        print("Has sacado aleatoriamente la bola", ball)
        print("Lo siento, no tienes descuento")
    else:
        if number == 10:
            ball = "ROJA"
        elif number == 20:
            ball = "AZUL"
        elif number == 25:
            ball = "VERDE"
        else:
            ball = "AMARILLA"  
        print("")
        print("Has sacado aleatoriamente la bola", ball) 
        print("Felicidades! Tienes " + str(number) + "% de descuento")
        obtenerTotal(shopping, ball)
#end obtenerBola

def obtenerTotal(parametro1, parametro2):
    discount = 0.0
    if parametro2 == "ROJA":
        discount = parametro1 * 0.10
    elif parametro2 == "AZUL":
        discount = parametro1 * 0.20
    elif parametro2 == "VERDE":
        discount = parametro1 * 0.25
    elif parametro2 == "AMARILLA":
        discount = parametro1 * 0.50
    else:
        pass
    total = parametro1 - discount
    print("El nuevo importe a pagar es: ", total, "€")
    

