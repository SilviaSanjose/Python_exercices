'''
Incluir sistema de puntos: Mientras el jugador vaya ganando, ira acumulando puntos.
-Si el jugador entra en la primera cueva y gana el tesoro, se le acreditan 100 puntos.
-Si entra en la segunda cueva y gana el tesoro, se le acreditan otros 100 puntos. 
-Si el jugador pierde, saldrá en pantalla el total de los puntos que realizo y la opción de empezar de nuevo.
'''
'''Mejoras:
-Incluir si elige otra cueva que no sea 1 o 2, avise de error.
-No distinga entre mayúsculas y minúsculas al jugar de nuevo Si o No
'''

from funciones.funReinoDragon import introduccion, CambiarCueva, cheqcueva

def reinoDelDragon():
    EmpezarNuevo = "si"
    
    while EmpezarNuevo.lower() == "s" or EmpezarNuevo.lower() == "si":
        introduccion()
        NumCaverna = CambiarCueva()
        cheqcueva(NumCaverna)
        print ("Quieres jugar de nuevo? (si o no)")
        EmpezarNuevo = input()
        
#reinoDelDragon()   
    
    
    
    