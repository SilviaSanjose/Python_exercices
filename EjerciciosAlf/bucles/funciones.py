#http://aprendeconalf.es/python/ejercicios/bucles.html
from _ast import In

def ejercicio1():
    a = input("Di una palabra: ")
    b = 0
    while b < 10:
        print(a)
        b +=1
        
def ejercicio2():
    age = int(input("Dime tu edad "))
    for i in range(1,age+1):
        print(i)
        
def ejercicio3():
    n = int(input("Introduce un nº positivo "))
    for i in range(1, n+1):
        if i % 2 != 0:
            print(i)
#     for i in range(1, n+1,2):   #mas sencillo 
#         print(i)

def ejercicio4():
    n = int(input("Introduce un nº positivo "))
    for i in reversed(range(1, n+1)):
        print(i, end=",")    

def ejercicio5():
    money = float(input("Introduce dinero a invertir "))
    tax = float(input("Introduce el interés anual "))
    year = int(input("Introduce los años "))
    for i in range(1,year+1):
        money = round(money * (1 + tax/100),2)
        print("El capital el año " + str(i) + " es de " + str(money) +"€")
               
def ejercicio6():
    numero = int(input("Introduce un número "))
    i = "*"
    a = "*"
    for n in range(numero):    #opcion1
        print(i)
        i = i+a
    for a in range(1,numero+1):   #opcion2
        for j in range(a):
            print("*", end="")
        print("")
        
def ejercicio7():
    for i in range(1,11):
        for n in range(1,11):
            r= i+n
            print(str(i) + "x" + str(n) + "=" + str(r))
    
def ejercicio8():
    numero = int(input("Introduce un número "))
    for n in range(1, numero+1, 2):   #salta de 2 en dos desde el 1; impares
        for i in range(n, 0, -2):     #coge el valor de n, y salta hacia abajo para mostrar primero el mayor y luego menor
            print(i, end="")
        print("")
        
def ejercicio9():
    passwd = "cuchufleta"
    ask_passwd = ""
    while passwd != ask_passwd:
        ask_passwd = input("Introduce la contraseña ").lower()
    print("Contraseña correcta")
    
def ejercicio10():
    numero = int(input("Introduce un número mayor que 1: "))
    i = 2   #si es uno se para al comienzo al ser el resto cero en divisiones por 1
    while numero % i != 0:
        i +=1
    if i == numero:
        print("Es primo")   
    else:
        print("No es primo")
    
def ejercicio11():
    word = input("Introduce una palabra: ")
    for p in reversed(word):
        print(p)
    
def ejercicio12():
    phrase = input("Introduce una frase: ").upper()
    letter = input("Introduce una letra: ").upper()
    n = 0
    for p in phrase:
        if p == letter:
            n +=1
    print("La letra " + letter + " aparece " + str(n)+ " veces")
    
def ejercicio13():
    ask = ""
    while ask != "salir":
        ask = input("Escribe algo o 'salir' para salir del juego: ").lower()
        if ask != "salir":
            print(ask)
    print("Fin del Juego")
    



