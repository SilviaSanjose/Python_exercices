#http://aprendeconalf.es/python/ejercicios/ficheros.html   del 1 al 5
from urllib import request

# Pide un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt 
# la tabla de multiplicar de ese número, done n es el número introducido.
def ejercicio1():
    n = int(input("Introduce un nº entero del 1 al 10 "))
    fichero = "tabla" + str(n) + ".txt"
    f = open(fichero, 'w')
    f.write("Tabla del " + str(n) + "\n")
    for i in range(1,11):
            multi = n * i
            f.write(str(n) + "x" + str(i) + "=" + str(multi) + "\n")
    f.close()
#end ejercicio1

# Pide un nº entero entre 1 y 10, lee el fichero tabla-n.txt con la tabla de multiplicar de ese número, 
# n es el número introducido, y la muestre por pantalla. Si el fichero no existe mostrarlo
def ejercicio2():     #Continucación del 1(para usar la tabla creada)
    m = int(input("Introduce un nº entero del 1 al 10 para mostrar su tabla "))
    fichero = "tabla" + str(m) + ".txt"
    try:
        f = open(fichero, 'r')
        print(f.read())
        f.close()
    except:
        print("El fichero no existe")
#end ejercicio2

# Pide dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar 
# de ese número, y muestre por pantalla la línea m del fichero. Si el fichero no existe mostrarlo
def ejercicio3():      #Continucación del 1 (para usar la tabla creada o no)
    n = int(input("Introduce un nº entero del 1 al 10 "))
    m = int(input("Introduce un nº entero del 1 al 10 "))
    fichero = "tabla" + str(n) + ".txt"
    try:
        f = open(fichero, 'r')
        lines = f.readlines()         #pasa cada línea a una lista de valores
        line = lines[m]               #seleciono la línea por indice
        print(line)
        f.close()
    except:
        print("El fichero no existe")
#end ejercicio3

# Escribir un programa que acceda a un fichero de internet mediante su url y muestre por 
# pantalla el número de palabras que contiene
def ejercicio4():
    f = request.urlopen("https://github.com/SilviaSanjose/Silvia_Python/blob/master/README.md")
    f_text = f.read()
    print(len(f_text.decode("utf-8").split()))    
#end ejercicio4

# Escribir un programa que abra el fichero con información sobre el PIB per cápita de los países de la UE
# pregunte por las iniciales de un país y muestre el PIB per cápita de ese país de todos los años disponibles.
def ejercicio5():
    f = request.urlopen("https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true")
    p = input("Dime las 2 iniciales del país que quieres ")
    lines = f.read().decode("utf-8").split("\n")    #paso a lista cada línea inicando que separe por salto linea
    for i in lines:
        if p.upper() in i:
            print("Leyenda: " + lines[0] + "\nPaís: " + i)
#end ejercicio5    


x = input("¿Qué ejercicio quieres ver? del 1 al 5 ")
if x == "1":
    ejercicio1()
elif x == "2":
    ejercicio2()
elif x == "3":
    ejercicio3()
elif x =="4":
    ejercicio4()
elif x =="5":
    ejercicio5() 
