'''
módulo clases ejercicio Productos Compra
'''
class Ropa():
    def __init__(self, nombre, codigo, precio):
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio
    def verprecio(self):
        print("El precio es de " + str(self.precio) + "€" )

        
camisa = Ropa("Camisa", 1, 20)
cinturón = Ropa("Cinturon", 2, 12)
zapatos = Ropa("Zapatos", 3, 30)
pantalón = Ropa("Pantalon", 4, 35)
calcetines = Ropa("Calcetines", 5, 6)
falda = Ropa("Falda", 6, 12)
gorra = Ropa("Gorra", 7, 7)
sueter = Ropa("Sueter", 8, 25)
corbata = Ropa("Corbata", 9, 10)
chaqueta = Ropa("Chaqueta", 10, 40 )


lista = [] 
lista.append(Ropa("Camisa", 1, 20))
lista.append(Ropa("Cinturon", 2, 12))
lista.append(Ropa("Zapatos", 3, 30))
lista.append(Ropa("Pantalon", 4, 35))
lista.append(Ropa("Calcetines", 5, 6))
lista.append(Ropa("Falda", 6, 12))
lista.append(Ropa("Gorra", 7, 7))
lista.append(Ropa("Sueter", 8, 25))
lista.append(Ropa("Corbata", 9, 10))
lista.append(Ropa("Chaqueta", 10, 40 ))





