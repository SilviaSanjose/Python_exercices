'''
módulo funciones
'''
import random
import time

puntos = 0
def introduccion():
    print ("""Estamos en una tierra llena de dragones...
    Delante nuestro se ven dos cuevas. 
        En una cueva, el dragon es amigable y compartira el tesoro contigo. 
            El otro dragon es codicioso y hambriento, y te va a comer según te vea.""")
    print ("")
#end introducion

def CambiarCueva():
    cueva = ""
    while cueva != "1" and cueva != "2":
        cueva = input("A que cueva quieres entrar? 1 o 2? ")
        if cueva != "1" and cueva != "2": 
            print("** Esa cueva no existe!!! Debes elegir sólo entre 1 y 2 **")
    return cueva
#end CambiarCueva

def cheqcueva(CambiarCueva):
    global puntos
    print ("Te acercas a la Cueva...")
    time.sleep(2)
    print ("Esta oscuro y tenebroso...")
    time.sleep(2)
    print ("Un gran dragon salta delante tuyo, abre su boca y...")
    print ("")
    time.sleep(2)
   
    
    FriendlyCueva = random.randint (1, 2)
   
    if CambiarCueva == str(FriendlyCueva):
        print ("Sonrie y te entrega el tesoro...")
        puntos += 100
        print("Bien! Obtienes 100 puntos. Total: " +str(puntos) + " puntos")
    else:
        print ("El dragon te come de un bocado....")
        print("""Ohhh :-(  Te han comido y pierdes todos tus puntos!! 
            Habías obtenido en la partida """ +str(puntos) + " puntos")
        puntos = 0
#end cheqcueva