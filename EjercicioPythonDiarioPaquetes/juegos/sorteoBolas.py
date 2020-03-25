'''
Pide la cantidad total de compras. Si es inferior a $100.00, no aplica a la promoción. 
Si es compras igual o superior a $100.00, se genera de forma aleatoria un número entero 
del cero al cinco. Cada número corresponderá a un color de bolas que hay para determinar 
el descuento que el cliente recibirá como premio.
'''
from funciones.funSorteoBolas import obtenerDescuento

def sorteoBolasDescuento():
    shopping = float(input("Total de compras: "))
    
    if shopping >= 100.00:
        print("""Participa en la promoción para obtener descuento!
                   COLOR                DESCUENTO
                BOLA BLANCA            NO TIENE :-(
                BOLA ROJA                  10%
                BOLA AZUL                  20%
                BOLA VERDE                 25%
                BOLA AMARILLA              50% """)
        obtenerDescuento(shopping)
    else:
        print("No aplica a la promoción")
        