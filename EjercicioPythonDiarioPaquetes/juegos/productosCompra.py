'''
Galería de productos; el usuario introducirá el código y el número de unidades 
del producto que desea comprar. El programa determinará el total a pagar, como una factura.
'''
from funciones.funProductosCompra import verPrecio, prueba

def empezarproductosCompra():
    print("""    Elija el producto deseado
    PRODUCTO           CÓDIGO
    Camisa.............. 1
    Cinturón............ 2
    Zapatos............. 3
    Pantalón............ 4
    Calcetines.......... 5
    Falda............... 6
    Gorra............... 7
    Sueter.............. 8
    Corbata............. 9
    Chaqueta............ 10""")
    
    continuar = True
    while continuar != False:
        verPrecio()
        prueba()
        a = input("Si desea añadir más artículos pulse 1, de lo contrario otra tecla: ")
        if a != "1":
            print("Fin factura")
            continuar = False
      
        

        

