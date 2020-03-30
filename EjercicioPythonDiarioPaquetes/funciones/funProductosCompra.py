'''
módulo funciones ejercicio Productos Compra
'''
from clases.clasesProductosCompra import lista
total_factura = 0

def verPrecio():
    code = input("Introduzca el código: ")
    code_int = int(code)
    for r in lista:
        if r.codigo == code_int:
            r.verprecio()
            numeroUnidades(r.precio)
            break

def numeroUnidades(precio):
    global total_articulo
    unit = input("Introduce el número de unidades: ")
    unit_int = int(unit)
    total_articulo = precio * unit_int
    print("El total a pagar por artículo es de " + str(total_articulo) + "€")

def prueba():
    global total_factura
    total_factura += total_articulo
    print("**** El total de la factura es de " + str(total_factura) + "€ ****")
    
  

