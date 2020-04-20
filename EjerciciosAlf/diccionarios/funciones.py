#http://aprendeconalf.es/python/ejercicios/diccionarios.html
from _ast import In
from dotenv.cli import cli

def ejercicio1():
    divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    divisa = input("Indica divisa: Euro, Dollar o Yen: ")
    print(divisas.get(divisa.capitalize(), "No existe"))
#end ejercicio1

def ejercicio2():
    info = {
        "name":input("Escribe tu nombre: "),
        "edad":int(input("Escribe tu edad: ")),
        "direccion": input("Escribe tu direccion: "),
        "teléfono": int(input("Escribe tu teléfono: "))
        }
    print(info.get("name").title() + " tiene " + str(info.get("edad")) + " años, vive en " + 
          info.get("direccion") + " y su número de teléfono es " + str(info.get("teléfono")) )
#end ejercicio2()

def ejercicio3():
    fruits = {
        "Plátano": 1.35,
        "Manzana": 0.80,
        "Pera" : 0.85,
        "Naranja": 0.70
        }
    fruit = input("Indica fruta: ").title()
    if fruit in fruits:
        kl = float(input("Indica Kilos: "))
        a = fruits.get(fruit)
        print(a*kl)
    else:
        print("No tenemos esa fruta")
#end ejercicio3

def ejercicio4():
    months = {1:"Enero", 2: "Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio", 7: "Julio",
              8:"Agosto", 9:"Septiembre", 10:"Octubre", 11:"Noviembre", 12:"Diciembre"}
    date = input("Introduce fecha en formato dd/mm/aaaa: ")
    date_list = date.split("/")
    print(date_list[0] + " de " + months[int(date_list[1])] + " de " + date_list[2])
#end ejercicio4  
    
def ejercicio5():
    creditos = {"Mates" : 6, "Física": 4, "Química": 5}
    total = 0
    for a, c in creditos.items():
        print("La asignatura " + a + " tiene " + str(c) + " créditos")
        total += c
    print("Total de créditos: " + str(total))
#end ejercicio5

def ejercicio6(): 
    usuario = {}
    datos = "S"
    while datos == "S":
        key = input("¿que datos quieres dar? ")
        value = input(key + ": ")
        usuario[key] = value
        print(usuario)
        cont = input("¿Quieres meter más datos? S/N ").upper()
        if cont == "N":
            datos = "N"
#end ejercicio6

def ejercicio7():
    lista_compra = {} 
    articulo = "S"
    while articulo == "S":
        key = input("Indica artículo: ")
        value = float(input("Indica precio: "))
        lista_compra[key] = value
        articulo = input("Añadir más artículo? S/N: ").upper()
    print("Lista de la compra")
    total = 0
    for k, v in lista_compra.items():
        total += v
        print(k + " " + str(v))
    print("Total " + str(total))
#end ejercicio7

def ejercicio8():
    dicc = {}
    words = "S"
    while words == "S":
        user = input("Introduce las palabras en formato 'español:ingles' ")
        user_list = user.split(":")
        dicc[user_list[0]] = user_list[1]
        words = input("Introduccir más palabras: S/N ").upper()     
    phrase = input("Introduce frase a traducir: ").split()
    for p in phrase:
        if p in dicc.keys():
            print(dicc[p], end= " ")
        else:
            print(p, end= " ")
#end ejercicio8

def ejercicio9():
    facturas = {}
    pendiente = 0
    cobrado = 0
    gestion = ""
    while gestion != "C":
        gestion = input("Operaciones: Añadir factura (pulse A), pagar factura (pulse P) o cerrar (pulse C) ").upper()
        if gestion == "A":
            key = input("Introduce número de factura para añadir: ")
            value = float(input("Introduce el precio: "))
            facturas[key] = value
            pendiente += value
        if gestion == "P":
            fact = input("Introduce número de factura a pagar: ")
            print("A pagar: " + str(facturas[fact]))
            cobrado += facturas[fact]
            pendiente -= facturas[fact]
        print("Pendiente de pagar total: " + str(pendiente))
        print("Ya cobrado: " + str(cobrado))
#end ejercicio9

def ejercicio10():
    clientes ={}
    gestionar = True
    while gestionar == True:
        print('''1. Introducir datos 
2. Eliminar sus datos de la base de datos.
3. Mostrar sus datos.
4. Mostrar lista de todos los clientes con su NIF y nombre.
5. Mostrar la lista de clientes preferentes con su NIF y nombre.
6. Terminar el programa''')
        print(clientes)
        option = int(input("Elige una opción: "))
        if option == 1:
            key = input("Introduce dni: ").upper()
            nombre = input("Nombre: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            correo = input("Correo: ")
            preferente = input("Preferente S/N: ").upper()
            client = {"Nombre": nombre, "Dirección": direccion, "Teléfono": telefono, "Correo": correo, "Preferente": preferente == "S"}
            clientes[key] = client
        if option == 2:
            delete = input("Indica dni a borrar: ").upper()
            del clientes[delete]
        if option == 3:
            dni = input("Indice dni a consultar: ").upper()
            if dni in clientes:
                for k, v in clientes[dni].items():
                    if k == "Nombre":
                        print(k + " : " + v)
            else:
                print("Ese cliente no existe")
        if option ==4:
            for k,v in clientes.items():
                print(k + " : " + v["Nombre"])
        if option == 5:
            for k, v in clientes.items():
                if v["Preferente"]:
                    print(k + " : " + v["Nombre"])
            
        else:
            print("Fin del Programa")       
            gestionar = False
   
        
        
ejercicio10()

