'''
Programa para gestionar listín telefónico con nombres y teléfonos de clientes de una empresa. 
Incorporar funciones crear el fichero con el listín si no existe, para consultar el teléfono 
de un cliente, añadir el teléfono de un nuevo cliente y eliminar el teléfono de un cliente. 
El listín debe estar guardado en el fichero de texto listin.txt donde el nombre del cliente 
y su teléfono deben aparecer separados por comas y cada cliente en una línea distinta.
'''

def new():
    name = input("Nombre: ").capitalize()
    phone = input("Teléfono: ")
    f = open("list.txt", "a")
    f.write("\n" + name + ", " + phone)
    f.close()
#end new

def search():
    name = input("Nombre de cliente: ").capitalize()
    f = open("list.txt", "r")
    clients = f.read().split("\n")
    for n in clients:
        if name in n:
            f.close()
            return print(n)       #si encuentra, rompe la función
    print("Ese cliente no existe")
    f.close()
#end search()

def delete():
    name = input("Qué cliente quieres borrar? ").capitalize()
    f = open("list.txt", "r")
    clients = f.readlines()          #guardo las líneas en la variable
    f.close()
    f = open("list.txt", 'w')           #creo fichero vacío
    for c in clients:             #si la línea guardada en la varible, no contiene el nombre, la escribo de nuevo
        if name not in c:
            f.write(c)
    print("El cliente ha sido borrado")       
    f.close()
#end delete   
    
try:
    f = open("list.txt", "r")
    f.close()
except:
    f = open("list.txt", 'w')
    f.write("LISTIN CLIENTES")
    f.close()

print('''Bienvenido al listín telefónico. Opciones:
    1-Añadir nuevo cliente
    2-Consultar teléfono de cliente
    3-Eliminar teléfono ''')
option = input("¿Qué quieres hacer? ")
if option == "1":
    new()
elif option == "2":
    search()
else:
    delete()










